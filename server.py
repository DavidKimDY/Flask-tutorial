from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Hello, World!</p>"


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == "dy" and request.form["password"] == "1234":
            return "Login success"
    return render_template("login.html")


app.run(debug=True, port=5002, host="0.0.0.0")
