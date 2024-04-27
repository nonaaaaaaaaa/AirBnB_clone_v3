# api/v1/views/index.py
from flask import jsonify
from . import app_views

# Define the route for the /status endpoint
@app_views.route('/status', methods=['GET'])
def get_status():
    """Return a JSON response with status OK."""
    return jsonify({"status": "OK"})
