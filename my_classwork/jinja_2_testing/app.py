from flask import Flask, render_template


app = Flask(__name__)


# writing our own tests
# this one passes in a value, gets the square root & asks if an int
def square(value):
    return (value ** 0.5).is_integer()


# app.jinja_env.tests["square"] = square
# then you put it in the jinja env & makes it avail in every template

@app.route("/")
def todo():
    return render_template("fizzbuzz.html")
