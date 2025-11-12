# Built-in Functions in Python and the Maths Module

x= 3.14
y = 4
z = 5

####

# round will round a floating-point number to the nearest integer
result = round(x)
print(result)
print()

# abs will return the absolute value of a number
result = abs(-5)
print(result)
print()

# pow will return the value of x raised to the power of y
result = pow(x, y)
print(result)
print()

# max will return the largest of the input values
result = max(x, y, z)
print(result)
print()

#min will return the smallest of the input values
result = min(x, y, z)
print(result)

######


import math

print(math.pi)  # Returns the value of pi
print(math.e)   # Returns the value of e
print(math.sqrt(16))  # Returns the square root of 16

print()

#maths.ceil will return the smallest integer greater than or equal to x
result = math.ceil(4.2)
print(result)

#maths.floor will return the largest integer less than or equal to x
result = math.floor(4.2)
print(result)


