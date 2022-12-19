# iteratort vs generator


# Problem
# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library. For example:

# import random
# random.randint(1,10)

# Solution
import random

def rand_num(low,high,n):
    for _ in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,3):
    print(num)


# Explanation
# A generator is a special type of function that returns a lazy iterator.
# Lazy iterators do NOT store all the values in memory, they generate the values on the fly:
#

# iter() & next()

lst = [1,2,3,4,5]

# for item in lst:
#     print(item)

iter_lst = iter(lst)
print(next(iter_lst))
print(next(iter_lst))
print(next(iter_lst))
print(next(iter_lst))
print(next(iter_lst))
try:
    print(next(iter_lst))
except StopIteration:
    print("StopIteration")


#################################################### Generator ####################################################

def square_numbers(nums):
    for i in range(nums):
        yield (i**2) # yield is a keyword that is used like return, except the function will return a generator. 
    
my_nums = square_numbers(10)

print(my_nums) # <generator object square_numbers at 0x0000020B1B2B0F48>
print(next(my_nums)) # 0
print(next(my_nums)) # 1
print(next(my_nums)) # 4


# Difference between yield and return
# yield is a keyword that is used like return, except the function will return a generator.

# To create a interator we need to use iter() and to get next value we need to use next() function
# Generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
# yeild is saves the local variable and return the value
# yeild is used to create generator

# Generator in python help us to save memory and time by not storing all the values in memory and return one value at a time

import types, collections

issubclass(types.GeneratorType, collections.Iterator) # True 
# Generator is a subclass of iterator so it is also an iterator


#################################################### Class Generator  ####################################################
                
class N_Even_Numbers:
  def __init__(self, num):
    self.num = num

  def __iter__(self): # __iter__ is a method of iterator in python
    self.counter = 0
    return self

  def __next__(self): # __next__ is a method of iterator
    if self.counter < self.num:
      cur = self.counter
      self.counter+=2
      return cur
    raise StopIteration('End of iteration')

# nums = N_Even_Numbers(5)

# for el in nums:
#   print(el)
# nums = iter(nums)

# print(next(nums))
# print(next(nums))
# print(next(nums))
