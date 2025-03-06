"""
Review-related routes for the application.
"""
import traceback
from flask import Blueprint, render_template, request, jsonify, redirect, url_for

from app.models.reviews import (
    get_all_reviews, 
    get_review_by_id,
    get_filtered_reviews,
    get_related_reviews,
    get_unique_categories,
    get_unique_brands
)
from app.utils.image_utils import prepare_review_for_display

# Create blueprint
reviews_bp = Blueprint('reviews', __name__, url_prefix='/reviews')
api_bp = Blueprint('api', __name__, url_prefix='/api')
debug_bp = Blueprint('debug', __name__, url_prefix='/debug')

@reviews_bp.route('/')
def reviews_list():
    """Display a list of reviews with filtering options"""
    try:
        # Get filter parameters
        category = request.args.get('category', '')
        brand = request.args.get('brand', '')
        price_range = request.args.get('price_range', '')
        sort_by = request.args.get('sort_by', 'newest')
        page = request.args.get('page', 1, type=int)
        
        # Get filtered reviews
        filtered_reviews = get_filtered_reviews(
            category=category,
            brand=brand,
            price_range=price_range,
            sort_by=sort_by
        )
        
        # Pagination
        items_per_page = 9
        total_reviews = len(filtered_reviews)
        total_pages = (total_reviews + items_per_page - 1) // items_per_page
        
        if page < 1:
            page = 1
        elif page > total_pages and total_pages > 0:
            page = total_pages
        
        start_idx = (page - 1) * items_per_page
        end_idx = start_idx + items_per_page
        paginated_reviews = filtered_reviews[start_idx:end_idx]
        
        # Prepare safe reviews for display
        safe_reviews = [prepare_review_for_display(review) for review in paginated_reviews]
        
        # Get all unique categories and brands for filters
        all_categories = get_unique_categories()
        all_brands = get_unique_brands()
        
        # Prepare active filters for display
        active_filters = []
        if category:
            active_filters.append({
                'type': 'category',
                'value': category,
                'display': category.capitalize(),
                'param': 'category'
            })
        if brand:
            active_filters.append({
                'type': 'brand',
                'value': brand,
                'display': brand,
                'param': 'brand'
            })
        if price_range:
            price_display = ''
            if price_range == 'under50':
                price_display = 'Under $50'
            elif price_range == '50to100':
                price_display = '$50 - $100'
            elif price_range == 'over100':
                price_display = 'Over $100'
            
            active_filters.append({
                'type': 'price',
                'value': price_range,
                'display': price_display,
                'param': 'price_range'
            })
            
        return render_template(
            'reviews/list.html',
            reviews=safe_reviews,
            categories=all_categories,
            brands=all_brands,
            current_category=category,
            current_brand=brand,
            current_price=price_range,
            current_sort=sort_by,
            current_page=page,
            total_pages=total_pages,
            total_reviews=total_reviews,
            active_filters=active_filters
        )
    except Exception as e:
        print(f"Error in reviews_list: {str(e)}")
        traceback.print_exc()
        return render_template('404.html'), 404

@reviews_bp.route('/filter')
def apply_filter():
    """Handle filter form submission and redirect to reviews list with filters"""
    category = request.args.get('category', '')
    brand = request.args.get('brand', '')
    price_range = request.args.get('price_range', '')
    sort_by = request.args.get('sort_by', 'newest')
    
    # Build the filter query parameters
    filter_params = {}
    if category:
        filter_params['category'] = category
    if brand:
        filter_params['brand'] = brand
    if price_range:
        filter_params['price_range'] = price_range
    if sort_by:
        filter_params['sort_by'] = sort_by
        
    # Redirect to the reviews list with the filter parameters
    return redirect(url_for('reviews.reviews_list', **filter_params))

@reviews_bp.route('/clear-filters')
def clear_filters():
    """Clear all filters and redirect to the reviews list"""
    return redirect(url_for('reviews.reviews_list'))

@reviews_bp.route('/remove-filter')
def remove_filter():
    """Remove a specific filter and redirect to the reviews list with remaining filters"""
    filter_type = request.args.get('type', '')
    
    # Get current filter values
    category = request.args.get('category', '')
    brand = request.args.get('brand', '')
    price_range = request.args.get('price_range', '')
    sort_by = request.args.get('sort_by', 'newest')
    
    # Remove the specified filter
    if filter_type == 'category':
        category = ''
    elif filter_type == 'brand':
        brand = ''
    elif filter_type == 'price':
        price_range = ''
    
    # Build the filter query parameters with the remaining filters
    filter_params = {}
    if category:
        filter_params['category'] = category
    if brand:
        filter_params['brand'] = brand
    if price_range:
        filter_params['price_range'] = price_range
    if sort_by:
        filter_params['sort_by'] = sort_by
        
    # Redirect to the reviews list with the updated filter parameters
    return redirect(url_for('reviews.reviews_list', **filter_params))

@reviews_bp.route('/<int:review_id>')
def review_detail(review_id):
    """Display detailed information about a specific review"""
    try:
        # Find the review by ID
        review = get_review_by_id(review_id)
        
        if not review:
            return render_template('404.html'), 404
        
        # Prepare the review for display
        safe_review = prepare_review_for_display(review)
        
        # Get related reviews (same category)
        related_reviews = get_related_reviews(review_id, limit=3)
        safe_related_reviews = [prepare_review_for_display(r) for r in related_reviews]
        
        return render_template('reviews/detail.html', 
                               review=safe_review, 
                               related_reviews=safe_related_reviews)
    except Exception as e:
        print(f"Error rendering review detail: {str(e)}")
        traceback.print_exc()
        return render_template('404.html'), 404

# API Routes
@api_bp.route('/reviews/<int:review_id>')
def api_review_detail(review_id):
    """Return JSON data for a specific review"""
    try:
        # Find the requested review
        review = get_review_by_id(review_id)
        if not review:
            return jsonify({'error': 'Review not found'}), 404
        return jsonify(review)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/reviews')
def api_reviews_list():
    """Return JSON data for all reviews, with optional filtering"""
    try:
        # Get filter parameters
        category = request.args.get('category', '')
        brand = request.args.get('brand', '')
        price_range = request.args.get('price_range', '')
        
        # Filter reviews based on parameters
        filtered_reviews = get_filtered_reviews(
            category=category,
            brand=brand,
            price_range=price_range
        )
        
        return jsonify(filtered_reviews)
    except Exception as e:
        print(f"Error in API reviews list: {e}")
        return jsonify({'error': str(e)}), 500

# Debug Routes
@debug_bp.route('/reviews')
def debug_reviews():
    """Debug endpoint to view all reviews and their IDs"""
    try:
        reviews = get_all_reviews()
        review_list = [{'id': r['id'], 'title': r['title']} for r in reviews]
        print(f"Debug reviews endpoint called, found {len(reviews)} reviews")
        return jsonify({
            'review_count': len(reviews),
            'reviews': review_list
        })
    except Exception as e:
        print(f"Error in debug reviews: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@debug_bp.route('/review/<int:review_id>')
def debug_review(review_id):
    """Debug endpoint to examine a specific review in detail"""
    try:
        print(f"Debug review endpoint called for ID {review_id}")
        review = get_review_by_id(review_id)
        if not review:
            print(f"Review with ID {review_id} not found")
            return jsonify({'error': f'Review with ID {review_id} not found'}), 404
        print(f"Found review: {review['title']}")
        return jsonify(review)
    except Exception as e:
        print(f"Error in debug review: {e}")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500 