#!/usr/bin/python3
from flask import Blueprint

# Create a Blueprint object with the url prefix /api/v1
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import views to register them with the Blueprint
from api.v1.views.index import *

from api.v1.views.states import *

from api.v1.views.cities import *
