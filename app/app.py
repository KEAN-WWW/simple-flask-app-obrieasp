from flask import Flask, jsonify

# Create the Flask app
app = Flask(__name__)

# Sample route for the main page
@app.route('/')
def home():
    return "<h1>Welcome to the Main Page</h1>"

# Route for the user page (valid user)
@app.route('/user/<username>')
def user(username):
    if username == "jack":
        return f"<h1>Hello {username}</h1>"  # Example valid user response
    else:
        return jsonify(error="User not found"), 404

# Route for the new page
@app.route('/new_page')
def new_page():
    return "<h1>New Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
