# Given an array of integers. Calculate
# return the list, calculate sum, and multiplication of elements
# Example: [1, 7, 3]


# (n)
def sum_and_mult(arr):
    sum_of_list = 0
    mult_of_list = 1

    for i in arr:
        sum_of_list += i
        mult_of_list *= i

    print(arr)
    print(sum_of_list)
    print(mult_of_list)

test_list = [1, 7, 3]
sum_and_mult(test_list)

