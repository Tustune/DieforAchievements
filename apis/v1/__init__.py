from flask import Blueprint
from flask_cors import CORS

api_v1 = Blueprint('api_v1', __name__)

# Set cross origin resource sharing, 跨域
CORS(api_v1)

from apis.v1 import resources