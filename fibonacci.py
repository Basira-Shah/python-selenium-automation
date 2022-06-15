# The equation for the Fibonacci sequence;
#
# first two numbers are always 1
# The task is to dispalay all the numbers from start to n of the Fibonacci sequence

# Equation
# F0 = 0
# F1 = 1
# F2 = 1
# Fn = fn-1 + Fn-2

# 1 1 2 3 5 8 13

# O(n)
fib_number = int(input('Provide a number:'))
index = 3  # index is 3 because we start from the 3rd number of fibonacci the first two numbers are 1,1
fib_1 = 1
fib_2 = 1
result = [fib_1, fib_2]

while index <= fib_number:
    result.append(fib_1 + fib_2) # we take the sum of these numbers and adding to the above list
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    index = index + 1 # index +=1

print(result)


