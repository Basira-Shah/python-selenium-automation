# Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

# (n)
#def below_arithmetical_mean(arr):
#    arithmetical_mean = sum(arr) / len(arr)
#    final_list = []

#    for i in arr:
#        if i < arithmetical_mean:
#            final_list.append(i)

#    return final_list


# test_list = [1, 3, 5, 6, 4, 10, 2, 3]   # 4,25,    [1, 3, 4, 2, 3]
# print(below_arithmetical_mean(test_list))

# O(n)
# Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

# def find_two_lowest_element(arr):
#    arr.sort()
#    return arr[:2]

# test_data = [198, 3, 4, 9, 10, 9, 2]  # [2, 3]
# print(find_two_lowest_element(test_data))