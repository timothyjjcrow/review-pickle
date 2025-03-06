from flask import Blueprint, request, jsonify
import json
from app.database.db import get_db_session
from app.database.models import Product, Review, AffiliateLink, ProductImage
from app.backend.utils.elastic_search import ElasticsearchManager
from app.backend.utils.affiliate_link_formatter import AffiliateLinkFormatter
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Create Blueprint
review_bp = Blueprint('reviews', __name__, url_prefix='/api/reviews')

# Initialize utilities
es_manager = ElasticsearchManager()
affiliate_link_formatter = AffiliateLinkFormatter()

@review_bp.route('/', methods=['GET'])
def get_reviews():
    """Get a list of reviews, with optional filtering and search"""
    # Get query parameters
    query = request.args.get('q', '')
    brand = request.args.get('brand')
    category = request.args.get('category')
    sort = request.args.get('sort', 'created_at:desc')
    page = int(request.args.get('page', 1))
    size = int(request.args.get('size', 10))
    
    # Build filters
    filters = {}
    if brand:
        filters['brand'] = brand
    if category:
        filters['category'] = category
    
    # If there's a search query, use Elasticsearch
    if query:
        results = es_manager.search_reviews(query, filters, sort, page, size)
        return jsonify(results)
    
    # Otherwise, use the database
    try:
        db = get_db_session()
        
        # Start with a base query
        query = db.query(Review).join(Review.product)
        
        # Apply filters
        if brand:
            query = query.filter(Product.brand == brand)
        if category:
            query = query.join(Product.categories).filter(Category.name == category)
        
        # Apply sorting
        sort_field, sort_dir = sort.split(':')
        if sort_field == 'rating':
            if sort_dir == 'asc':
                query = query.order_by(Review.rating.asc())
            else:
                query = query.order_by(Review.rating.desc())
        elif sort_field == 'created_at':
            if sort_dir == 'asc':
                query = query.order_by(Review.created_at.asc())
            else:
                query = query.order_by(Review.created_at.desc())
        
        # Apply pagination
        total = query.count()
        reviews = query.offset((page - 1) * size).limit(size).all()
        
        # Convert to dict
        results = {
            "total": total,
            "results": [
                {
                    "id": review.id,
                    "product_id": review.product_id,
                    "title": review.title,
                    "content": review.content,
                    "pros": json.loads(review.pros) if review.pros else [],
                    "cons": json.loads(review.cons) if review.cons else [],
                    "rating": review.rating,
                    "author": review.author,
                    "created_at": review.created_at.isoformat(),
                    "updated_at": review.updated_at.isoformat()
                }
                for review in reviews
            ]
        }
        
        return jsonify(results)
    except Exception as e:
        logger.error(f"Error fetching reviews: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@review_bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id):
    """Get a single review by ID with all related data"""
    try:
        db = get_db_session()
        
        # Get the review with related data
        review = db.query(Review).filter(Review.id == review_id).first()
        
        if not review:
            return jsonify({"error": "Review not found"}), 404
        
        # Get the product and images
        product = db.query(Product).filter(Product.id == review.product_id).first()
        images = db.query(ProductImage).filter(ProductImage.product_id == product.id).all()
        
        # Get affiliate links and format them
        affiliate_links = db.query(AffiliateLink).filter(AffiliateLink.review_id == review_id).all()
        formatted_links = []
        
        for link in affiliate_links:
            formatted_url = affiliate_link_formatter.format_link(
                link.retailer, 
                link.base_url
            )
            formatted_links.append({
                "id": link.id,
                "retailer": link.retailer,
                "display_text": link.display_text,
                "url": formatted_url
            })
        
        # Construct the response
        response = {
            "id": review.id,
            "title": review.title,
            "content": review.content,
            "pros": json.loads(review.pros) if review.pros else [],
            "cons": json.loads(review.cons) if review.cons else [],
            "rating": review.rating,
            "author": review.author,
            "created_at": review.created_at.isoformat(),
            "updated_at": review.updated_at.isoformat(),
            "product": {
                "id": product.id,
                "name": product.name,
                "brand": product.brand,
                "description": product.description,
                "price": product.price
            },
            "images": [
                {
                    "id": image.id,
                    "url": image.image_url,
                    "alt_text": image.alt_text,
                    "is_primary": image.is_primary
                }
                for image in images
            ],
            "affiliate_links": formatted_links
        }
        
        return jsonify(response)
    except Exception as e:
        logger.error(f"Error fetching review {review_id}: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

# Routes for administrators to manage reviews
@review_bp.route('/', methods=['POST'])
def create_review():
    """Create a new review"""
    try:
        data = request.json
        db = get_db_session()
        
        # Create the new review
        new_review = Review(
            product_id=data['product_id'],
            title=data['title'],
            content=data['content'],
            pros=json.dumps(data.get('pros', [])),
            cons=json.dumps(data.get('cons', [])),
            rating=data['rating'],
            author=data.get('author'),
            is_published=data.get('is_published', False)
        )
        
        db.add(new_review)
        db.flush()  # Get the ID without committing
        
        # Add affiliate links if provided
        if 'affiliate_links' in data:
            for link_data in data['affiliate_links']:
                new_link = AffiliateLink(
                    review_id=new_review.id,
                    retailer=link_data['retailer'],
                    base_url=link_data['base_url'],
                    display_text=link_data.get('display_text', 'Check Price')
                )
                db.add(new_link)
        
        db.commit()
        
        # Index the review in Elasticsearch if it's published
        if new_review.is_published:
            # Get product data for indexing
            product = db.query(Product).filter(Product.id == new_review.product_id).first()
            
            # Prepare review data for indexing
            review_data = {
                "id": new_review.id,
                "product_id": new_review.product_id,
                "title": new_review.title,
                "content": new_review.content,
                "pros": json.loads(new_review.pros) if new_review.pros else [],
                "cons": json.loads(new_review.cons) if new_review.cons else [],
                "rating": new_review.rating,
                "brand": product.brand,
                "created_at": new_review.created_at.isoformat(),
                "updated_at": new_review.updated_at.isoformat()
            }
            
            es_manager.index_review(review_data)
        
        return jsonify({"id": new_review.id, "message": "Review created successfully"}), 201
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating review: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@review_bp.route('/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    """Update an existing review"""
    try:
        data = request.json
        db = get_db_session()
        
        # Find the review
        review = db.query(Review).filter(Review.id == review_id).first()
        if not review:
            return jsonify({"error": "Review not found"}), 404
        
        # Update fields
        if 'title' in data:
            review.title = data['title']
        if 'content' in data:
            review.content = data['content']
        if 'pros' in data:
            review.pros = json.dumps(data['pros'])
        if 'cons' in data:
            review.cons = json.dumps(data['cons'])
        if 'rating' in data:
            review.rating = data['rating']
        if 'author' in data:
            review.author = data['author']
        if 'is_published' in data:
            review.is_published = data['is_published']
        
        # Update affiliate links if provided
        if 'affiliate_links' in data:
            # Delete existing links
            db.query(AffiliateLink).filter(AffiliateLink.review_id == review_id).delete()
            
            # Add new links
            for link_data in data['affiliate_links']:
                new_link = AffiliateLink(
                    review_id=review_id,
                    retailer=link_data['retailer'],
                    base_url=link_data['base_url'],
                    display_text=link_data.get('display_text', 'Check Price')
                )
                db.add(new_link)
        
        db.commit()
        
        # Update in Elasticsearch if published
        if review.is_published:
            # Get product data for indexing
            product = db.query(Product).filter(Product.id == review.product_id).first()
            
            # Prepare review data for indexing
            review_data = {
                "id": review.id,
                "product_id": review.product_id,
                "title": review.title,
                "content": review.content,
                "pros": json.loads(review.pros) if review.pros else [],
                "cons": json.loads(review.cons) if review.cons else [],
                "rating": review.rating,
                "brand": product.brand,
                "created_at": review.created_at.isoformat(),
                "updated_at": review.updated_at.isoformat()
            }
            
            es_manager.update_review(review_id, review_data)
        elif data.get('is_published') is False:
            # If unpublished, remove from Elasticsearch
            es_manager.delete_review(review_id)
        
        return jsonify({"message": "Review updated successfully"})
    except Exception as e:
        db.rollback()
        logger.error(f"Error updating review {review_id}: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@review_bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    """Delete a review"""
    try:
        db = get_db_session()
        
        # Find the review
        review = db.query(Review).filter(Review.id == review_id).first()
        if not review:
            return jsonify({"error": "Review not found"}), 404
        
        # Delete from the database
        db.delete(review)
        db.commit()
        
        # Delete from Elasticsearch
        es_manager.delete_review(review_id)
        
        return jsonify({"message": "Review deleted successfully"})
    except Exception as e:
        db.rollback()
        logger.error(f"Error deleting review {review_id}: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        db.close() 