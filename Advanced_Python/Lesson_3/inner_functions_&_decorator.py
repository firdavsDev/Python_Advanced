# Lesson 3: Inner Functions & Decorator

# Why we need decorator?
# We need decorator to add some functionality to our function without changing the function itself or changing the function code
# When we need to use decorator?
# When we need to add some functionality to our function without changing the function itself or changing the function code
# What is decorator?
# Decorator is a function that takes another function as an argument adds some functionality and returns another function without altering the source code of the original function passed in.


# Example: Inner function
def make_adder(x):
    def add(n):
        return x + n
    return add


plus_3 = make_adder(3)
print(plus_3(10))


# Example: Passing function object as argument
def decorator(func):
    test = func()
    return f"{test} Davron"


def hello():
    return "Hello"


hello = decorator(hello)
print(hello)


# Example 2: Creating simple s_decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)
say_whee()
# same example with @
@my_decorator
def say_whee():
    print("Whee!")

# Example 3
def do_twice(func):
    def wrapper_do_twice(name):
        func(name)
        func(name)
    return wrapper_do_twice


@do_twice
def greet(name):
    print(f"Hello {name}")


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


greet("Davron")
return_greeting("Adam")



############################################ Decorator ############################################

def decorator_function(orginal_function):
    def wrapper_function(*args, **kwargs):
        print(f"wrapper executed this before {orginal_function.__name__}")
        return orginal_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("display function ran")

@decorator_function
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")

display_info("Davron", 25)

display()

# Class decorator example
class decorator_class(object):
        def __init__(self, original_function):
            self.original_function = original_function
    
        def __call__(self, *args, **kwargs):
            print(f"call method executed this before {self.original_function.__name__}")
            return self.original_function(*args, **kwargs)

@decorator_class
def display():
    print("display function ran")

@decorator_class
def display_info(name, age):
    print(f"display_info ran with arguments ({name}, {age})")

display_info("Davron", 25)

display()

# usefull decorators

# Example 1: Timer decorator
import time

def my_timer(original_function):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{original_function.__name__} ran in: {t2} sec")
        return result
    return wrapper

def display_info(name, age):
    time.sleep(1)
    print(f"display_info ran with arguments ({name}, {age})")

display_info = my_timer(display_info)
display_info("Davron", 25)

# Example 2: Logger decorator

def my_logger(original_function):
    import logging
    logging.basicConfig(filename=f"{original_function.__name__}.log", level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            f"Ran with args: {args}, and kwargs: {kwargs}")
        return original_function(*args, **kwargs)
    return wrapper

def display_info(name, age):
    time.sleep(1)
    print(f"display_info ran with arguments ({name}, {age})")

display_info = my_logger(display_info)
display_info("Davron", 25)

# Example 3: Combination of timer and logger decorator

def my_logger(original_function):
    import logging
    logging.basicConfig(filename=f"{original_function.__name__}.log", level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            f"Ran with args: {args}, and kwargs: {kwargs}")
        return original_function(*args, **kwargs)
    return wrapper

def my_timer(original_function):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{original_function.__name__} ran in: {t2} sec")
        return result
    return wrapper

import time

@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f"display_info ran with arguments ({name}, {age})")

display_info("Davron", 25)

# Example 4: Using functools

from functools import wraps


