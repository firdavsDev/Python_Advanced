import time

start_time = time.time()

list_of_numbers = list(range(1000000))

list_of_evens = list(filter(lambda x: x % 2 == 0, list_of_numbers))

# list_of_evens = [i for i in list_of_numbers if i % 2 == 0]
print(list_of_evens)
    

end_time = time.time()

print(end_time - start_time)