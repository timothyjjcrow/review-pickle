import os
from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

# Sample review data for demonstration
SAMPLE_REVIEWS = [
    {
        "id": 1,
        "title": "Selkirk AMPED Epic Paddle",
        "brand": "Selkirk",
        "category": "paddles",
        "summary": "The ultimate power paddle with premium materials and exceptional control.",
        "content": """<p>The Selkirk AMPED Epic Paddle represents the pinnacle of paddle engineering, combining cutting-edge materials with thoughtful design to create a truly exceptional playing experience.</p>
        <p>Featuring Selkirk's proprietary X5 polypropylene core and FiberFlex fiberglass face, the AMPED Epic delivers impressive power without sacrificing touch. The slightly elongated shape provides an extended reach while maintaining excellent maneuverability.</p>
        <p>During our testing, the paddle performed exceptionally well in all areas. The sweet spot is generous, allowing for consistent power even on off-center hits. The edge guard is well-designed, minimizing mishits without adding unnecessary weight.</p>
        <p>The handle design deserves special mention, with its comfortable grip and perfect balance point that reduces fatigue during extended play sessions. The vibration dampening is also noteworthy, protecting players' elbows and wrists during hard-hitting exchanges.</p>""",
        "pros": [
            "Excellent power-to-control ratio",
            "Premium materials and construction",
            "Comfortable grip reduces fatigue",
            "Large sweet spot for consistent performance",
            "Vibration dampening technology"
        ],
        "cons": [
            "Premium price point",
            "Might be too powerful for beginners",
            "Slightly heavier than some competing models"
        ],
        "specifications": {
            "weight": "7.9-8.3 oz",
            "paddle face": "FiberFlex Fiberglass",
            "core": "X5 Polypropylene Honeycomb Core",
            "grip size": "4 1/4\"",
            "grip type": "ComfortGrip",
            "shape": "Elongated"
        },
        "rating": 4.9,
        "category_ratings": {
            "power": 9.5,
            "control": 9.2,
            "touch": 9.0,
            "durability": 9.3,
            "comfort": 9.4
        },
        "price": 169.99,
        "image_url": "https://placehold.co/800x600/a5d6a7/ffffff?text=Selkirk+AMPED+Epic",
        "published_date": datetime(2023, 10, 15),
        "affiliate_links": [
            {"retailer": "Amazon", "url": "https://amazon.com"},
            {"retailer": "PickleballCentral", "url": "https://pickleballcentral.com"},
            {"retailer": "DSG", "url": "https://dickssportinggoods.com"}
        ],
        "testing_process": "We tested this paddle with 12 players of varying skill levels over a period of 4 weeks in both indoor and outdoor environments. Testing included drills, match play, and specific skill assessments.",
        "verdict": "The Selkirk AMPED Epic is one of the best paddles on the market today. While it comes with a premium price tag, the exceptional performance, quality construction, and comfort make it a worthwhile investment for serious players."
    },
    {
        "id": 2,
        "title": "K-Swiss Express Light 2 Pickleball Shoes",
        "brand": "K-Swiss",
        "category": "shoes",
        "summary": "Lightweight court shoes designed specifically for pickleball players who value agility and comfort.",
        "content": """<p>K-Swiss has established itself as a leader in pickleball footwear, and the Express Light 2 reinforces that reputation. These shoes are engineered specifically for the unique movements and demands of pickleball.</p>
        <p>The standout feature is the weight - at just 11.2 oz (men's size 10), these are among the lightest court shoes available without compromising stability or durability. The Surge 7.0 midsole provides excellent energy return, helping players move quickly around the court without fatigue.</p>
        <p>Durability has been significantly improved over the original Express Light model, with added reinforcement in high-wear areas. The herringbone outsole pattern delivers exceptional traction on both indoor and outdoor courts, with minimal squeaking on indoor surfaces.</p>
        <p>The breathable mesh upper keeps feet cool during intense matches, while the padded collar and tongue enhance comfort. The shoes required minimal break-in time, feeling comfortable right out of the box.</p>""",
        "pros": [
            "Extremely lightweight design",
            "Excellent court grip and traction",
            "Durable reinforced construction",
            "Good breathability",
            "Quick break-in period"
        ],
        "cons": [
            "Limited color options",
            "Runs slightly narrow for wide feet",
            "Not as much ankle support as heavier models"
        ],
        "specifications": {
            "weight": "11.2 oz (men's size 10)",
            "upper": "Breathable mesh with synthetic overlays",
            "midsole": "Surge 7.0 cushioning",
            "outsole": "Aösta 7.0 rubber with herringbone pattern",
            "heel drop": "6mm"
        },
        "rating": 4.7,
        "category_ratings": {
            "comfort": 9.3,
            "traction": 9.5,
            "durability": 9.0,
            "weight": 9.8,
            "support": 8.7
        },
        "price": 124.99,
        "image_url": "https://placehold.co/800x600/a5d6a7/ffffff?text=K-Swiss+Express+Light+2",
        "published_date": datetime(2023, 9, 22),
        "affiliate_links": [
            {"retailer": "Amazon", "url": "https://amazon.com"},
            {"retailer": "DSG", "url": "https://dickssportinggoods.com"}
        ],
        "testing_process": "We had 8 testers wear these shoes for a minimum of 15 hours each on indoor and outdoor courts. We evaluated comfort, traction, support, and durability under various playing conditions.",
        "verdict": "The K-Swiss Express Light 2 is an excellent choice for pickleball players seeking a lightweight, responsive shoe. While they may not offer enough support for players with ankle concerns, they excel in quickness and comfort, making them ideal for agile players who prioritize speed."
    },
    {
        "id": 3,
        "title": "Dura Fast 40 Outdoor Pickleballs",
        "brand": "Dura",
        "category": "balls",
        "summary": "Tournament-approved pickleballs with excellent durability and consistent bounce for outdoor play.",
        "content": """<p>Dura Fast 40 balls have long been considered the standard for outdoor pickleball, and our testing confirms their continued excellence. These USAPA-approved balls deliver remarkable consistency in both bounce and flight.</p>
        <p>The 40-hole design strikes an ideal balance between speed and control, with the balls performing predictably even in windy conditions. The durability is impressive - during our testing, a single ball lasted through approximately 6-8 hours of continuous play before showing signs of wear.</p>
        <p>The bright yellow color provides excellent visibility against most court surfaces, though some players might prefer the optional neon green for certain lighting conditions. The balls maintain their round shape exceptionally well, even after heavy use.</p>
        <p>One minor drawback is that these balls require a short break-in period, feeling slightly stiff when first used. However, after 10-15 minutes of play, they reach optimal performance and maintain it consistently thereafter.</p>""",
        "pros": [
            "Excellent durability",
            "Consistent bounce and flight",
            "USAPA tournament approved",
            "Good visibility",
            "Performs well in wind"
        ],
        "cons": [
            "Requires short break-in period",
            "Slightly more expensive than some competitors",
            "Limited color options"
        ],
        "specifications": {
            "material": "Rotomolded plastic",
            "diameter": "74mm",
            "holes": "40",
            "colors available": "Yellow, Neon Green",
            "quantity per pack": "3, 6, or 12"
        },
        "rating": 4.5,
        "category_ratings": {
            "durability": 9.5,
            "consistency": 9.3,
            "visibility": 8.9,
            "value": 8.5,
            "performance": 9.2
        },
        "price": 9.99,
        "image_url": "https://placehold.co/800x600/a5d6a7/ffffff?text=Dura+Fast+40",
        "published_date": datetime(2023, 11, 5),
        "affiliate_links": [
            {"retailer": "Amazon", "url": "https://amazon.com"},
            {"retailer": "PickleballCentral", "url": "https://pickleballcentral.com"}
        ],
        "testing_process": "We conducted extensive testing of these balls across multiple outdoor courts with 20+ players of various skill levels. Tests included consistency measurements, durability tracking, and player feedback on performance.",
        "verdict": "Dura Fast 40 Outdoor Pickleballs remain the gold standard for outdoor play. Their exceptional consistency and durability justify the slightly higher price point, making them an excellent choice for serious players and recreational enthusiasts alike."
    }
]

# Popular tags for sidebar
POPULAR_TAGS = ["beginner", "advanced", "lightweight", "power", "control", "budget", "premium", "durable", "tournament"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reviews')
def reviews_list():
    # Get filter parameters
    category = request.args.get('category')
    brand = request.args.get('brand')
    sort = request.args.get('sort', 'date')
    price_range = request.args.get('price_range')
    page = int(request.args.get('page', 1))
    
    # Filter reviews (basic filtering for demonstration)
    filtered_reviews = SAMPLE_REVIEWS.copy()
    
    if category:
        filtered_reviews = [r for r in filtered_reviews if r['category'] == category]
    
    if brand:
        filtered_reviews = [r for r in filtered_reviews if r['brand'].lower() == brand.lower()]
    
    if price_range:
        if price_range == 'under_50':
            filtered_reviews = [r for r in filtered_reviews if r['price'] < 50]
        elif price_range == '50_100':
            filtered_reviews = [r for r in filtered_reviews if 50 <= r['price'] < 100]
        elif price_range == '100_200':
            filtered_reviews = [r for r in filtered_reviews if 100 <= r['price'] < 200]
        elif price_range == 'over_200':
            filtered_reviews = [r for r in filtered_reviews if r['price'] >= 200]
    
    # Sort reviews
    if sort == 'rating_high':
        filtered_reviews.sort(key=lambda x: x['rating'], reverse=True)
    elif sort == 'price_low':
        filtered_reviews.sort(key=lambda x: x['price'])
    elif sort == 'price_high':
        filtered_reviews.sort(key=lambda x: x['price'], reverse=True)
    else:  # Default sort by date
        filtered_reviews.sort(key=lambda x: x['published_date'], reverse=True)
    
    # Simple pagination
    items_per_page = 6
    total_pages = (len(filtered_reviews) + items_per_page - 1) // items_per_page
    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    paginated_reviews = filtered_reviews[start_idx:end_idx]
    
    pagination = {
        'page': page,
        'pages': total_pages,
        'has_prev': page > 1,
        'has_next': page < total_pages
    }
    
    return render_template('reviews/list.html', reviews=paginated_reviews, pagination=pagination)

@app.route('/reviews/<int:review_id>')
def review_detail(review_id):
    # Find the requested review
    review = next((r for r in SAMPLE_REVIEWS if r['id'] == review_id), None)
    
    if not review:
        return render_template('404.html'), 404
    
    # Get related reviews (simple implementation - same category but different ID)
    related_reviews = [r for r in SAMPLE_REVIEWS if r['category'] == review['category'] and r['id'] != review_id]
    
    return render_template('reviews/detail.html', review=review, related_reviews=related_reviews, popular_tags=POPULAR_TAGS)

@app.route('/api/reviews/<int:review_id>')
def api_review_detail(review_id):
    # Find the requested review
    review = next((r for r in SAMPLE_REVIEWS if r['id'] == review_id), None)
    
    if not review:
        return jsonify({"error": "Review not found"}), 404
    
    # Convert datetime to string for JSON serialization
    review_copy = {**review}
    review_copy['published_date'] = review_copy['published_date'].strftime('%Y-%m-%d')
    
    return jsonify(review_copy)

@app.route('/api/reviews')
def api_reviews_list():
    # Convert datetime to string for JSON serialization
    reviews_copy = []
    for review in SAMPLE_REVIEWS:
        review_copy = {**review}
        review_copy['published_date'] = review_copy['published_date'].strftime('%Y-%m-%d')
        reviews_copy.append(review_copy)
    
    return jsonify({"results": reviews_copy})

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000) 