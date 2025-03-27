from flask import Blueprint

blueprint_demo = Blueprint('blueprint_demo', __name__, url_prefix='/user')

@blueprint_demo.route("/<username>")
def user(username):
    return f"Hello, {username}!"
