from flask import Flask, render_template

app = Flask(__name__)

# values below are for variables titled: text & completed 
todos = [
    ("Get milk", False),
    ("Learn code", True),
    ("Wash dog", True),
    ("Cook dinner", False),
    ("Feed cat", False)
]

@app.route("/")
def todo():
    return render_template("home.html", todos=todos)


# for a specific todo that takes in the todo string as a part of the url
# then it goes through the todos
# if the text matches one of the todos in the list, then it will calc completed or not
# then it will create a title for the page
# then it renders the template with the passed in arguments
# and if not found, then directed to not found page
@app.route("/<string:todo>")
def todo_item(todo: str):
    for text, completed in todos:
        if text == todo:
            completed_text = "[x]" if completed else "[]"
            title = f"{completed_text} - Todos"
            return render_template("todo.html", text=text, completed=completed, title=title)
    else:
        return render_template("not-found.html", text=todo, title="Not found")
