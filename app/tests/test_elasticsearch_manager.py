import unittest
import os
from unittest.mock import patch, MagicMock
from app.backend.utils.elastic_search import ElasticsearchManager

class ElasticsearchManagerTestCase(unittest.TestCase):
    """Test case for the ElasticsearchManager utility"""
    
    def setUp(self):
        """Set up test environment"""
        # Set environment variables for testing
        os.environ['ELASTICSEARCH_URL'] = 'https://test-es.example.com'
        os.environ['ELASTICSEARCH_USERNAME'] = 'test_user'
        os.environ['ELASTICSEARCH_PASSWORD'] = 'test_password'
        os.environ['ELASTICSEARCH_DEV_INDEX'] = 'test_index_dev'
        os.environ['ELASTICSEARCH_PROD_INDEX'] = 'test_index_prod'
        os.environ['FLASK_ENV'] = 'development'
    
    @patch('app.backend.utils.elastic_search.Elasticsearch')
    def test_init(self, mock_elasticsearch):
        """Test initialization of ElasticsearchManager"""
        # Set up mock
        mock_es_instance = MagicMock()
        mock_elasticsearch.return_value = mock_es_instance
        
        # Create manager
        manager = ElasticsearchManager()
        
        # Verify Elasticsearch was initialized with correct parameters
        mock_elasticsearch.assert_called_once_with(
            'https://test-es.example.com',
            basic_auth=('test_user', 'test_password')
        )
        
        # Verify index name is set correctly for development
        self.assertEqual(manager.index_name, 'test_index_dev')
        
        # Test production environment
        os.environ['FLASK_ENV'] = 'production'
        manager = ElasticsearchManager()
        self.assertEqual(manager.index_name, 'test_index_prod')
    
    @patch('app.backend.utils.elastic_search.Elasticsearch')
    def test_create_index(self, mock_elasticsearch):
        """Test creating an Elasticsearch index"""
        # Set up mock
        mock_es_instance = MagicMock()
        mock_elasticsearch.return_value = mock_es_instance
        
        # Mock indices.exists to return False (index doesn't exist)
        mock_es_instance.indices.exists.return_value = False
        
        # Create manager and call create_index
        manager = ElasticsearchManager()
        result = manager.create_index()
        
        # Verify indices.exists was called with correct index name
        mock_es_instance.indices.exists.assert_called_once_with(index='test_index_dev')
        
        # Verify indices.create was called
        self.assertTrue(mock_es_instance.indices.create.called)
        self.assertTrue(result)
        
        # Test when index already exists
        mock_es_instance.indices.exists.return_value = True
        mock_es_instance.indices.create.reset_mock()
        
        result = manager.create_index()
        
        # Verify indices.create was not called
        self.assertFalse(mock_es_instance.indices.create.called)
        self.assertTrue(result)
    
    @patch('app.backend.utils.elastic_search.Elasticsearch')
    def test_index_review(self, mock_elasticsearch):
        """Test indexing a review"""
        # Set up mock
        mock_es_instance = MagicMock()
        mock_elasticsearch.return_value = mock_es_instance
        
        # Create manager and call index_review
        manager = ElasticsearchManager()
        review_data = {
            'id': 1,
            'title': 'Test Review',
            'content': 'Test content',
            'rating': 9.0
        }
        
        result = manager.index_review(review_data)
        
        # Verify index was called with correct parameters
        mock_es_instance.index.assert_called_once_with(
            index='test_index_dev',
            id=1,
            document=review_data
        )
        self.assertTrue(result)
    
    @patch('app.backend.utils.elastic_search.Elasticsearch')
    def test_update_review(self, mock_elasticsearch):
        """Test updating a review"""
        # Set up mock
        mock_es_instance = MagicMock()
        mock_elasticsearch.return_value = mock_es_instance
        
        # Create manager and call update_review
        manager = ElasticsearchManager()
        review_data = {
            'title': 'Updated Test Review',
            'rating': 9.5
        }
        
        result = manager.update_review(1, review_data)
        
        # Verify update was called with correct parameters
        mock_es_instance.update.assert_called_once_with(
            index='test_index_dev',
            id=1,
            doc=review_data
        )
        self.assertTrue(result)
    
    @patch('app.backend.utils.elastic_search.Elasticsearch')
    def test_delete_review(self, mock_elasticsearch):
        """Test deleting a review"""
        # Set up mock
        mock_es_instance = MagicMock()
        mock_elasticsearch.return_value = mock_es_instance
        
        # Create manager and call delete_review
        manager = ElasticsearchManager()
        result = manager.delete_review(1)
        
        # Verify delete was called with correct parameters
        mock_es_instance.delete.assert_called_once_with(
            index='test_index_dev',
            id=1
        )
        self.assertTrue(result)
    
    @patch('app.backend.utils.elastic_search.Elasticsearch')
    def test_search_reviews(self, mock_elasticsearch):
        """Test searching for reviews"""
        # Set up mock
        mock_es_instance = MagicMock()
        mock_elasticsearch.return_value = mock_es_instance
        
        # Mock search response
        mock_search_response = {
            'hits': {
                'total': {
                    'value': 2
                },
                'hits': [
                    {
                        '_source': {
                            'id': 1,
                            'title': 'Test Review 1',
                            'content': 'Test content 1',
                            'rating': 9.0
                        }
                    },
                    {
                        '_source': {
                            'id': 2,
                            'title': 'Test Review 2',
                            'content': 'Test content 2',
                            'rating': 8.5
                        }
                    }
                ]
            }
        }
        mock_es_instance.search.return_value = mock_search_response
        
        # Create manager and call search_reviews
        manager = ElasticsearchManager()
        result = manager.search_reviews('test', {'brand': 'Test Brand'}, 'rating:desc', 1, 10)
        
        # Verify search was called
        self.assertTrue(mock_es_instance.search.called)
        
        # Verify search results were processed correctly
        self.assertEqual(result['total'], 2)
        self.assertEqual(len(result['results']), 2)
        self.assertEqual(result['results'][0]['id'], 1)
        self.assertEqual(result['results'][1]['id'], 2)
    
    @patch('app.backend.utils.elastic_search.Elasticsearch')
    def test_connection_error(self, mock_elasticsearch):
        """Test behavior when Elasticsearch connection fails"""
        # Make Elasticsearch constructor raise an exception
        mock_elasticsearch.side_effect = Exception("Connection failed")
        
        # Create manager
        manager = ElasticsearchManager()
        
        # Verify es attribute is None
        self.assertIsNone(manager.es)
        
        # Test that methods handle the None es gracefully
        self.assertFalse(manager.create_index())
        self.assertFalse(manager.index_review({'id': 1}))
        self.assertFalse(manager.update_review(1, {}))
        self.assertFalse(manager.delete_review(1))
        
        search_result = manager.search_reviews('test')
        self.assertEqual(search_result['total'], 0)
        self.assertEqual(search_result['results'], [])

if __name__ == '__main__':
    unittest.main() 