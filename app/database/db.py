from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os
# from dotenv import load_dotenv
import logging

# Load environment variables
# load_dotenv()

# Set up logging
logger = logging.getLogger(__name__)

# Get database connection details from environment variables
DB_USERNAME = os.getenv('DB_USERNAME', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'picklepulse')

# Create database URL
DATABASE_URL = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

try:
    # Create engine
    engine = create_engine(DATABASE_URL)
    
    # Create session factory
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)
    
    # Create base for models
    Base = declarative_base()
    Base.query = Session.query_property()
    
    logger.info(f"Connected to database at {DB_HOST}:{DB_PORT}/{DB_NAME}")
except Exception as e:
    logger.error(f"Failed to connect to database: {str(e)}")
    # Create a mock engine for development
    engine = None
    Session = None
    Base = declarative_base()

def get_db_session():
    """Get a database session"""
    if Session is None:
        logger.error("Database session is not available")
        return None
        
    db = Session()
    try:
        return db
    finally:
        db.close()

def init_db():
    """Initialize the database by creating all tables"""
    if engine is None:
        logger.error("Database engine is not available")
        return False
        
    try:
        # Import all models to ensure they are registered with Base.metadata
        from app.database.models import Product, Category, Review, ProductImage, AffiliateLink
        
        # Create tables
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
        return True
    except Exception as e:
        logger.error(f"Failed to initialize database: {str(e)}")
        return False 