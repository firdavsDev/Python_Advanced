import time
start_time = time.time()

list_of_numbers = list(map(lambda x: x**2, range(1000))) # by map function 0.0019252300262451172
print(list_of_numbers)



# list_of_number = [i**2 for i in range(1000)] # by for loop 0.0006175041198730469
# print(list_of_number)

end_time = time.time()
print(end_time - start_time)


def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9)*(T-32)

temperatures = (36.5, 37, 37.5, 38, 39)

F = map(fahrenheit, temperatures)
C = map(celsius, F)

print(list(F))
print(list(C))

temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))

print(temperatures_in_Fahrenheit)
print(temperatures_in_Celsius)

# More https://www.geeksforgeeks.org/python-map-function/