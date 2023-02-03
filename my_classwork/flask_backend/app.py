# app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template(
        "jinja_intro.html",
        name="Minnie Tonka", template_name="Jinja2"
        )
# render_template is a built in function that takes the name of a file to load up & send to the user

# it also works with the Jinja engine where it first checks for Jinja code, variable interpolation, etc... before it sends back the html template

# as soon as it has Jinja code, the html template is no longer a static document
