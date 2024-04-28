#!/usr/bin/python3
'''api status'''
import models
from models import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views
from models import State


@app_views.route('/status', strict_slashes=False)
def returnstuff():
    '''return stuff'''
    return jsonify(status='OK')


@app_views.route('/stats', strict_slashes=False)
def stuff():
    '''JSON Responses'''
    todos = {
            "states": storage.count("State"),
            "cities": storage.count("City"),
            "amenities": storage.count("Amenity"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            }
    return jsonify(todos)
