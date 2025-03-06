import os
from dotenv import load_dotenv
from urllib.parse import urlencode, urlparse, parse_qs, urlunparse

# Load environment variables
load_dotenv()

class AffiliateLinkFormatter:
    """Utility class for formatting affiliate links with proper tracking codes"""
    
    def __init__(self):
        """Initialize with affiliate IDs from environment variables"""
        self.affiliate_ids = {
            'amazon': os.getenv('AMAZON_AFFILIATE_ID'),
            'pickleballcentral': os.getenv('PICKLEBALLCENTRAL_AFFILIATE_ID'),
            'dickssportinggoods': os.getenv('DICKSSPORTINGGOODS_AFFILIATE_ID')
        }
    
    def format_amazon_link(self, base_url, product_id=None):
        """Format an Amazon affiliate link
        
        Args:
            base_url (str): The base product URL
            product_id (str, optional): The Amazon product ID (ASIN)
            
        Returns:
            str: Formatted affiliate link
        """
        if not self.affiliate_ids.get('amazon'):
            return base_url
            
        # Parse the URL
        parsed_url = urlparse(base_url)
        
        # Get existing query parameters
        query_params = parse_qs(parsed_url.query)
        
        # Add or update the tag parameter
        query_params['tag'] = [self.affiliate_ids['amazon']]
        
        # If product_id is provided and not in the URL, add it
        if product_id and 'dp' not in parsed_url.path:
            new_path = f"/dp/{product_id}"
            parsed_url = parsed_url._replace(path=new_path)
        
        # Rebuild the query string
        new_query = urlencode(query_params, doseq=True)
        
        # Reassemble the URL
        return urlunparse(parsed_url._replace(query=new_query))
    
    def format_pickleballcentral_link(self, base_url):
        """Format a Pickleball Central affiliate link
        
        Args:
            base_url (str): The base product URL
            
        Returns:
            str: Formatted affiliate link
        """
        if not self.affiliate_ids.get('pickleballcentral'):
            return base_url
            
        # Parse the URL
        parsed_url = urlparse(base_url)
        
        # Get existing query parameters
        query_params = parse_qs(parsed_url.query)
        
        # Add or update the affiliate parameter
        query_params['aff'] = [self.affiliate_ids['pickleballcentral']]
        
        # Rebuild the query string
        new_query = urlencode(query_params, doseq=True)
        
        # Reassemble the URL
        return urlunparse(parsed_url._replace(query=new_query))
    
    def format_dickssportinggoods_link(self, base_url):
        """Format a Dick's Sporting Goods affiliate link
        
        Args:
            base_url (str): The base product URL
            
        Returns:
            str: Formatted affiliate link
        """
        if not self.affiliate_ids.get('dickssportinggoods'):
            return base_url
            
        # Parse the URL
        parsed_url = urlparse(base_url)
        
        # Get existing query parameters
        query_params = parse_qs(parsed_url.query)
        
        # Add or update the affiliate parameter
        query_params['affiliate_id'] = [self.affiliate_ids['dickssportinggoods']]
        
        # Rebuild the query string
        new_query = urlencode(query_params, doseq=True)
        
        # Reassemble the URL
        return urlunparse(parsed_url._replace(query=new_query))
    
    def format_link(self, retailer, base_url, product_id=None):
        """Format an affiliate link based on the retailer
        
        Args:
            retailer (str): The retailer name (amazon, pickleballcentral, dickssportinggoods)
            base_url (str): The base product URL
            product_id (str, optional): The product ID for retailers that need it
            
        Returns:
            str: Formatted affiliate link
        """
        retailer = retailer.lower()
        
        if retailer == 'amazon':
            return self.format_amazon_link(base_url, product_id)
        elif retailer == 'pickleballcentral':
            return self.format_pickleballcentral_link(base_url)
        elif retailer == 'dickssportinggoods':
            return self.format_dickssportinggoods_link(base_url)
        else:
            return base_url  # Return the original URL for unsupported retailers 