"""Python refresher course - Destructuring Variables Section"""

student_attendance = {"Jen": 85, "Joe": 90, "Bud": 95}

print(list(student_attendance.items())) # this unpacks the dictionary and prints a LIST of the tuples



for student, attendance in student_attendance.items(): # student & attendance are just two variables
    print(f"{student}: {attendance}") # the variables are assigned to the key & the value



# if you want to print out each tuple similar to the code above, use a for loop
for t in student_attendance.items(): # <--gotta unpack with .items()
    print(t)



# a list full of tuples
people = [
    ("Jen", 46, "Engineer"),
    ("Joe", 32, "Chef"),
    ("Bud", 56, "Pilot")
]

for name, age, profession in people: #assigning variables to elements - 3 for 3 or you'll get an error
    print(f"Name: {name}, Age: {age}, Profession: {profession}") #prints out a nice list
    
    

# alternatively, you can do something like this 
people = [
    ("Si", 39, "Driver"),
    ("Bea", 39, "Dancer"),
    ("Dan", 43, "Artist")
]

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}") #this is trippy
    
# prints out:
# Name: Si, Age: 39, Profession: Driver
# Name: Bea, Age: 39, Profession: Dancer
# Name: Dan, Age: 43, Profession: Artist


# what if you DON'T want to access an element??
person = ("Michelle", 42, "Engineer")
name, _, profession = person  # the underscore by itself will be assigned to the element you want to skip

print(name, profession) # Michelle Engineer


# separate a list into two from the 1st element and the rest of the elements
head, *tail = [1, 2, 3, 4, 5] # the 'head' is the 1st value & * collects the remaining values

print(head) # prints the 1st element
print(tail) # prints a list of the remaining elements
