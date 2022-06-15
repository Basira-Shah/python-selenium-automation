# Given a list of random number.
# Find and return max element and the index of this element
# Example: [1, 45, 33, 76, 9, 10], print [3, 76]

# (On)
def find_max_item(arr):
    max_num = arr[0]          # this is just an assumption that the first element of the list is the biggest element of
    max_index = 0             # the list

    for i in range(1, len(arr)):
        if arr[i] > max_num:      # here we compare our numbers from 45 mean range 1 to the max_num which is 1 till end
            max_num = arr[i]
            max_index = i

    print([max_index, max_num])

test_list = [1, 45, 33, 76, 9, 10]    # [3, 76]
find_max_item(test_list)

