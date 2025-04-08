""" Flask Methods """
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, CPS3500!"

@app.route("/new_page")
def newpage():
    return "This is the new page!"

@app.route("/user/<username>")
def user(username):
    return render_template("user.html", username=username)

if __name__ == "__main__":
    app.run(debug = True)