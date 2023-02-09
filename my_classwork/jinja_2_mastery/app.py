from flask import Flask, render_template

app = Flask(__name__)

# values below are for variables titled: text & completed 
todos = [
    ("Get milk", False),
    ("Learn code", True)
]

@app.route("/")
def todo():
    return render_template("home.html", todos=todos)
