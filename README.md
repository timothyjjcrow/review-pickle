# PicklePulse - Equipment Reviews Feature

This module handles the equipment reviews for pickleball gear with affiliate marketing integration on the PicklePulse website.

## Features

- Comprehensive, SEO-friendly equipment reviews
- Affiliate marketing integration
- Rich review content with images, pros/cons, and ratings
- Search and filtering capabilities using Elasticsearch

## Setup

1. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

2. Set up environment variables (copy .env.example to .env and update accordingly)

3. Run development server:
   ```
   python app/backend/app.py
   ```

## Project Structure

- `/app/backend` - Python backend code
- `/app/frontend` - Frontend HTML/JS code
- `/app/static` - Static assets (CSS, JS, images)
- `/app/templates` - HTML templates
- `/app/database` - Database models and migrations
- `/app/tests` - Test files

## Affiliate Marketing Integration

The system uses environment variables to manage affiliate links. Make sure the `.env` file contains the required affiliate tracking codes.

## Search Functionality

The review search is powered by Elasticsearch. Separate indexes are maintained for development and production environments.
