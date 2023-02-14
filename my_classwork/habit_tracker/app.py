import datetime
from flask import Flask, render_template, request


app = Flask(__name__)
habits = ["Test habit"]


# func using list comp to get starting/current date & to get dates 3 days before & after
# timedelta is adding 3 or subtracting 3 days from the starting/current date
@app.context_processor
def add_calc_date_range():
    def date_range(start: datetime.date):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3,4)]
        return dates

    return {"date_range": date_range}

@app.route("/")
def index():
    date_str =request.args.get("date")
    if date_str:
        selected_date = datetime.date.fromisoformat(date_str)
    else:
        selected_date = datetime.date.today()

    return render_template(
        "index.html", 
        habits = habits,
        title="Habit Tracker - Home",
        selected_date=selected_date
        )


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habit = request.form.get("habit") # <--getting habit user input
        habits.append(habit) # <--appending to the list
    return render_template(
        "add_habit.html", 
        title="Habit Tracker - Add Habit", 
        selected_date=datetime.date.today()
    )
