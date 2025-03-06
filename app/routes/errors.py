"""
Error handlers for the application.
"""
import traceback
from flask import Blueprint, render_template

errors_bp = Blueprint('errors', __name__)

@errors_bp.app_errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@errors_bp.app_errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    # Log the error for debugging
    print(f"500 error: {error}")
    traceback.print_exc()
    return render_template('404.html'), 500 