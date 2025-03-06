from sqlalchemy import Column, Integer, String, Text, Float, Boolean, ForeignKey, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

# Association table for product categories (many-to-many)
product_categories = Table(
    'product_categories', 
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

class Product(Base):
    """Model for pickleball equipment products"""
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    brand = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    # Relationships
    reviews = relationship("Review", back_populates="product", cascade="all, delete-orphan")
    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")
    categories = relationship("Category", secondary=product_categories, back_populates="products")
    
    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', brand='{self.brand}')>"

class Category(Base):
    """Model for product categories (paddles, balls, shoes, etc.)"""
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False, unique=True)
    
    # Relationships
    products = relationship("Product", secondary=product_categories, back_populates="categories")
    
    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"

class Review(Base):
    """Model for product reviews"""
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    pros = Column(Text, nullable=True)  # Stored as JSON in the application layer
    cons = Column(Text, nullable=True)  # Stored as JSON in the application layer
    rating = Column(Float, nullable=False)
    author = Column(String(100), nullable=True)
    is_published = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    # Relationships
    product = relationship("Product", back_populates="reviews")
    affiliate_links = relationship("AffiliateLink", back_populates="review", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Review(id={self.id}, product_id={self.product_id}, title='{self.title}')>"

class ProductImage(Base):
    """Model for product images"""
    __tablename__ = 'product_images'
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    image_url = Column(String(255), nullable=False)
    alt_text = Column(String(255), nullable=True)
    is_primary = Column(Boolean, default=False)
    
    # Relationships
    product = relationship("Product", back_populates="images")
    
    def __repr__(self):
        return f"<ProductImage(id={self.id}, product_id={self.product_id})>"

class AffiliateLink(Base):
    """Model for affiliate links associated with reviews"""
    __tablename__ = 'affiliate_links'
    
    id = Column(Integer, primary_key=True)
    review_id = Column(Integer, ForeignKey('reviews.id'), nullable=False)
    retailer = Column(String(100), nullable=False)
    base_url = Column(String(255), nullable=False)
    display_text = Column(String(100), nullable=False, default="Check Price")
    
    # Relationships
    review = relationship("Review", back_populates="affiliate_links")
    
    def __repr__(self):
        return f"<AffiliateLink(id={self.id}, review_id={self.review_id}, retailer='{self.retailer}')>" 