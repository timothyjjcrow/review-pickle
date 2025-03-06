"""
PicklePulse - Main Entry Point
"""
import os
import sys

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Disable Flask's automatic loading of .env files
os.environ['FLASK_SKIP_DOTENV'] = '1'

# Set environment variables directly
os.environ['DB_USERNAME'] = 'postgres'
os.environ['DB_PASSWORD'] = 'password'
os.environ['DB_HOST'] = 'localhost'
os.environ['DB_PORT'] = '5432'
os.environ['DB_NAME'] = 'picklepulse'
os.environ['SECRET_KEY'] = 'dev-secret-key'
os.environ['FLASK_ENV'] = 'development'
os.environ['ELASTICSEARCH_URL'] = 'mock'

# Import the application
from app.backend.app import app

# Run the application
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 