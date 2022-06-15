# User inputs two numbers. one number is assigned to a variable. the other number is assined to another variable.
# The task is to invert the variables, as that the first variable contains the second number, while the first number
# is in the second variable.

# O(1) constant time
a = int(input('Input value a: '))
b = int(input('Input value b:'))

print(f'a = {a}, b= {b}')

# temp = a
# a = b
# b = temp

print(f'a = {a}, b= {b}')

#  usually it is not always acceptable if you are able to solve the problem in one line code you can do it in
#  brute force solution
a, b = b, a

print(f'a = {a}, b= {b}')

# by math
# a = 10, b = 5

a = a + b  # 10 + 5 = 15
b = a - b  # 15 - 5 = 10
a = a - b  # 15 - 10 = 5


