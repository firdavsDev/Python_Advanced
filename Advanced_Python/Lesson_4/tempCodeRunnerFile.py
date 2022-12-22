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
