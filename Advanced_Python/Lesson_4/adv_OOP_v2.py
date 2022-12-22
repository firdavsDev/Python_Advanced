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

print(obj)
# Class methods can be called from the class.
print(MyClass.classmethod())

# Static methods can be called from the class.
print(MyClass.staticmethod())

# Example:

class Pizza:
    def __init__(self, toppings: list):
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        # return Pizza(['mozzarella', 'tomatoes'])
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

    def crete_order(self, topings):
        self.toppings = topings

print(Pizza.margherita().toppings)
print(Pizza.prosciutto().toppings)
p_3 = Pizza(['cheese', 'onions', 'spam'])
print(p_3.crete_order(['cheese', 'onions', 'spam2']))

# Example:

class Pizza:
    def __init__(self, toppings: list):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        return topping != 'pineapple'

ingredients = ['cheese', 'onions', 'pineapple'] # spam is not a topping

if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
    print(pizza.toppings)
else:
    print('No pineapples!')

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
        self.make = make# public
        self.model = model

    def __str__(self):
        return f'{self.make} {self.model}'

class ElectricCar(Car):
    def __init__(self, make, model, range):
        super().__init__(make, model)
        self._range = range # protected

    def __str__(self):
        return f'{super().__str__()}, {self._range} miles on a charge'

class SuperCar(ElectricCar):
    def __init__(self, make, model, range, top_speed):
            super().__init__(make, model, range)
            self.__top_speed = top_speed # private
    
    def __str__(self):
        return f'{super().__str__()}, {self.__top_speed} mph'

    def get_speed(self):
        return self.__top_speed

    

gm = SuperCar('GM', 'Bolt', 300, 200)
print(gm)
print(gm._range)
# gm.__top_speed = 3000
# print(gm.__top_speed)
# print(gm.__top_speed) # AttributeError: 'SuperCar' object has no attribute '__top_speed'
print(gm.get_speed())
            

tesla = ElectricCar('Tesla', 'Model S', 300)
print(tesla.make)
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

    @staticmethod
    def get_child_count(child_count: int):
        return child_count > 0

class Dog(Animal):
    def fetch(self):
        print(f'{self.name} is fetching')

class Cat(Animal):

    def __init__(self, name, child_count=0):
        super().__init__(name)
        self.child_count = child_count

    def swatstring(self):
        print(f'{self.name} shreds the string!')

    @staticmethod
    def get_child_count(child_count: int):
        return child_count > 0

    @classmethod
    def set_child_count(cls, child_count: int):
        return cls('Isis', child_count)


if Cat.get_child_count(-1):
    print('Isis has kittens')
    isis_2 = Cat.set_child_count(-1)
    print(isis_2.child_count)
else:
    print('Isis has no kittens')

fido = Dog('Fido')
isis = Cat('Isis')

fido.fetch()
isis.swatstring()

fido.eat()
isis.drink()

### 3. Composition is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly