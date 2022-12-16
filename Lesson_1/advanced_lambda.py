import time 

start_time = time.time()

if_then_else = lambda cond: lambda then_do: lambda else_do: cond(then_do)(else_do) #nested lambda function

troo = lambda then_do: lambda else_do: then_do #lambda function 
falz = lambda then_do: lambda else_do: else_do #lambda function

tired = troo
not_tired = falz

coffees_today = if_then_else(tired)(3)(1)
print(coffees_today)

end_time = time.time()

print(end_time - start_time)



#More https://www.geeksforgeeks.org/nested-lambda-function-in-python/
