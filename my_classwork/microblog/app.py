import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
import certifi


app = Flask(__name__)
client = MongoClient("mongodb+srv://BBluth:Lucille143!@microblog-app.fy7jwwt.mongodb.net/test", tlsCAFile=certifi.where())
app.db = client.microblog
entries = []

# a temporary place to save our entries before we move over to a database
# since our data is simple, we are going to save the data in tuples
# for every form we receive, we're going to append a new tuple to the entries list that contains the content & the date


# setting the end points/routes & their methods
# for the microblog, we can post new entries and get past entries on the homepage
# the request variable is a value that has something inside it whenever we're in a function that is currently responding to a request made by the browser & it's associated endpoint
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((entry_content, formatted_date))
        app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

    entries_with_date = [
        (
            entry[0],
            entry[1],
            datetime.datetime.strptime(entry[1], "%Y-%m-%d").strftime("%b %d")
        )
        for entry in entries
    ]
    return render_template("home.html", entries=entries_with_date)

  # print(entry_content, formatted_date) <-- for testing
  # print([e for e in app.db.entries.find({})]) <-- for testing

  # if the request method is post, we can grab the entry content data
  # when the form submits, the data is added to a payload & sent with the request
  # then we can access that data with request.form.get()
  # "content" is the NAME of that field - set in HTML block
  # in flask, request.form is something that looks like a dictionary


  # datetime.datetime.today() accesses the datetime class of the datetime module and gives us a datetime object that has today's date
  # .strftime("%Y-%m-%d") formats the datetime object into a string with the year, month & day as 2 digits each
  # when reformatting, we tell Python which date we're talking about & then changes it into month & date
  # the for loop applies that logic to every entry in the entries list
  
  
  # next, the data has to be stored somewhere - for now an empty list
  # then the data needs to be sent back to the template to be displayed in the browser
  
  
  # using the reformated entries in our template --> entries=entries_with_date
  # entries=entries creates an entries variable in the template that will contain our list of tuples
  # then in the template, you make use of that {{ variable }}
  