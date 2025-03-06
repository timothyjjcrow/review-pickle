"""
Home routes for the application.
"""
from flask import Blueprint, render_template
from app.models.reviews import get_all_reviews, get_unique_categories, get_unique_brands

# Create blueprint
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    """Serve the homepage"""
    # Get reviews data for featured products
    all_reviews = get_all_reviews()
    
    # Get top rated reviews for featured section
    featured_reviews = sorted(all_reviews, key=lambda x: x['rating'], reverse=True)[:3]
    
    # Get unique categories and brands for filtering
    categories = get_unique_categories()
    brands = get_unique_brands()
    
    return render_template('home.html', 
                          featured_reviews=featured_reviews,
                          categories=categories,
                          brands=brands) 