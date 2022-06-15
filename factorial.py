# When user enters a number, its factorial is displayed.

import math

number = int(input('Input a number: '))
result = 1

# O(n) Simple search
for i in range(1, number + 1):
    result = result * i  # result *= i

print(f'Result: {result}')

result = math.factorial(number)     # Built in functions are not acceptable during homework but in work you can use it

print(f'Result: {result}')