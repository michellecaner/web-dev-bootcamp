from flask import (
    Flask,
    session,
    render_template,
    request,
    abort,
    url_for,
    flash,
    redirect
)

app = Flask(__name__)
# Secret key generated with secrets.token_urlsafe()
app.secret_key = "lkaQT-kAb6aIvqWETVcCQ28F-j-rP_PSEaCDdTynkXA"

users = {}


@app.get("/")
def home():
    return render_template("home.html", email=session.get("email"))


@app.get("/protected")
def protected():
    if not session.get("email"):
        abort(401)
    return render_template("protected.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    email = ""

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if users.get(email) == password:
            session["email"] = email
            return redirect(url_for("protected"))
        flash("Incorrect email or password.")
    return render_template("login.html", email=email)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        users[email] = password
        flash("Successfully signed up.")
        return redirect(url_for("login"))

    return render_template("signup.html")
