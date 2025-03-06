import os
import json
from elasticsearch import Elasticsearch
# from dotenv import load_dotenv
import logging

# Load environment variables
# load_dotenv()

# Set up logging
logger = logging.getLogger(__name__)

class ElasticsearchManager:
    """Class to manage Elasticsearch operations for product reviews"""
    
    def __init__(self):
        """Initialize Elasticsearch connection"""
        self.es_url = os.getenv('ELASTICSEARCH_URL')
        self.es_username = os.getenv('ELASTICSEARCH_USERNAME')
        self.es_password = os.getenv('ELASTICSEARCH_PASSWORD')
        
        # Determine which index to use based on environment
        env = os.getenv('FLASK_ENV', 'development')
        if env == 'production':
            self.index_name = os.getenv('ELASTICSEARCH_PROD_INDEX', 'picklepulse_reviews_prod')
        else:
            self.index_name = os.getenv('ELASTICSEARCH_DEV_INDEX', 'picklepulse_reviews_dev')
        
        # Connect to Elasticsearch
        try:
            # If using mock, don't actually connect
            if self.es_url == 'mock':
                logger.info("Using mock Elasticsearch")
                self.es = None
            else:
                self.es = Elasticsearch(
                    self.es_url,
                    basic_auth=(self.es_username, self.es_password)
                )
                logger.info(f"Connected to Elasticsearch at {self.es_url}")
        except Exception as e:
            logger.error(f"Failed to connect to Elasticsearch: {str(e)}")
            self.es = None
    
    def create_index(self):
        """Create the review index with appropriate mappings if it doesn't exist"""
        if not self.es:
            logger.info("Elasticsearch connection not available or using mock")
            return True
        
        # Check if index exists
        if self.es.indices.exists(index=self.index_name):
            logger.info(f"Index {self.index_name} already exists")
            return True
        
        # Define the index mappings
        mappings = {
            "mappings": {
                "properties": {
                    "id": {"type": "integer"},
                    "product_id": {"type": "integer"},
                    "title": {"type": "text", "analyzer": "english"},
                    "content": {"type": "text", "analyzer": "english"},
                    "pros": {"type": "text", "analyzer": "english"},
                    "cons": {"type": "text", "analyzer": "english"},
                    "rating": {"type": "float"},
                    "brand": {"type": "keyword"},
                    "category": {"type": "keyword"},
                    "created_at": {"type": "date"},
                    "updated_at": {"type": "date"}
                }
            },
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 1
            }
        }
        
        # Create the index
        try:
            self.es.indices.create(index=self.index_name, body=mappings)
            logger.info(f"Created index {self.index_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to create index {self.index_name}: {str(e)}")
            return False
    
    def index_review(self, review_data):
        """Index a review in Elasticsearch
        
        Args:
            review_data (dict): The review data to index
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.es:
            logger.info("Elasticsearch connection not available or using mock")
            return True
        
        try:
            self.es.index(
                index=self.index_name,
                id=review_data['id'],
                document=review_data
            )
            logger.info(f"Indexed review {review_data['id']}")
            return True
        except Exception as e:
            logger.error(f"Failed to index review {review_data.get('id')}: {str(e)}")
            return False
    
    def update_review(self, review_id, review_data):
        """Update a review in Elasticsearch
        
        Args:
            review_id (int): The ID of the review to update
            review_data (dict): The updated review data
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.es:
            logger.info("Elasticsearch connection not available or using mock")
            return True
        
        try:
            self.es.update(
                index=self.index_name,
                id=review_id,
                doc=review_data
            )
            logger.info(f"Updated review {review_id}")
            return True
        except Exception as e:
            logger.error(f"Failed to update review {review_id}: {str(e)}")
            return False
    
    def delete_review(self, review_id):
        """Delete a review from Elasticsearch
        
        Args:
            review_id (int): The ID of the review to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.es:
            logger.info("Elasticsearch connection not available or using mock")
            return True
        
        try:
            self.es.delete(
                index=self.index_name,
                id=review_id
            )
            logger.info(f"Deleted review {review_id}")
            return True
        except Exception as e:
            logger.error(f"Failed to delete review {review_id}: {str(e)}")
            return False
    
    def search_reviews(self, query, filters=None, sort=None, page=1, size=10):
        """Search for reviews using Elasticsearch
        
        Args:
            query (str): The search query
            filters (dict, optional): Filters to apply (e.g., {'brand': 'Selkirk', 'category': 'Paddles'})
            sort (str, optional): Field to sort by (e.g., 'rating:desc')
            page (int, optional): Page number
            size (int, optional): Number of results per page
            
        Returns:
            dict: Search results
        """
        if not self.es:
            logger.info("Elasticsearch connection not available or using mock")
            return {"total": 0, "results": []}
        
        # Calculate from value for pagination
        from_val = (page - 1) * size
        
        # Build the search body
        search_body = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "multi_match": {
                                "query": query,
                                "fields": ["title^2", "content", "pros", "cons"]
                            }
                        }
                    ]
                }
            },
            "from": from_val,
            "size": size
        }
        
        # Add filters if provided
        if filters:
            filter_clauses = []
            for key, value in filters.items():
                filter_clauses.append({"term": {key: value}})
            search_body["query"]["bool"]["filter"] = filter_clauses
        
        # Add sort if provided
        if sort:
            field, order = sort.split(":")
            search_body["sort"] = [{field: {"order": order}}]
        
        try:
            # Execute the search
            search_results = self.es.search(index=self.index_name, body=search_body)
            
            # Process the results
            hits = search_results.get("hits", {})
            total = hits.get("total", {}).get("value", 0)
            results = [hit["_source"] for hit in hits.get("hits", [])]
            
            return {
                "total": total,
                "results": results
            }
            
        except Exception as e:
            logger.error(f"Search error: {str(e)}")
            return {"total": 0, "results": []} 