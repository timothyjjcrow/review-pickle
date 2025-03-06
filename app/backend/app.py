from flask import Flask, render_template
import os
# from dotenv import load_dotenv
import logging
import sys

# Disable Flask's automatic loading of .env files
os.environ['FLASK_SKIP_DOTENV'] = '1'

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Load environment variables
# load_dotenv()

# Set environment variables directly
os.environ['DB_USERNAME'] = 'postgres'
os.environ['DB_PASSWORD'] = 'password'
os.environ['DB_HOST'] = 'localhost'
os.environ['DB_PORT'] = '5432'
os.environ['DB_NAME'] = 'picklepulse'
os.environ['SECRET_KEY'] = 'dev-secret-key'
os.environ['FLASK_ENV'] = 'development'
os.environ['ELASTICSEARCH_URL'] = 'mock'

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__, 
                template_folder='../templates',
                static_folder='../static')
    
    # Set up configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    
    try:
        # Initialize the database
        from app.database.db import init_db
        init_db()
        
        # Initialize Elasticsearch
        from app.backend.utils.elastic_search import ElasticsearchManager
        es_manager = ElasticsearchManager()
        es_manager.create_index()
        
        # Register blueprints
        from app.backend.routes.review_routes import review_bp
        app.register_blueprint(review_bp)
    except Exception as e:
        logger.error(f"Error during app initialization: {str(e)}")
    
    # Front-end routes
    @app.route('/')
    def index():
        """Home page"""
        return 'Hello, World! Welcome to PicklePulse!'
    
    @app.route('/reviews')
    def reviews_page():
        """Reviews listing page"""
        return 'Reviews Page'
    
    @app.route('/reviews/<int:review_id>')
    def review_detail(review_id):
        """Review detail page"""
        return f'Review Detail Page for Review #{review_id}'
    
    return app

# Create the application
app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 