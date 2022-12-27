from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Hello, World!</p>"


app.run(debug=True, port=5002, host="0.0.0.0")