from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/signin/", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute(
                "select * from users where name = ?", [request.form["username"]]
            )
            result = cur.fetchall()
            # result는 [(username, password)] 모양.
            # 만약 조건의 데이터가 없으면 []
            if result == []:
                return "There is No user"
            else:
                username, password = result[0]

            if password == request.form["password"]:
                return "Login success"
            else:
                return "Wrong password"
    return render_template("signin.html")


@app.route("/signup/", methods=["GET", "POST"])
def signup():

    return render_template("signup.html")


app.run(debug=True, port=5002, host="0.0.0.0")
