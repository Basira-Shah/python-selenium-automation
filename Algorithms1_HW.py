# compute the sum of digits in all numbers from 1 to n.
# when a user enters a number n, find the sum of digits in all numbers from 1 to n.
# exmple: n = 5. result = 1 + 2 + 3 + 4 + 5 = 15

# HW-1
def sum_to_n(n):
    final_result = 0
    for x in range(n + 1):
        final_result += x
    return final_result

test_n = 5
print(sum_to_n(test_n))   # 1.


# Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.

number_1 = int(input('enter number 1: '))
number_2 = int(input('enter number 2: '))
number_3 = int(input('enter number 3: '))

# O(1)
def find_max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n1 and n2 > n3:
        return n2
    return n3


print(find_max(number_1, number_2, number_3))


# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).


# O(n)
def count_odd_even(n):
    odds = []
    evens = []

    while n != 0:
        current_digit = n % 10
        if current_digit % 2:
            odds.append(current_digit)
        else:
            evens.append(current_digit)
        n = n // 10
    return ['Even: ' + str(evens), 'Odds: ' + str(odds)]


print(count_odd_even(34560))