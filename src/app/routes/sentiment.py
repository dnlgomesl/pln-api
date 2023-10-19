from flask import Blueprint, request
from flask_cors import cross_origin
from app.util import METHOD_NOT_DEFINED
from app.controllers import sentiment as controller

sentiment = Blueprint('sentiment', __name__)

@sentiment.route("", methods=["POST"])
@cross_origin(supports_credentials=True)
def route_sentiment():
    if request.method == "POST":
        return controller.get_sentiment(request)
    
    return METHOD_NOT_DEFINED
