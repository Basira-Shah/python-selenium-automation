# [3, 5, 5] -> false
# [3, 4, 5, 2] -> true
# O(n)
def is_mountin(array):
    if len(array) < 3:
        return False

    i = 1
    while i < len(array) and array[i] > array[i - 1]:
        i += 1
        if i == 1 or i == len(array):
            return False
    while i < len(array)  and array[i] < array[i -1]:
        i += 1

    return i == len(array)

test_data_pos = [1, 4, 7, 9, 5, 2]
test_data_neg = [1, 4, 7, 9, 5, 6]

print(is_mountin(test_data_pos))
print(is_mountin(test_data_neg))