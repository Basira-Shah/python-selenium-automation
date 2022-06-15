# inputs
# [2, 1, 3, 7, 5, 6, 4], [3, 7, 2, 1, 4, 6]
# O(n)
# def find_missing_number(arr1, arr2):
#    arr1.sort()                         # O(n * logn) a fast sorting algorithims
#    arr2.sort()

#    for num1, num2 in zip(arr1, arr2):     # zip means we are comparing two arrays with each other
#        if num1 != num2:
#            return num1

#    return arr1[-1]    # here if dont find the missing element it will return -1

import collections

# {key1: value1, key2: value2}
# O(n)
def find_missing_number(arr1, arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

test_arr1 = [1, 2, 3, 4, 5, 6, 7]
test_arr2 = [3, 7, 2, 1, 4, 6]

print(find_missing_number(test_arr1, test_arr2))