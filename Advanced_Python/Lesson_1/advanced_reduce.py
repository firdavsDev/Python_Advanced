from functools import reduce

list_of_numbers = [1,2,3,4]

# list_of_numbers = list(range(1000000))
print(reduce(lambda x,y: x*y, list_of_numbers))
