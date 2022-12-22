class MyClassName:
    age = 30

    def __init__(self, name:str, age:int=30):
        self.name:str = name
        self.age = age

        self.validate_age()
    
    def validate_age(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative.")

    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name and self.age == __o.age

object_1 = MyClassName("John", 30)
object_2 = MyClassName("Davron", 40)
print(object_2>object_1)
object_1.age = -4
print(object_1.validate_age())


# Dataclass in Python 3.7

# What is a dataclass?
# A dataclass is a class that is used to store data.

# Why use a dataclass?
# A dataclass is useful when we want to store data in a structured way.

# Import the dataclass decorator.
from dataclasses import dataclass, field, asdict, astuple

# Define a dataclass.
@dataclass
class Person:
    name: str
    age: int
    active: bool = field(default=True, repr=False)


# Create a Person object.
person_1 = Person("John", 30)
person_2 = Person("John", 30)

#compare two objects
print(person_1 == person_2)
print(person_1 is person_2)

# Print the Person object.
print(person_1) #Person(name='John', age=30, active=True)

# Print the person_1 object's name.
print(person_1.name)

# asdict() function
# The asdict() function returns a dictionary representation of the dataclass.
print(asdict(person_1))

# astuple() function
# The astuple() function returns a tuple representation of the dataclass.
print(astuple(person_1))



########## Dataclass Parameters ##########

# field() function
# The field() function allows us to specify additional information about the dataclass field.
# We can use the default parameter to specify a default value for the field.
# We can use the default_factory parameter to specify a function that returns a default value for the field.

# frozen parameter (default=False) - If True, the dataclass is immutable.
# order parameter (default=False) - If True, the dataclass is ordered.
# slots parameter (default=False) - If True, the dataclass uses __slots__ instead of __dict__.
# kw_only parameter (default=False) - If True, only keyword arguments are allowed in the constructor. Example: Person(name="John", age=30) is allowed, but Person("John", 30) is not allowed.
# match_args parameter (default=False) - If True, the dataclass is used to match arguments in a function call. Example: def foo(person: Person): pass foo(Person("John", 30)) is allowed, but foo(Person("John", 30) is not allowed.

from dataclasses import dataclass, field, asdict, astuple

@dataclass(frozen=True, order=True, slots=True, match_args=True)
class Comment:
    id: int = field(compare=False, hash=False, repr=False)
    likes: int = field(default=0)
    text: str = field(default="No comment.")
    replies: list[int] = field(default_factory=[], compare=False, hash=False)

# Create a Comment object.
comment_1 = Comment(4, "This is a comment.", 5, )
print(comment_1)
comment_2 = Comment(1, "This is a comment.", 5, [2, 3, 4])

# Print the Comment object.
# comment.id = 1 # AttributeError: cannot assign to field 'id'
print(comment_1 == comment_2) # [2, 3, 4]


# with dataclass decorator we don't need to define __init__ method anymore, it is done automatically
# Simple Class we write megic methods like __init__ and __repr__ manually but with dataclass decorator we don't need to do that


# __post_init__ method is called after __init__ method and it is used to do some post initialization work
# __setattr__ method is called when we try to set an attribute on an object
# __getattr__ method is called when we try to get an attribute on an object
# __delattr__ method is called when we try to delete an attribute on an object

from dataclasses import dataclass, field, asdict, astuple

@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        '''Called after __init__ method.'''
        if self.age < 0:
            raise ValueError("Age cannot be negative.")
    
    def __setattr__(self, name, value):
        '''Called when we try to set an attribute on an object.'''
        print(f"Setting attribute {name} to {value}")
        super().__setattr__(name, value)

# Create a Person object.
person = Person("John", -30)

# Print the Person object.
print(person)


########## Dataclass validate ##########

from dataclasses import dataclass, field, asdict, astuple

@dataclass
class Employee:
    name: str
    age: int
    salary: float = field(default=0.0, repr=False)

    def __post_init__(self):
        '''Called after __init__ method.'''
        if self.age < 0:
            raise ValueError("Age cannot be negative.")
        if self.salary < 0:
            raise ValueError("Salary cannot be negative.")

# Create an Employee object.
employee_1 = Employee("John", 30)
employee_2 = Employee("John", 30)

# Print the Employee object.
print(employee_1>employee_2)

