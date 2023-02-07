import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

# setting the end points/routes & their methods
# for the microblog, we can post new entries and get past entries on the homepage
# the request variable is a value that has something inside it whenever we're in a function that is currently responding to a request made by the browser & it's associated endpoint 
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        print(entry_content, formatted_date)
    return render_template("home.html")
  
  # if the request method is post, we can grab the entry content data
  # when the form submits, the data is added to a payload & sent with the request
  # then we can access that data with request.form.get()
  # "content" is the NAME of that field - set in HTML block
  # in flask, request.form is something that looks like a dictionary
  
  # datetime.datetime.today() accesses the datetime class of the datetime module  and gives us a datetime object that has today's date
  # .strftime("%Y-%m-%d") formats the datetime object into a string with the year, month & day as 2 digits each
  
  # next, the data has to be stored somewhere
  # then the data needs to be sent back to the template to be displayed in the browser
  
  