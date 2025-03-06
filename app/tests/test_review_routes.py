import unittest
import json
from app.backend.app import create_app
from app.database.db import init_db
from app.database.models import Product, Review, AffiliateLink, ProductImage, Category
import os
import tempfile

class ReviewRoutesTestCase(unittest.TestCase):
    """Test case for the review routes"""
    
    def setUp(self):
        """Set up test client and database"""
        # Create a temporary database file
        self.db_fd, self.db_path = tempfile.mkstemp()
        
        # Configure the application for testing
        os.environ['DB_USERNAME'] = 'test'
        os.environ['DB_PASSWORD'] = 'test'
        os.environ['DB_HOST'] = 'localhost'
        os.environ['DB_PORT'] = '5432'
        os.environ['DB_NAME'] = 'test_db'
        
        # Create the test client
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
        # Initialize the database
        with self.app.app_context():
            init_db()
            self._create_test_data()
    
    def tearDown(self):
        """Clean up after tests"""
        os.close(self.db_fd)
        os.unlink(self.db_path)
    
    def _create_test_data(self):
        """Create test data in the database"""
        # Create a test product
        product = Product(
            name='Test Paddle',
            brand='Test Brand',
            description='A test paddle for testing',
            price=99.99
        )
        
        # Create a test category
        category = Category(
            name='Paddles',
            slug='paddles'
        )
        
        # Create a test review
        review = Review(
            product_id=1,
            title='Test Review',
            content='This is a test review content.',
            pros='["Good control", "Durable"]',
            cons='["Expensive", "Heavy"]',
            rating=8.5,
            author='Test Author',
            is_published=True
        )
        
        # Create a test affiliate link
        affiliate_link = AffiliateLink(
            review_id=1,
            retailer='Amazon',
            base_url='https://www.amazon.com/dp/B12345',
            display_text='Buy on Amazon'
        )
        
        # Create a test product image
        product_image = ProductImage(
            product_id=1,
            image_url='https://example.com/image.jpg',
            alt_text='Test Paddle Image',
            is_primary=True
        )
        
        # Add to database
        db = get_db_session()
        db.add(product)
        db.add(category)
        db.add(review)
        db.add(affiliate_link)
        db.add(product_image)
        db.commit()
    
    def test_get_reviews(self):
        """Test getting a list of reviews"""
        response = self.client.get('/api/reviews/')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('results', data)
        self.assertIn('total', data)
        self.assertEqual(data['total'], 1)
        self.assertEqual(len(data['results']), 1)
        self.assertEqual(data['results'][0]['title'], 'Test Review')
    
    def test_get_review(self):
        """Test getting a single review"""
        response = self.client.get('/api/reviews/1')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Test Review')
        self.assertEqual(data['rating'], 8.5)
        self.assertEqual(data['product']['name'], 'Test Paddle')
        self.assertEqual(len(data['affiliate_links']), 1)
        self.assertEqual(data['affiliate_links'][0]['retailer'], 'Amazon')
    
    def test_create_review(self):
        """Test creating a new review"""
        review_data = {
            'product_id': 1,
            'title': 'New Test Review',
            'content': 'This is a new test review.',
            'pros': ['Good quality', 'Affordable'],
            'cons': ['Limited color options'],
            'rating': 9.0,
            'author': 'New Test Author',
            'is_published': True,
            'affiliate_links': [
                {
                    'retailer': 'PickleballCentral',
                    'base_url': 'https://www.pickleballcentral.com/product123',
                    'display_text': 'Buy from Pickleball Central'
                }
            ]
        }
        
        response = self.client.post(
            '/api/reviews/',
            data=json.dumps(review_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 201)
        
        data = json.loads(response.data)
        self.assertIn('id', data)
        
        # Verify the review was created
        response = self.client.get(f'/api/reviews/{data["id"]}')
        self.assertEqual(response.status_code, 200)
        
        review_data = json.loads(response.data)
        self.assertEqual(review_data['title'], 'New Test Review')
        self.assertEqual(review_data['rating'], 9.0)
    
    def test_update_review(self):
        """Test updating an existing review"""
        update_data = {
            'title': 'Updated Test Review',
            'rating': 9.5
        }
        
        response = self.client.put(
            '/api/reviews/1',
            data=json.dumps(update_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        
        # Verify the review was updated
        response = self.client.get('/api/reviews/1')
        self.assertEqual(response.status_code, 200)
        
        review_data = json.loads(response.data)
        self.assertEqual(review_data['title'], 'Updated Test Review')
        self.assertEqual(review_data['rating'], 9.5)
    
    def test_delete_review(self):
        """Test deleting a review"""
        response = self.client.delete('/api/reviews/1')
        self.assertEqual(response.status_code, 200)
        
        # Verify the review was deleted
        response = self.client.get('/api/reviews/1')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main() 