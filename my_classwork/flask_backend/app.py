# app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("first_page.html")
# render_template is a built in function that takes the name of a file to load up & send to the user


@app.route("/second")
def hello_world_fancy():
    return render_template("second_page.html")
