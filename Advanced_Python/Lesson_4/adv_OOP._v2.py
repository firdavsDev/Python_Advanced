######################################### Python advanced OOP #########################################

## Questions

### 1. What is the difference between a class and an object?
### 2. What is the difference between a @classmethod and a @staticmethod?

## Answers

### 1. A class is a blueprint for creating objects. An object is an instance of a class. A class is like a cookie cutter and an object is like a cookie.
### 2. A @classmethod is a method that is bound to a class rather than its object. It doesn't require creation of a class instance, much like staticmethod. A @staticmethod is a method that knows nothing about the class and just deals with the parameters.
# Example:

class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()

# Class methods can be called from the class.
print(MyClass.classmethod())
print(MyClass.staticmethod())

# Static methods can be called from the class.
print(MyClass.staticmethod())

# Example:

class Pizza:
    def __init__(self, toppings: list):
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

print(Pizza.margherita().toppings)
print(Pizza.prosciutto().toppings)

# Example:

class Pizza:
    def __init__(self, toppings: list):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == 'pineapple':
            raise ValueError('No pineapples!')
        else:
            return True

ingredients = ['cheese', 'onions', 'spam'] # spam is not a topping
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

######################################### Python Encapsulation #########################################

## Questions

### 1. What is encapsulation?
### 2. What is the purpose of encapsulation?
### 3. What is the difference between public, protected, and private attributes?

## Answers

### 1. Encapsulation is the process of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variable.   
### 2. The purpose of encapsulation is to hide the values or state of a structured data object inside a class, preventing unauthorized parties' direct access to them.
### 3. Public attributes can be accessed from outside the class. Protected attributes should not be used outside the class, unless inside a subclass. Private attributes should never be used outside the class.

# Example:

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f'{self.make} {self.model}'

class ElectricCar(Car):
    def __init__(self, make, model, range):
        super().__init__(make, model)
        self._range = range

    def __str__(self):
        return f'{super().__str__()}, {self._range} miles on a charge'

tesla = ElectricCar('Tesla', 'Model S', 300)
print(tesla)
print(tesla._range) # 300

######################################### Python Inheritance #########################################

## Questions

### 1. What is inheritance?
### 2. What is the purpose of inheritance?
### 3. What is the difference between composition and inheritance?

## Answers  

### 1. Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly
### 2. The purpose of inheritance is to specify a new class that is a modified version of one or more existing classes.

# Example:

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def drink(self):
        print(f'{self.name} is drinking')

class Dog(Animal):
    def fetch(self):
        print(f'{self.name} is fetching')

class Cat(Animal):
    def swatstring(self):
        print(f'{self.name} shreds the string!')

fido = Dog('Fido')
isis = Cat('Isis')

fido.fetch()
isis.swatstring()

fido.eat()
isis.drink()

### 3. Composition is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly