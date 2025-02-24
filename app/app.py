from flask import Flask
import sys
import os

# Ensure the app can find the bp package, add it to the sys.path
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app'))

from bp.blueprint_demo import example_blueprint  # Import the blueprint

app = Flask(__name__)

# Register the blueprint with the app
app.register_blueprint(example_blueprint, url_prefix='/bp')  # Adjust the url_prefix if needed

@app.route('/')
def main_page():
    return "<h1>Welcome to the Main Page</h1>"

@app.route('/user/<username>')
def user(username):
    if username == "jack":
        return f"Hello, {username}!"
    return "Anonymous"

# Define the /new_page route
@app.route('/new_page')
def new_page():
    return "<h1>New Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
