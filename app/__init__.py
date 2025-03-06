# This file marks the app directory as a Python package
"""
Flask application factory module.
"""
import os
from flask import Flask

from app.models.reviews import get_all_reviews
from app.utils.image_utils import sanitize_image_urls, validate_review_data

def create_app(test_config=None):
    """Create and configure the Flask application

    Args:
        test_config: Configuration for testing

    Returns:
        Flask application instance
    """
    # Disable Flask's automatic loading of .env files
    os.environ['FLASK_SKIP_DOTENV'] = '1'
    
    # Create and configure app
    app = Flask(__name__, 
                static_folder='static',
                template_folder='templates')
    
    # Set default config
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        DEBUG=os.environ.get('FLASK_DEBUG', True),
    )

    if test_config is None:
        # Load instance config if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load test config
        app.config.from_mapping(test_config)
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Initialize reviews data
    reviews = get_all_reviews()
    validate_review_data(reviews)
    sanitize_image_urls(reviews)
    
    # Register blueprints
    from app.routes.home import home_bp
    from app.routes.reviews import reviews_bp, api_bp, debug_bp
    from app.routes.errors import errors_bp
    
    app.register_blueprint(home_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(debug_bp)
    app.register_blueprint(errors_bp)
    
    return app 