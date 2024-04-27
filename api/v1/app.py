# api/v1/app.py
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

# Create a Flask application instance
app = Flask(__name__)

# Register the blueprint app_views to the Flask instance app
app.register_blueprint(app_views, url_prefix='/api/v1')

# Define a method to handle teardown_appcontext
@app.teardown_appcontext
def teardown_storage(exception):
    """Close the storage engine at the end of the request."""
    storage.close()

# Run the Flask server if this script is executed directly
if __name__ == "__main__":
    # Define host and port based on environment variables or defaults
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
