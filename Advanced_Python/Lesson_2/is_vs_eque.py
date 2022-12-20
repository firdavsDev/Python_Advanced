# What is the difference between is and == ?

# Problem
a = 1000
# b = a
b = 1000

a is b #False
a == b #True

# Problem
c = 230
d = 230

c is d #True
c == d #True

print(c is d)
print(c == d)


# Answer
# is checks if two variables point to the same object in memory
# == checks if the objects referred to by the variables are equal
