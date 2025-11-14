# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

num = 6


print("Positive" if num > 0 else "Negative")
print()

result = "Even" if num % 2 == 0 else "Odd"
print(result)
print()

##

a = 6
b = 7

max_num = a if a > b else b
print(max_num)
print()

min_num = a if a < b else b
print(min_num)
print()

##

age = 25
status = "Adult" if age >= 18 else "Minor"
print(status)

##

temperature = 30
weather = "Hot" if temperature > 25 else "Cold"
print(weather)

##

user_role = "admin"
access = "Allowed" if user_role == "admin" else "Denied"
print(access)

