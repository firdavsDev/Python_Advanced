def make_adder(x):
    def add(n):
        return x + n
    return add


plus_3 = make_adder(3)
print(plus_3(10))



# Example 1: Passing function object as argument
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