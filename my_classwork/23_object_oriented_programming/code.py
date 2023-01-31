"""Python refresher course - Object Oriented Programming Section"""

student = {"name": "Bo", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"])) # average function, passing in student dict & accessing grades // 88.0

# because the average function has no real tie to the student dictionary but instead to sequence, let's shift our thinking when writing the code. In the real world, the student and their average would be related.

# print(student.average()) <-- can't quite do this though because we can't call methods on dictionaries?

# creating an instance of a student
class Student:
    def __init__(self, name, grades): # self is a given, but we can have more parameters like name & grades for reassigning
        self.name = name #accessing the name using dot notation
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)
  
student = Student("Peg", (100, 98, 88, 100, 90)) # creating an object that behaves as the class above defines

print(student.name)
print(student.grades)

# No. 1, call a class • No. 2, the init method runs • No. 3, access the properties
# If we want to find the grade average for the student, we can then put that method INSIDE the class & pass <self>

print(f"Peg's grade average is {student.average()}")
