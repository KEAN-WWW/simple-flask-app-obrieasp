from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello CPS3500!</h1>"

@app.route("/new_page")
def new_page():
    return "<h1>This is a New Page!</h1>"

@app.route("/user/<username>")
def user(username):
    return render_template("user.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)
