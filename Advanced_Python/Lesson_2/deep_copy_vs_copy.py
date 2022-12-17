# deepcopy() vs copy() in Python

import copy


# Problem

# Create a list
a = [1,2,3,[]]
b = copy.copy(a)

a is b #False
a == b #True

# A simple class to represent a student
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student({self.name}, {self.age})"


    def __str__(self) -> str:
        return f"Student({self.name}, {self.age})"


# A simple class to represent a class
class Class:
    def __init__(self, name:str, students:list):
        self.name = name
        self.students = students

    def __repr__(self):
        return f"Class({self.name}, {self.students})"

# Create a class with a list of students
s1 = Student("Student 1", 20)
s2 = Student("Student 2", 21)

class1 = Class("Class 1", [Student("Student 1", 20), Student("Student 2", 21)])

# Create a copy of the class
class2 = copy.copy(class1)

# Create a deep copy of the class
class3 = copy.deepcopy(class1)

# Print the classes
print("Original class:", class1)
print("Copy of the class:", class2)
print("Deep copy of the class:", class3)

# Modify the class
class1.students[0].name = "Student 3"
class1.students[0].age = 22

# Print the classes
print()
print("After modifying the original class:")
print("Original class:", class1)
print("Copy of the class:", class2)
print("Deep copy of the class:", class3)

# Why is the copy of the class not affected by the modification?
# Why is the deep copy of the class not affected by the modification? 
# What is the difference between copy() and deepcopy()?

# Answer:
# The copy of the class is not affected by the modification because the copy() function 
# creates a shallow copy of the class. A shallow copy of a class creates a new class
# object and copies the references of the class attributes to the new class object.
# In this case, the list of students is copied by reference, so when the list of students
# is modified, the copy of the class is also modified.
#
