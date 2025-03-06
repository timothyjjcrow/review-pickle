"""
Image utility functions for working with product images.
This module contains helper functions for ensuring reliable image URLs.
"""

def get_reliable_product_images():
    """Returns a dictionary of reliable images for different product categories and products"""
    image_map = {
        # Paddles
        'paddles': {
            'default': "https://dickssportinggoods.imgix.net/Product/e7bc8f80-6f14-422b-82b2-ed6f5242af51/00737096-Black-White_00-1080x1080-72-RGB.jpg",
            'selkirk': "https://dickssportinggoods.imgix.net/Product/9c1e4c95-af25-4d31-9ab7-58f903dc673c/00879600-BLUE-BLUE_00-1080x1080-72-RGB.jpg",
            'joola': "https://dickssportinggoods.imgix.net/Product/f33eb400-e9b9-4e1a-a98a-d5e15bb38376/00871901-Grey-Blue_00-1080x1080-72-RGB.jpg",
            'franklin': "https://dickssportinggoods.imgix.net/Product/34d38909-4f76-4eea-9af8-eb5a71e79bb1/00751201-BLACK-BLACK_00-1080x1080-72-RGB.jpg",
            'gallery': [
                "https://dickssportinggoods.imgix.net/Product/9c1e4c95-af25-4d31-9ab7-58f903dc673c/00879600-BLUE-BLUE_00-1080x1080-72-RGB.jpg",
                "https://dickssportinggoods.imgix.net/Product/f33eb400-e9b9-4e1a-a98a-d5e15bb38376/00871901-Grey-Blue_00-1080x1080-72-RGB.jpg", 
                "https://dickssportinggoods.imgix.net/Product/e4b96e07-ce79-4ef3-9efd-d1f8c44a9101/00762901-BLACK-BLACK_00-1080x1080-72-RGB.jpg",
                "https://dickssportinggoods.imgix.net/Product/f0b63303-6de9-4a8f-a084-7b45c4c144c6/00871903-Grey-Blue_00-1080x1080-72-RGB.jpg"
            ]
        },
        # Balls
        'balls': {
            'default': "https://dickssportinggoods.imgix.net/Product/a7e83122-5c0e-4ad5-aedb-c340a2fb0583/18FRNDULT2-YELLOW-YELLOW_00-1080x1080-72-RGB.jpg",
            'franklin': "https://dickssportinggoods.imgix.net/Product/a8cf4ae1-b54d-43e7-80e4-2ecabcf87bc4/18FRNDULT-NYLW-NYLW_00-1080x1080-72-RGB.jpg",
            'dura': "https://dickssportinggoods.imgix.net/Product/ebb8a5e4-1b1e-43c1-bb6c-c16eb9f4c1df/00750001-Yellow-Yellow_00-1080x1080-72-RGB.jpg",
            'gallery': [
                "https://dickssportinggoods.imgix.net/Product/a7e83122-5c0e-4ad5-aedb-c340a2fb0583/18FRNDULT2-YELLOW-YELLOW_00-1080x1080-72-RGB.jpg",
                "https://dickssportinggoods.imgix.net/Product/ebb8a5e4-1b1e-43c1-bb6c-c16eb9f4c1df/00750001-Yellow-Yellow_00-1080x1080-72-RGB.jpg",
                "https://dickssportinggoods.imgix.net/Product/a8cf4ae1-b54d-43e7-80e4-2ecabcf87bc4/18FRNDULT-NYLW-NYLW_00-1080x1080-72-RGB.jpg", 
                "https://dickssportinggoods.imgix.net/Product/36b2a307-b34e-409a-87bd-c0a3aa4a779f/00751101-YELLOW-YELLOW_00-1080x1080-72-RGB.jpg"
            ]
        },
        # Shoes
        'shoes': {
            'default': "https://dickssportinggoods.imgix.net/Product/3f0202ec-9eb1-4b49-af99-4d52ab2a878f/22KNMWKSWFTBLMN8MTEN-WHITE-BLACK_00-1080x1080-72-RGB.jpg",
            'k-swiss': "https://dickssportinggoods.imgix.net/Product/7aa21e7c-e0fe-4be3-85f6-507e41d8be5e/21KSWMEXPRSLTEMNS-WHITE-HIGHRISE_00-1080x1080-72-RGB.jpg",
            'asics': "https://dickssportinggoods.imgix.net/Product/86baa2c5-aca5-47a3-9aee-89bb50d04fc9/22ASCMGLRSLTN8FFMTEN-WHITE-PEACOAT_00-1080x1080-72-RGB.jpg",
            'gallery': [
                "https://dickssportinggoods.imgix.net/Product/3f0202ec-9eb1-4b49-af99-4d52ab2a878f/22KNMWKSWFTBLMN8MTEN-WHITE-BLACK_00-1080x1080-72-RGB.jpg",
                "https://dickssportinggoods.imgix.net/Product/7aa21e7c-e0fe-4be3-85f6-507e41d8be5e/21KSWMEXPRSLTEMNS-WHITE-HIGHRISE_00-1080x1080-72-RGB.jpg",
                "https://dickssportinggoods.imgix.net/Product/86baa2c5-aca5-47a3-9aee-89bb50d04fc9/22ASCMGLRSLTN8FFMTEN-WHITE-PEACOAT_00-1080x1080-72-RGB.jpg",
                "https://dickssportinggoods.imgix.net/Product/0fe8be80-44c9-4fd0-8c40-0bef3c59d34e/22KSWMULTRSHTMLTCTM-WHITE-NAVY_00-1080x1080-72-RGB.jpg"
            ]
        },
        # Bags
        'bags': {
            'default': "https://dickssportinggoods.imgix.net/Product/45a3bcff-1a6c-4c76-b2c7-ae47f5e66489/00847701-black-black_00-1080x1080-72-RGB.jpg",
            'franklin': "https://dickssportinggoods.imgix.net/Product/c0bd1bb8-8f7d-4d57-bc36-a8a0367c19bd/21FRNSNGPCKBLBGP-KHAKI-KHAKI_00-1080x1080-72-RGB.jpg",
            'onix': "https://dickssportinggoods.imgix.net/Product/9f9aec35-1b19-4a20-8b14-f5f0b2ae26e5/00847802-GREY-GREY_00-1080x1080-72-RGB.jpg",
            'gallery': [
                "https://dickssportinggoods.imgix.net/Product/45a3bcff-1a6c-4c76-b2c7-ae47f5e66489/00847701-black-black_00-1080x1080-72-RGB.jpg",
                "https://dickssportinggoods.imgix.net/Product/c0bd1bb8-8f7d-4d57-bc36-a8a0367c19bd/21FRNSNGPCKBLBGP-KHAKI-KHAKI_00-1080x1080-72-RGB.jpg",
                "https://dickssportinggoods.imgix.net/Product/9f9aec35-1b19-4a20-8b14-f5f0b2ae26e5/00847802-GREY-GREY_00-1080x1080-72-RGB.jpg",
                "https://dickssportinggoods.imgix.net/Product/6b5d3ea5-b1f2-47b0-9ce5-15e4eef11ecb/00847703-TEAL-TEAL_00-1080x1080-72-RGB.jpg"
            ]
        }
    }
    
    return image_map

def sanitize_image_urls(reviews):
    """Replace Amazon image URLs with reliable images
    
    Args:
        reviews: List of review dictionaries to process
        
    Returns:
        None, modifies reviews in place
    """
    # Get reliable image map
    image_map = get_reliable_product_images()
    
    for review in reviews:
        category = review.get('category', '')
        brand = review.get('brand', '').lower()
        
        # Get category images or default to paddles
        category_images = image_map.get(category, image_map.get('paddles'))
        
        # Try to get brand-specific image or use category default
        if brand and brand in category_images:
            image_url = category_images[brand]
        else:
            image_url = category_images['default']
            
        # Set the main image URL
        review['image_url'] = image_url
        
        # Set gallery images
        if category in image_map and 'gallery' in image_map[category]:
            review['gallery'] = image_map[category]['gallery']
        else:
            # Fallback to a list with just the main image
            review['gallery'] = [image_url]

def validate_review_data(reviews):
    """Ensure all reviews have required fields
    
    Args:
        reviews: List of review dictionaries to validate
        
    Returns:
        None, modifies reviews in place
    """
    for review in reviews:
        # Ensure affiliate_links exists
        if 'affiliate_links' not in review:
            review['affiliate_links'] = {
                'amazon': '#',
                'official_store': '#'
            }
        # Ensure gallery is a list
        if 'gallery' not in review or not review['gallery']:
            review['gallery'] = [review['image_url']]
        # Ensure specs exist
        if 'specs' not in review:
            review['specs'] = {}
        # Ensure pros and cons exist
        if 'pros' not in review:
            review['pros'] = []
        if 'cons' not in review:
            review['cons'] = []
        # Ensure id is an integer
        if 'id' in review and not isinstance(review['id'], int):
            try:
                review['id'] = int(review['id'])
            except (ValueError, TypeError):
                # Assign a unique ID if conversion fails
                review['id'] = len(reviews) + 1
        # Ensure image_url has a fallback
        if 'image_url' not in review or not review['image_url']:
            review['image_url'] = f"https://placehold.co/800x600/a5d6a7/ffffff?text={review['title'].replace(' ', '+') if 'title' in review else 'Product'}"

def prepare_review_for_display(review):
    """Prepare a single review for display by ensuring all fields are properly formatted
    
    Args:
        review: A review dictionary to prepare
        
    Returns:
        A copy of the review with all fields properly formatted
    """
    safe_review = review.copy()
    
    # Use our improved image selection based on category and brand
    image_map = get_reliable_product_images()
    category = safe_review.get('category', '')
    brand = safe_review.get('brand', '').lower()
    
    # Get category images
    category_images = image_map.get(category, image_map.get('paddles'))
    
    # Try to get brand-specific image or use category default
    if brand and brand in category_images:
        safe_review['image_url'] = category_images[brand]
    else:
        safe_review['image_url'] = category_images['default']
    
    # Set gallery images from our collection
    if category in image_map and 'gallery' in image_map[category]:
        safe_review['gallery'] = image_map[category]['gallery']
    else:
        # Fallback to a list with just the main image
        safe_review['gallery'] = [safe_review['image_url']]
        
    return safe_review 