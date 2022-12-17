# What is the difference between is and == ?

# Problem
a = 1000
# b = a
b = 1000

a is b #False
a == b #True

# Problem
a = 100
b = 100

a is b #True
a == b #True



# Answer
# is checks if two variables point to the same object in memory
# == checks if the objects referred to by the variables are equal
