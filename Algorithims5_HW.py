# Algo HW5
# O(n^2)
def selection_sort(arr):
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


test_list = [4, 7, 2, 9, 3, 11, 1]  # 1, 2, 3, 4, 7, 9, 11
print(test_list)
print(selection_sort(test_list))


# O(n^2)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i -1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


test_list = [11, 5, 4, 1, 7, 98, 3]
print(test_list)
print(bubble_sort(test_list))


# O(N^2)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


test_list = [4, 7, 5, 1, 8, 9, 12, 2]
print(test_list)
print(insertion_sort(test_list))



# O(n * logn)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def merge_arrays(left_arr, right_arr):
    merged_array = []
    i = j = 0

    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_array.append(right_arr[j])
            j += 1
            continue
        if j == len(left_arr):
            merged_array.append(left_arr[i])
            i += 1
            continue
        if left_arr[i] >= right_arr[j]:
            merged_array.append(left_arr[i])
            i += 1
        else:
            merged_array.append(right_arr[j])
            j += 1

    return merged_array


test_list = [5, 3, 6, 2, 7, 1, 8, 4]
print(test_list)
print(merge_sort(test_list))

