# app/app.py
from flask import Flask, render_template, abort

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def main_page():
    """Main page route"""
    return "<h1>Welcome to the Main Page!</h1>"

@app.route('/new')
def new_page():
    """Route for the new page"""
    return "<h1>New Page</h1>"

@app.route('/user/<username>')
def user_page(username):
    """Route for a valid user"""
    # For now, simulate the validation
    valid_users = ['jack', 'john', 'jane']
    if username not in valid_users:
        abort(404)  # Return 404 if the user is not valid
    return f"<h1>Hello, {username}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
