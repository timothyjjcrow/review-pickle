"""
Review model and data loading.
This module handles the review data structure and mock data loading.
"""

# Sample data - in a real app, this would come from a database
def load_mock_data():
    try:
        # Sample reviews data with real pickleball product information
        reviews = [
            {
                "id": 1,
                "title": "Selkirk Sport Atlas Pickleball Paddle",
                "brand": "Selkirk",
                "category": "paddles",
                "price": 103.99,
                "rating": 4.7,
                "release_date": "2023-09-15",
                "summary": "The Selkirk Atlas is a top-rated carbon fiber pickleball paddle designed for the perfect balance of power and control with SLK Raw Carbon Fiber technology.",
                "content": "The Selkirk Sport Atlas represents a premium option in the pickleball paddle market, featuring SLK Raw Carbon Fiber construction that provides exceptional power and control. In our extensive testing, the paddle demonstrated excellent maneuverability and a large sweet spot, making it ideal for players of all skill levels. The paddle's face offers a satisfying pop on impact while maintaining precision for dinks and third-shot drops. We particularly appreciated the balanced weight distribution, which reduces arm fatigue during extended play sessions. The handle provides a comfortable grip with good sweat absorption properties. For players looking to elevate their game with a professional-grade paddle, the Selkirk Atlas delivers outstanding performance that justifies its premium price point.",
                "image_url": "https://www.selkirk.com/cdn/shop/files/AMPED-Atlas-X5-FiberFlex-Blue_900x.png",
                "gallery": [
                    "https://www.selkirk.com/cdn/shop/files/AMPED-Atlas-X5-FiberFlex-Blue_900x.png",
                    "https://www.selkirk.com/cdn/shop/files/AMPED-Atlas-X5-FiberFlex-Blue-Handle_900x.png",
                    "https://www.selkirk.com/cdn/shop/files/AMPED-Atlas-X5-FiberFlex-Blue-Edge_900x.png",
                    "https://www.selkirk.com/cdn/shop/files/AMPED-Atlas-X5-FiberFlex-Blue-Face_900x.png"
                ],
                "pros": [
                    "Premium SLK Raw Carbon Fiber construction",
                    "Excellent balance of power and control",
                    "Large sweet spot from edge to edge",
                    "Comfortable grip with good sweat absorption"
                ],
                "cons": [
                    "Premium price point",
                    "May be too advanced for absolute beginners",
                    "Limited color options"
                ],
                "specs": {
                    "Weight": "7.9-8.3 oz",
                    "Grip Size": "4 1/4 inches",
                    "Surface": "Raw Carbon Fiber",
                    "Core": "Polymer",
                    "Handle Length": "5 inches"
                },
                "affiliate_links": {
                    "amazon": "https://www.amazon.com/Selkirk-Sport-Atlas-Pickleball-Paddle/dp/B0BSS8K8G3",
                    "official_store": "https://www.selkirk.com/products/atlas-pickleball-paddle"
                }
            },
            {
                "id": 2,
                "title": "JOOLA Ben Johns Hyperion C2 Pickleball Paddle",
                "brand": "JOOLA",
                "category": "paddles",
                "price": 199.95,
                "rating": 4.6,
                "release_date": "2023-06-10",
                "summary": "The JOOLA Ben Johns Hyperion C2 Pickleball Paddle features Aero-Curve Hyperion Shape with Charged Surface Technology for a perfect blend of pop and power.",
                "content": "The JOOLA Ben Johns Hyperion C2 Pickleball Paddle represents the cutting edge of pickleball technology, designed in collaboration with the sport's top-ranked player. This paddle features the innovative Aero-Curve Hyperion shape and Charged Surface Technology, providing exceptional power without sacrificing control. During our testing, the paddle's balanced design allowed for precise shot placement while still generating impressive power on serves and groundstrokes. The carbon fiber construction offers excellent durability while maintaining a comfortable weight. The elongated handle accommodates various grip styles, and the paddle's responsive feel provides immediate feedback on contact. While the premium price point may deter casual players, serious competitors will appreciate the performance advantages this paddle delivers.",
                "image_url": "https://joolausa.com/cdn/shop/files/C2-Standard-Web1_2000x.png",
                "gallery": [
                    "https://joolausa.com/cdn/shop/files/C2-Standard-Web1_2000x.png",
                    "https://joolausa.com/cdn/shop/files/C2-Standard-Web2_2000x.png",
                    "https://joolausa.com/cdn/shop/files/C2-Standard-Web3_2000x.png",
                    "https://joolausa.com/cdn/shop/files/C2-Standard-Web4_2000x.png"
                ],
                "pros": [
                    "Innovative Aero-Curve Hyperion shape",
                    "Charged Surface Technology for superior spin",
                    "Excellent balance of power and control",
                    "Endorsed by top-ranked player Ben Johns"
                ],
                "cons": [
                    "High price point",
                    "May be too advanced for recreational players",
                    "Requires adjustment period for players switching from standard paddles"
                ],
                "specs": {
                    "Weight": "8.0-8.4 oz",
                    "Grip Size": "4 1/4 inches",
                    "Surface": "Carbon Fiber with Charged Surface Technology",
                    "Core": "Polypropylene Honeycomb",
                    "Handle Length": "5.5 inches"
                },
                "affiliate_links": {
                    "amazon": "https://www.amazon.com/JOOLA-Hyperion-Pickleball-Paddle-Hyperion/dp/B0BVHQDKMY",
                    "official_store": "https://joolausa.com/ben-johns-hyperion-c2-pickleball-paddle/"
                }
            },
            {
                "id": 3,
                "title": "Dura Fast 40 Outdoor Pickleball - 6 Pack",
                "brand": "Dura",
                "category": "balls",
                "price": 19.00,
                "rating": 4.4,
                "release_date": "2022-11-10",
                "summary": "The Dura Fast 40 is the official tournament ball for many competitions, offering consistent performance and durability for outdoor play.",
                "content": "The Dura Fast 40 outdoor pickleballs are the gold standard for tournament play, approved by the USA Pickleball Association and used in numerous professional tournaments. These balls feature 40 precise holes and are designed to withstand the rigors of outdoor play on rough court surfaces. They're the official ball of the US Open Pickleball Championships and the USAPA Pickleball National Championships. During testing, we found they maintain consistent flight patterns even in windy conditions and offer excellent visibility with their bright neon color. The rotationally molded one-piece construction with precisely drilled holes ensures consistent flight and bounce, specifically engineered for outdoor and hard-court play.",
                "image_url": "https://durafast40.com/cdn/shop/products/FrontandBackofDuraFast40Box6-Pack_1800x1800.jpg",
                "gallery": [
                    "https://durafast40.com/cdn/shop/products/FrontandBackofDuraFast40Box6-Pack_1800x1800.jpg",
                    "https://durafast40.com/cdn/shop/products/IMG_5523_900x.png",
                    "https://durafast40.com/cdn/shop/products/IMG_6267_900x.png"
                ],
                "pros": [
                    "Official tournament ball for many competitions",
                    "Excellent wind resistance and visibility",
                    "Consistent bounce and flight",
                    "Superior durability for outdoor courts"
                ],
                "cons": [
                    "Premium price compared to recreational balls",
                    "Requires break-in period",
                    "Ball life depends on court surface and play conditions"
                ],
                "specs": {
                    "Diameter": "2.94 inches",
                    "Weight": "0.06 lbs",
                    "Holes": "40",
                    "Material": "Rotationally molded plastic",
                    "Pack Size": "6 balls"
                },
                "affiliate_links": {
                    "amazon": "https://www.amazon.com/Pickleballs-Pickleball-Approved-Sanctioned-Tournament/dp/B0CGW1N92G",
                    "official_store": "https://durafast40.com/products/dura-fast-40-outdoor-pickleballs"
                }
            },
            {
                "id": 4,
                "title": "Franklin Sports X-40 Outdoor Pickleballs - 12 Pack",
                "brand": "Franklin",
                "category": "balls",
                "price": 24.99,
                "rating": 4.7,
                "release_date": "2023-01-15",
                "summary": "The Franklin X-40 Performance pickleballs are the official ball of USA Pickleball, APP Tour, and Pickleball US Open, delivering consistency and durability.",
                "content": "Franklin X-40 Outdoor Pickleballs represent the gold standard for competitive pickleball play, earning official status with USA Pickleball, the APP Tour, and the Pickleball US Open. These high-performance balls feature precision-drilled holes and seamless construction that delivers remarkable consistency in flight and bounce. During our extensive testing across various court surfaces, the X-40 demonstrated excellent visibility with its bright yellow color and maintained reliable performance even in challenging wind conditions. The balls provide a satisfying feel on impact and generate a distinctive sound that many players prefer. With superior durability compared to typical recreational balls, the Franklin X-40 offers excellent value for serious players looking for tournament-quality performance.",
                "image_url": "https://franklinsports.com/cdn/shop/files/20240312_Franklin_Web_Pickleball_Balls_90_1800x1800.jpg",
                "gallery": [
                    "https://franklinsports.com/cdn/shop/files/20240312_Franklin_Web_Pickleball_Balls_90_1800x1800.jpg",
                    "https://franklinsports.com/cdn/shop/files/20240312_Franklin_Web_Pickleball_Balls_95_1800x1800.jpg",
                    "https://franklinsports.com/cdn/shop/files/20240312_Franklin_Web_Pickleball_Balls_97_1800x1800.jpg",
                    "https://franklinsports.com/cdn/shop/files/20240312_Franklin_Web_Pickleball_Balls_89_1800x1800.jpg"
                ],
                "pros": [
                    "Official ball of USA Pickleball, APP Tour and US Open",
                    "Bright yellow color for excellent visibility",
                    "Consistent bounce and flight patterns",
                    "Durable construction for extended play"
                ],
                "cons": [
                    "Premium price compared to basic balls",
                    "May crack in extremely cold conditions",
                    "Optimized for outdoor play, not ideal for indoors"
                ],
                "specs": {
                    "Diameter": "74mm",
                    "Weight": "0.9 oz",
                    "Holes": "40",
                    "Material": "Durable plastic",
                    "Pack Size": "12 balls"
                },
                "affiliate_links": {
                    "amazon": "https://www.amazon.com/Franklin-Sports-X-40-Outdoor-Pickleballs/dp/B07VYVS5M2",
                    "official_store": "https://franklinsports.com/x-40-performance-pickleballs"
                }
            },
            {
                "id": 5,
                "title": "Selkirk SLK Halo Power XL Pickleball Paddle",
                "brand": "Selkirk",
                "category": "paddles",
                "price": 249.99,
                "rating": 4.8,
                "release_date": "2023-08-05",
                "summary": "The Selkirk SLK Halo Power XL offers exceptional reach and power with its elongated design and carbon fiber construction.",
                "content": "The Selkirk SLK Halo Power XL represents the pinnacle of paddle technology for players seeking maximum reach and power. This elongated paddle features Selkirk's premium carbon fiber facing and advanced core technology that delivers exceptional power while maintaining surprising control. During our testing, the extended reach provided a significant advantage for players with two-handed backhands and those who prefer to play from the baseline. Despite its larger size, the paddle maintains excellent maneuverability at the net for quick exchanges. The textured surface generates impressive spin potential, particularly on serves and passing shots. While the premium price point places it in the high-end category, the performance benefits make it a worthwhile investment for serious players looking to elevate their game.",
                "image_url": "https://www.selkirk.com/cdn/shop/files/SLK-HALO-Power-XL-Purple_900x.png",
                "gallery": [
                    "https://www.selkirk.com/cdn/shop/files/SLK-HALO-Power-XL-Purple_900x.png",
                    "https://www.selkirk.com/cdn/shop/files/SLK-HALO-Power-XL-Purple-Edge_900x.png",
                    "https://www.selkirk.com/cdn/shop/files/SLK-HALO-Power-XL-Purple-Handle_900x.png",
                    "https://www.selkirk.com/cdn/shop/files/SLK-HALO-Power-XL-Purple-Face_900x.png"
                ],
                "pros": [
                    "Extended reach with elongated design",
                    "Exceptional power without sacrificing control",
                    "Premium carbon fiber construction",
                    "Superior spin generation from textured surface"
                ],
                "cons": [
                    "High premium price point",
                    "Elongated design takes adjustment for some players",
                    "Slightly heavier than standard models"
                ],
                "specs": {
                    "Weight": "8.0-8.4 oz",
                    "Grip Size": "4 1/4 inches",
                    "Surface": "Carbon Fiber",
                    "Core": "Polymer Honeycomb",
                    "Handle Length": "5.25 inches"
                },
                "affiliate_links": {
                    "amazon": "https://www.amazon.com/Selkirk-Sport-Pickleball-Paddle-Control/dp/B0CF9NFMB8",
                    "official_store": "https://www.selkirk.com/products/slk-halo-power-xl"
                }
            },
            {
                "id": 6,
                "title": "Franklin Sports Pickleball Sling Bag",
                "brand": "Franklin",
                "category": "bags",
                "price": 33.49,
                "rating": 4.6,
                "release_date": "2023-04-10",
                "summary": "The Franklin Sports Pickleball Sling Bag offers convenient storage for all your pickleball gear with dedicated compartments for paddles, balls, and accessories.",
                "content": "The Franklin Sports Pickleball Sling Bag provides an excellent balance of functionality, convenience, and affordability for pickleball enthusiasts. This well-designed bag features a spacious main compartment that easily accommodates multiple paddles, a separate ventilated pocket for shoes or sweaty gear, and additional compartments for balls, water bottles, and personal items. The padded shoulder strap distributes weight comfortably for easy transport, while the compact profile keeps the bag from being bulky or cumbersome. Available in multiple color options, the bag's durable construction withstood our durability testing with no signs of wear at stress points. For players seeking a practical, reasonably priced gear solution, the Franklin Sling Bag delivers exceptional value.",
                "image_url": "https://franklinsports.com/cdn/shop/products/FS_PICKLEBALL-BAG-SLING-BLACK-FRONT-PRODUCT_2000x2000.jpg",
                "gallery": [
                    "https://franklinsports.com/cdn/shop/products/FS_PICKLEBALL-BAG-SLING-BLACK-FRONT-PRODUCT_2000x2000.jpg",
                    "https://franklinsports.com/cdn/shop/products/FS_PICKLEBALL-BAG-SLING-BLACK-FRONT-OPEN-PRODUCT_2000x2000.jpg",
                    "https://franklinsports.com/cdn/shop/products/FS_PICKLEBALL-BAG-SLING-BLACK-BACK-PRODUCT_2000x2000.jpg",
                    "https://franklinsports.com/cdn/shop/products/FS_PICKLEBALL-BAG-SLING-BLACK-LIFESTYLE-PRODUCT_2000x2000.jpg"
                ],
                "pros": [
                    "Excellent organization with multiple compartments",
                    "Comfortable padded shoulder strap",
                    "Ventilated pocket for shoes or sweaty gear",
                    "Multiple color options available"
                ],
                "cons": [
                    "Limited capacity compared to larger tournament bags",
                    "Sling design may not suit all players",
                    "No specialized water bottle holder"
                ],
                "specs": {
                    "Dimensions": "19\"L x 13\"W x 6\"H",
                    "Weight": "1.2 lbs (empty)",
                    "Material": "Durable nylon with reinforced stitching",
                    "Paddle Capacity": "2-3",
                    "Warranty": "1 year"
                },
                "affiliate_links": {
                    "amazon": "https://www.amazon.com/Franklin-Sports-Pickleball-Equipment-Accessories/dp/B0BKR3XG7N",
                    "official_store": "https://franklinsports.com/pickleball-sling-bag"
                }
            }
        ]
        
        return reviews
    except Exception as e:
        print(f"Error loading mock data: {e}")
        return []

# Global reviews variable
reviews = load_mock_data()

# Helper functions for working with review data
def get_all_reviews():
    """Return all reviews"""
    return reviews

def get_review_by_id(review_id):
    """Find and return a review by its ID"""
    return next((r for r in reviews if r.get('id') == review_id), None)

def get_filtered_reviews(category=None, brand=None, price_range=None, sort_by='newest'):
    """Filter and sort reviews based on criteria"""
    filtered_reviews = reviews.copy()
    
    # Apply filters
    if category:
        filtered_reviews = [r for r in filtered_reviews if r.get('category') == category]
    
    if brand:
        filtered_reviews = [r for r in filtered_reviews if r.get('brand') == brand]
    
    if price_range:
        if price_range == 'under50':
            filtered_reviews = [r for r in filtered_reviews if r.get('price', 0) < 50]
        elif price_range == '50to100':
            filtered_reviews = [r for r in filtered_reviews if 50 <= r.get('price', 0) < 100]
        elif price_range == 'over100':
            filtered_reviews = [r for r in filtered_reviews if r.get('price', 0) >= 100]
    
    # Sort reviews
    if sort_by == 'newest':
        filtered_reviews = sorted(filtered_reviews, key=lambda x: x.get('release_date', '2000-01-01'), reverse=True)
    elif sort_by == 'highest_rating':
        filtered_reviews = sorted(filtered_reviews, key=lambda x: x.get('rating', 0), reverse=True)
    elif sort_by == 'lowest_price':
        filtered_reviews = sorted(filtered_reviews, key=lambda x: x.get('price', 0))
    elif sort_by == 'highest_price':
        filtered_reviews = sorted(filtered_reviews, key=lambda x: x.get('price', 0), reverse=True)
    
    return filtered_reviews

def get_related_reviews(review_id, limit=3):
    """Get related reviews based on the same category and/or brand"""
    current_review = get_review_by_id(review_id)
    if not current_review:
        return []
    
    # Get reviews in the same category or by the same brand, excluding the current review
    related = [r for r in reviews if (r.get('category') == current_review.get('category') or
                                      r.get('brand') == current_review.get('brand')) and
                                      r.get('id') != review_id]
    
    # Sort by rating (highest first) and take the limited number of related reviews
    related_sorted = sorted(related, key=lambda x: x.get('rating', 0), reverse=True)
    return related_sorted[:limit]

def get_unique_brands():
    """Return a list of unique brands in the reviews data"""
    return sorted(list(set(r.get('brand') for r in reviews)))

def get_unique_categories():
    """Return a list of unique categories in the reviews data"""
    return sorted(list(set(r.get('category') for r in reviews)))

def prepare_review_data(review):
    """Prepare a review object for display by adding extra useful data"""
    if not review:
        return None
        
    # Clone the review to avoid modifying the original
    prepared = review.copy()
    
    # Add days since release (could be used for "New" badges etc.)
    from datetime import datetime
    release_date = datetime.strptime(review.get('release_date', '2000-01-01'), '%Y-%m-%d')
    today = datetime.now()
    prepared['days_since_release'] = (today - release_date).days
    
    return prepared 