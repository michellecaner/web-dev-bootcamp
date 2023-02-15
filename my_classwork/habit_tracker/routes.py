import datetime
import uuid
from flask import Blueprint, current_app, render_template, request, url_for, redirect


pages = Blueprint(
    "habits", __name__, template_folder="templates", static_folder="static"
    )


# func using list comp to get starting/current date & to get dates 3 days before & after
# timedelta is adding 3 or subtracting 3 days from the starting/current date
@pages.context_processor
def add_calc_date_range():
    def date_range(start: datetime.datetime):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3,4)]
        return dates

    return {"date_range": date_range}


def today_at_midnight():
    today = datetime.datetime.today()
    return datetime.datetime(today.year, today.month, today.day)


@pages.route("/")
def index():
    date_str =request.args.get("date")
    if date_str:
        selected_date = datetime.datetime.fromisoformat(date_str)
    else:
        selected_date = today_at_midnight()

    habits_on_date = current_app.db.habits.find({"added": {"$lte": selected_date}})

    completions =  [
        habit["habit"]
        for habit in current_app.db.completions.find({"date": selected_date})
    ]

    return render_template(
        "index.html", 
        habits = habits_on_date,
        selected_date=selected_date,
        completions=completions,
        title="Habit Tracker - Home"
        )


@pages.route("/add", methods=["GET", "POST"])
def add_habit():
    today = today_at_midnight()

    if request.form:
      current_app.db.habits.insert_one(
          {"_id": uuid.uuid4().hex, "added": today, "name": request.form.get("habit")}
      )

    return render_template(
        "add_habit.html", 
        title="Habit Tracker - Add Habit",
        selected_date=today
    )
    
    
# new flask feature
# instead of @app.route("/complete", methods=["POST"])
# need to make a place for that completed habit data to go
# @app.post("/complete")
@pages.route("/complete", methods=["POST"])
def complete():
    date_string = request.form.get("date") # <--db key
    habit = request.form.get("habitId") # <--db key
    date = datetime.datetime.fromisoformat(date_string)
    current_app.db.completions.insert_one({"date": date, "habit": habit})

    return redirect(url_for(".index", date=date_string))