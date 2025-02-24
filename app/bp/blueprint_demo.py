from flask import Blueprint

# Define the blueprint
example_blueprint = Blueprint('example', __name__, url_prefix='/user')

# Define a route within the blueprint
@example_blueprint.route("/<username>")
def user(username):
    return f"Hello, {username}!"
