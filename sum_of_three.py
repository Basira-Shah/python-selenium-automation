# Our code generates a random three-digit number and has to sum up all its digit.
# For example, if a number is 349, the code has to print 16, because 3 + 4 + 9 = 16.


from random import randint    # its random function

random_number = randint(100, 999)
print(f'The random number is: {random_number}')

result = 0
# for digit in str(random_number):  # 349 [3, 4, 9] string
#    result = result + int(digit)

# O(n)  # n = Length of random_number
while random_number != 0:
    result = result + (random_number % 10)
    random_number = random_number // 10

print(f'Result: {result}')
