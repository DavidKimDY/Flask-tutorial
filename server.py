from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Hello, World!</p>"


@app.route("/you/")
def you():
    return "<p>Hello, You!</p>"


app.run(debug=True, port=5002, host="0.0.0.0")
