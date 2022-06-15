# Write a program that takes as input a sorted array and updates it so that duplicates
# have been removed and the remaining elements have been shifted left to fill the emptied indices
# fill the remaining indices with zeroes
# return the number of valid elements
# you can not use sets for this coding chalenge


# O(n)
def delete_duplicates(arr):
    write_index = 1              # the first element is always unqiue the second element could be the same as first one
                                 # so thats why we are starting  with index 1 basically the second element
    for i in range(1, len(arr)):
        if arr[write_index -1] != arr[i]:    # if the previous index is not equal to current index we are comparing the
            arr[write_index] = arr[i]        # indexes of list with the previous one for example the first two are same
            write_index += 1                 # and we skip it and then we check 4 with 1 means with first index and then
                                             # 6 with 4 an till end
    for i in range(write_index, len(arr)):
        arr[i] = 0

    return write_index, len(arr) - write_index


test_list = [1, 1, 4, 6, 8, 31, 31, 45, 98]  #  7 number of valid elements, 2 number of duplicate element
print(delete_duplicates(test_list))
