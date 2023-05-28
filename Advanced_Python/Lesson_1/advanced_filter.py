# Map takes all objects in a list and allows you to apply a function to it
# Filter takes all objects in a list and runs that through a function to create a new list with all objects that return True in that function.


import time

start_time = time.time()

list_of_numbers = list(range(1000000))

# list_of_evens = list(filter(lambda x: x % 2 == 0, list_of_numbers))

# list_of_evens = [i for i in list_of_numbers if i % 2 == 0]

list_of_evens = []
for i in list_of_numbers:
    if i % 2 == 0:
        list_of_evens.append(i)
    else:
        pass

print(list_of_evens)
    

end_time = time.time()

print(end_time - start_time)