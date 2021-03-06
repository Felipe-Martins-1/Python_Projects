from flask import Flask
from .extensions import config_app, config_login
from .blueprints import database, authentication, admin, blog, api


def create_app():
    app = Flask(__name__)
    config_app.init_app(app)
    database.init_app(app)
    config_login.init_app(app)
    admin.init_app(app)
    app.register_blueprint(authentication.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(api.bp)
    return app
