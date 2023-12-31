from app.routes.status import status
from app.routes.sentiment import *


def define_routes(app):
    app.register_blueprint(status, url_prefix='/status/')
    app.register_blueprint(sentiment, url_prefix='/sentiment/')