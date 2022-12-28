from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Hello, World!</p>"


@app.route("/you/")
def you():
    return "<p>Hello, You!</p>"


@app.route("/<name>/")
def name(name):
    return f"<p>Hello, {name}!</p>"


@app.route("/login/")
def login():
    return render_template("login.html")


app.run(debug=True, port=5002, host="0.0.0.0")
