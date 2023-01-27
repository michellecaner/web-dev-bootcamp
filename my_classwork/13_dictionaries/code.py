"""Python refresher course - Dictionaries Section"""

friend_ages = {"Allison": 34, "Duley": 46, "Kyle": 32}

# values in dictionaries are accessed via keys & bracket/subscript notation
print(friend_ages["Kyle"])



# to add to a dictionary
friend_ages["Chaneice"] = 28

print(friend_ages)



# to change as existing key
friend_ages["Chaneice"] = 29

print(friend_ages)



# putting dictionaries in lists
friends = [
    {"name": "Allison", "age": 34},
    {"name": "Duley", "age": 46},
    {"name": "Kyle", "age": 32}
]

print(friends)

print(friends[0]) #can access via index cause this is a LIST

print(friends[0]["name"]) # get that name baby



# using a for loop to iterate over a dictionary to access data
student_attendance = {"Ava": 96, "Di": 80, "Lea": 100}

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

# the print statement lists the student variable/key (in this case, the NAME) and by accessing the dictionary and the student variable key via bracket notation, you get the value printed. CRIKEY.



# an easier (ha) way to write the above is below - .items UNPACKS the dictionary (LIKE * ????)
student_attendance = {"Jen": 85, "Joe": 90, "Bud": 95}

for student, attendance in student_attendance.items(): # student & attendance are just two variables
    print(f"{student}: {attendance}") # the variables are assigned to the key & the value



# can also use 'in' with an if/else statement on dictionaries to check whether a value is one of the keys of a dictionary
student_attendance = {"Bo": 100, "Al": 75, "Ben": 90}

if "Bo" in student_attendance:
    print(f"Bo: {student_attendance['Bo']}") # single quotes cause ya used double already & the 'Bo' key gives you the VALUE
else:
    print("Bo is not in this class.")



# if you would want to get the total & average of student attendance, you can do something like this
student_attendance = {"Xi": 85, "Flo": 95, "Jim": 100}

attendance_values = student_attendance.values() # spits out a list of the values
print(sum(attendance_values) / len(attendance_values)) # takes the sum & divides by the length of the dict
