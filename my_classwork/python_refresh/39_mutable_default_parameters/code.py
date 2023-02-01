"""Python refresher course - Mutable Default Parameters Section"""

from typing import List, Optional

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None): # List[int] = [] <--this is bad! 
        self.name = name
        self.grades = grades or [] # <--or [] was added

    def take_exam(self, result: int):
          self.grades.append(result)


bob = Student("Bob")
raj = Student("Raj")
kit = Student("Kit", [95, 100]) # this however, will give you kit's grades when called on line 21
bob.take_exam(90)
print(bob.grades) # 90
print(raj.grades) # 90 even though he didn't take a test!!!
# ^^^ and in re: to line 6, grades are set to a list with a default value but self.grades is referring to the SAME default list when the function was created. Essentially, they are sharing the same grades.
print(kit.grades)
