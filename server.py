from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
)
from flask_login import (
    UserMixin,
    current_user,
    LoginManager,
    login_user,
    login_required,
    logout_user,
)
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    def __init__(self, username, password):
        self.id = username
        self.username = username
        self.password = password

    @classmethod
    def get(cls, username):
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("select * from users where name = ?", [username])
            result = cur.fetchall()
            if result == []:
                return Nnoe
            else:
                username, password = result[0]
                return cls(username, password)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/only-login-user/")
@login_required
def only_login_user():
    return f"this is login user : {current_user.username}"


@app.route("/signout/")
@login_required
def signout():
    logout_user()
    return redirect(url_for("home"))


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
                user = User(username, password)
                login_user(user)
                return "Login success"
            else:
                return "Wrong password"
    return render_template("signin.html")


@app.route("/signup/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute(
                "insert into users (name, password) values (?, ?)",
                [username, password],
            )
    return render_template("signup.html")


app.run(debug=True, port=5002, host="0.0.0.0")
