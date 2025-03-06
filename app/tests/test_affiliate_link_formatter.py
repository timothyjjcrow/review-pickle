import unittest
import os
from app.backend.utils.affiliate_link_formatter import AffiliateLinkFormatter

class AffiliateLinkFormatterTestCase(unittest.TestCase):
    """Test case for the AffiliateLinkFormatter utility"""
    
    def setUp(self):
        """Set up test environment"""
        # Set environment variables for testing
        os.environ['AMAZON_AFFILIATE_ID'] = 'test-20'
        os.environ['PICKLEBALLCENTRAL_AFFILIATE_ID'] = 'test123'
        os.environ['DICKSSPORTINGGOODS_AFFILIATE_ID'] = 'test456'
        
        # Create formatter instance
        self.formatter = AffiliateLinkFormatter()
    
    def test_format_amazon_link(self):
        """Test formatting Amazon affiliate links"""
        # Test basic URL
        base_url = 'https://www.amazon.com/Selkirk-Pickleball-Paddle/dp/B07CZKZ7YC'
        formatted_url = self.formatter.format_amazon_link(base_url)
        self.assertIn('tag=test-20', formatted_url)
        
        # Test URL with existing parameters
        base_url = 'https://www.amazon.com/Selkirk-Pickleball-Paddle/dp/B07CZKZ7YC?ref=sr_1_1'
        formatted_url = self.formatter.format_amazon_link(base_url)
        self.assertIn('tag=test-20', formatted_url)
        self.assertIn('ref=sr_1_1', formatted_url)
        
        # Test URL with product ID
        base_url = 'https://www.amazon.com/Selkirk-Pickleball-Paddle'
        product_id = 'B07CZKZ7YC'
        formatted_url = self.formatter.format_amazon_link(base_url, product_id)
        self.assertIn('tag=test-20', formatted_url)
        self.assertIn('/dp/B07CZKZ7YC', formatted_url)
    
    def test_format_pickleballcentral_link(self):
        """Test formatting Pickleball Central affiliate links"""
        # Test basic URL
        base_url = 'https://www.pickleballcentral.com/Engage_Encore_Pro_Pickleball_Paddle_p/epep.htm'
        formatted_url = self.formatter.format_pickleballcentral_link(base_url)
        self.assertIn('aff=test123', formatted_url)
        
        # Test URL with existing parameters
        base_url = 'https://www.pickleballcentral.com/Engage_Encore_Pro_Pickleball_Paddle_p/epep.htm?color=blue'
        formatted_url = self.formatter.format_pickleballcentral_link(base_url)
        self.assertIn('aff=test123', formatted_url)
        self.assertIn('color=blue', formatted_url)
    
    def test_format_dickssportinggoods_link(self):
        """Test formatting Dick's Sporting Goods affiliate links"""
        # Test basic URL
        base_url = 'https://www.dickssportinggoods.com/p/franklin-x-40-outdoor-pickleballs-6-pack-19fraufrnklnx40pkpcb/19fraufrnklnx40pkpcb'
        formatted_url = self.formatter.format_dickssportinggoods_link(base_url)
        self.assertIn('affiliate_id=test456', formatted_url)
        
        # Test URL with existing parameters
        base_url = 'https://www.dickssportinggoods.com/p/franklin-x-40-outdoor-pickleballs-6-pack-19fraufrnklnx40pkpcb/19fraufrnklnx40pkpcb?color=yellow'
        formatted_url = self.formatter.format_dickssportinggoods_link(base_url)
        self.assertIn('affiliate_id=test456', formatted_url)
        self.assertIn('color=yellow', formatted_url)
    
    def test_format_link(self):
        """Test the general format_link method"""
        # Test Amazon
        base_url = 'https://www.amazon.com/Selkirk-Pickleball-Paddle/dp/B07CZKZ7YC'
        formatted_url = self.formatter.format_link('amazon', base_url)
        self.assertIn('tag=test-20', formatted_url)
        
        # Test Pickleball Central
        base_url = 'https://www.pickleballcentral.com/Engage_Encore_Pro_Pickleball_Paddle_p/epep.htm'
        formatted_url = self.formatter.format_link('pickleballcentral', base_url)
        self.assertIn('aff=test123', formatted_url)
        
        # Test Dick's Sporting Goods
        base_url = 'https://www.dickssportinggoods.com/p/franklin-x-40-outdoor-pickleballs-6-pack-19fraufrnklnx40pkpcb/19fraufrnklnx40pkpcb'
        formatted_url = self.formatter.format_link('dickssportinggoods', base_url)
        self.assertIn('affiliate_id=test456', formatted_url)
        
        # Test unsupported retailer
        base_url = 'https://www.unsupportedretailer.com/product123'
        formatted_url = self.formatter.format_link('unsupportedretailer', base_url)
        self.assertEqual(base_url, formatted_url)
    
    def test_missing_affiliate_ids(self):
        """Test behavior when affiliate IDs are missing"""
        # Clear environment variables
        os.environ.pop('AMAZON_AFFILIATE_ID', None)
        
        # Create new formatter instance
        formatter = AffiliateLinkFormatter()
        
        # Test that original URL is returned when affiliate ID is missing
        base_url = 'https://www.amazon.com/Selkirk-Pickleball-Paddle/dp/B07CZKZ7YC'
        formatted_url = formatter.format_amazon_link(base_url)
        self.assertEqual(base_url, formatted_url)

if __name__ == '__main__':
    unittest.main() 