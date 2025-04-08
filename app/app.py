from flask import Flask, render_template, request

app = Flask(__name__)

valid_users = ["jack", "jill", "alice"]

@app.route("/")
def home():
    return "Welcome to the homepage"

@app.route("/user/<username>")
def greet_user(username):
    if username.lower() == "none":
        return "No user provided", 400

    if username.lower() in valid_users:
        return render_template("user.html", username=username)
    else:
        return "Invalid user", 403

@app.route("/new")
def new_page():
    return render_template("user.html", new_page=True)
