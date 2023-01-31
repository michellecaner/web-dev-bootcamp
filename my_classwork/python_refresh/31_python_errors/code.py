"""Python refresher course - Type Hinting in Python Errors Section"""

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.") # built in error type - there are lots!

    return dividend / divisor

# divide(15, 0) # gives us our traceback error that helps up locate bugs

students = [
  {"name": "Pam", "grades": [75, 90]},
  {"name": "Kip", "grades": [65, 70]},
  {"name": "Val", "grades": [100, 100]}
]

print("Welcome to the Average Grades Program")
try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError as e:
    print(f"ERROR: {name} has no grades!") # you can have multiple except clauses
else:
    print("All student averages calculated.")
finally:
    print("Ya done!")

# the try / except block helps us handle and communicate errors on the back and front end until it gets a correct answer via the else statement or hits the final statement