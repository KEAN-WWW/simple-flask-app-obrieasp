from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Home Page</h1>", 200

@app.route("/new")
def new_page():
    return "<h1>Welcome to the New Page!</h1>", 200

valid_users = {"jack": "Jack", "jill": "Jill"}
@app.route("/user/<username>")
def get_user(username):
    if username in valid_users:
        return f"<h1>Hello, {valid_users[username]}!</h1>", 200
    return "<h1>User not found</h1>", 404

if __name__ == "__main__":
    app.run(debug=True)
