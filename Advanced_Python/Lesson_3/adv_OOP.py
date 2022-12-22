# Advanced Python, Lesson 3, Advanced OOP

# Public, Private, Protected attributes

# Public attributes
# Public attributes are attributes that can be accessed from outside the class. Public attributes are the default in Python.

# Private attributes
# Private attributes are attributes that cannot be accessed from outside the class. Private attributes are preceded by a double underscore (__) and are not inherited by subclasses.

# Protected attributes
# Protected attributes are attributes that cannot be accessed from outside the class, but can be accessed from subclasses. Protected attributes are preceded by a single underscore (_) and are inherited by subclasses.

# Example 1: Public, Private, Protected attributes

class Employee:
    def __init__(self, first, last):
        self.first = first 
        self.last = last
        self._email = f"{ self.first }.{ self.last }@company.com"
        self.__salary = 5000

    def fullname(self):
        return f"{ self.first } { self.last }"

    def email(self):
        return self._email  # Protected attribute

    def salary(self):
        return self.__salary # 

emp_1 = Employee("Davron", "Davronov")

print(emp_1.first)
print(emp_1.last)
print(emp_1.email())
print(emp_1.salary())

# Example 2: Public, Private, Protected attributes

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._color = "Black"
        self.__price = 10000

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_info(self):
        return f"{ self.brand } { self.model } { self.year }"

car_1 = Car("BMW", "X5", 2019)

print(car_1.get_info())
print(car_1.get_color())
print(car_1.get_price())

car_1.set_color("White")
car_1.set_price(20000)

print(car_1.get_color())
print(car_1.get_price())

class Tesla(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.__price = 50000
    
    def get_price(self):
        return self.__price

tesla_1 = Tesla("Tesla", "Model S", 2019)

print(tesla_1.get_info())
print(tesla_1.get_color())
print(tesla_1.get_price())




# What is super()?
# super() is a built-in function that returns a proxy object (temporary object of the superclass) that allows us to access methods of the base class.


########################################## Magic Methods ##########################################

# Magic methods are special methods that have double underscores at the beginning and end of their names. 
# They are used to emulate the behavior of built-in types. For example, to get the length of a string you can call len('string'), but behind the scenes, 
# Python actually calls 'string'.__len__(). Magic methods are always surrounded by double underscores, for example __init__(), __len__(), __add__(), __repr__(), etc.

# Example 1: Magic methods

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __repr__(self):
        return f"Employee('{ self.first }', '{ self.last }')"

    def __str__(self):
        return f"{ self.first } { self.last }"

    def __add__(self, other):
        return f"{ self.first } { other.last }"

    def __len__(self):
        return len(self.first) + len(self.last)

emp_1 = Employee("Davron", "Davronov")
emp_2 = Employee("Adam", "Smith")

print(emp_1)
print(emp_2)

print(emp_1 + emp_2)

print(len(emp_1))

# __repr__ is used to represent the object and is usually used for debugging and development.
# __str__ is used to display the object and is usually used for end-user display.
# __add__ is used to add two objects together using the + operator.
# __len__ is used to get the length of an object using the len() function.
# __format__ is used to format the object and is usually used for end-user display.

# __repr__ vs __str__ vs __format__: https://stackoverflow.com/questions/1436703/difference-between-str-and-repr

