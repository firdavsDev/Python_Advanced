from itertools import chain, groupby, cycle, islice, count, dropwhile, takewhile

# groupby() takes a sequence and a function and groups the
# items in the sequence by the return value of the function.


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

grouped = groupby(numbers, key=lambda x: x < 3) # True [1, 2] False [3, 4, 5, 6, 7, 8, 9]

for key, value in grouped:
    print(key, list(value))

# Task: Group the persons by age
persons = [
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 23},
    {'name': 'Jack', 'age': 25},
    {'name': 'Jill', 'age': 23},
    {'name': 'Joe', 'age': 25},
]


# in filter() the function is applied to each item in the sequence and a new sequence is returned with only the items for which the function returned True.
filtered = list(filter(lambda x: x < 3, numbers))
print(filtered) # [1, 2]

#################################################### cycle ####################################################
# cycle() takes a sequence and returns an iterator that returns the items in the sequence over and over again.
# It is useful when you want to iterate over a sequence but don't want to use a for loop.
# It is also useful when you want to cycle over a sequence indefinitely.
# The following example shows how to use cycle() to cycle over a sequence indefinitely.
# The example also shows how to use zip() to combine two sequences.
# The example also shows how to use islice() to slice an iterator.

colors = ['red', 'green', 'blue']
cycles = cycle(colors)
limited = islice(cycles, 0, 10) # 0 is the start index, 10 is the end index
print(list(limited)) # ['red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue', 'red']

#################################################### count ####################################################
# count() returns an iterator that returns consecutive integers, starting with 0 by default.
# The following example shows how to use count() to create an iterator that returns consecutive integers starting with 1.

# use count to create a simple counter
count1 = count(100, 10)
print(next(count1))  # 100
print(next(count1))  # 110
print(next(count1))  # 120


#################################################### chain ####################################################
# chain() takes a number of sequences as arguments and returns an iterator that returns the items in the sequences one after the other.
# The following example shows how to use chain() to combine two sequences.

# use chain to connect sequences
# use chain to connect sequences together
x = chain("ABCD", "1234")
print(list(x))  # ['A', 'B', 'C', 'D', '1', '2', '3', '4']


#################################################### dropwhile ####################################################
# dropwhile() returns an iterator that returns the items in the sequence after the predicate function returns False for the first time.
# The following example shows how to use dropwhile() to drop items from a sequence while the predicate function returns True.

# dropwhile and takewhile will return values until
# a certain condition is met that stops them

vals = [10, 20, 30, 40, 50, 40, 30]
print(list(dropwhile(lambda x: x<40, vals)))  # [40, 50, 40, 30]
print(list(takewhile(lambda x: x<40, vals)))  # [10, 20, 30]
