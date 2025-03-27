from flask import Flask
from app.bp.blueprint_demo import blueprint_demo

def create_app():
    app = Flask(__name__)

    app.register_blueprint(blueprint_demo)

    @app.route("/")
    def home():
        return "<h1>Welcome to the Home Page</h1>", 200

    @app.route("/new")
    def new_page():
        return "<h1>Welcome to the New Page!</h1>", 200

    return app
