# app.py
from flask import Flask, render_template

app = Flask(__name__)


class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


@app.route("/")
def hello_world():
    return render_template(
        "jinja_intro.html",
        name="Minnie Tonka", template_name="Jinja2"
        )
# render_template is a built in function that takes the name of a file to load up & send to the user

# it also works with the Jinja engine where it first checks for Jinja code, expressions, etc... before it sends back the html template to the user

# as soon as it has Jinja code, the html template is no longer a static document

# adding the / at the end of the route below as a safety catch - flask doesn't care either way
@app.route("/expressions/")
def render_expressions():

    # interpolation variables
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"

    # addition and subtraction variable
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    # string concatenation variable
    first_name = "Captain"
    last_name = "Marvel"

    # these were originally in the call of the render_template function, but because there are so many keyword args, we are assigning them to a dictionary named kwargs. When calling the render_template function, we will UNPACK that dictionary (**) and pass the data into html template expressions!
    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name
    }

    return render_template(
        "expressions.html", **kwargs)

    # color="brown" (now color=color) is a key/value pair - different from the variables even though they look similar!

@app.route("/data-structures/")
def render_data_structures():

    # list operations / accessed by index: movies[0]
    movies = [
        "Leon the Professional",
        "The Usual Suspects",
        "A Beautiful Mind"
    ]

    # dictionary operations / accessed by keys: car["brand"]
    car = {
        "brand": "Tesla",
        "model": "Roadster",
        "year": "2020"
    }

    # custom data structure operations / accessed by dot notation: moons.first
    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")

    kwargs = {
        "movies": movies,
        "car": car,
        "moons": moons,
    }

    return render_template("data_structures.html", **kwargs)


@app.route("/conditionals-basics/")
def render_conditionals():
    company = "Microsoft"

    return render_template("conditionals_basics.html", company=company)


# using our for loop to display an ul of planets
@app.route("/for-loop/")
def render_for_loops():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupyter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]
    return render_template("for_loops.html", planets=planets)


# using for loops WITH conditionals on a dictionary
@app.route("/for-loop/conditionals/")
def render_for_loops_conditionals():
    user_os = {
        "Bob Miller": "Windows",
        "Judy Lee": "MacOS",
        "Zach Ng": "Linux",
        "Regina George": "Windows"
    }
    return render_template("loops_and_conditionals.html", user_os=user_os)