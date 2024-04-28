#!/usr/bin/python3
"""Flask server (variable app)
"""


from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from os import getenv
from api.v1.views import app_views


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://0.0.0.0"}})  # Allow CORS for all origins on 0.0.0.0
app.register_blueprint(app_views)
app.url_map.strict_slashes = False

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


@app.teardown_appcontext
def downtear(self):
    '''Status of your API'''
    storage.close()


@app.errorhandler(404)
def error_not_found(error):
    '''To return not found error'''
    response = {"error": "Not found"}
    return (jsonify(response), 404)

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
