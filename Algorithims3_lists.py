def print_numbers(arr):
    for num in arr[1:]:
        print(num)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print_numbers(array)


my_first_list = [1, 5, 7, 9]
my_second_list = [-5, 643, 6, 7, 8, 9]

print(my_first_list + my_second_list)
print(my_first_list[2])     # its also starting from 0 like indexes
print(my_first_list)
my_first_list.append(25)
print(my_first_list)
my_first_list.clear()
print(my_first_list)
print(my_first_list.count(5))
print(my_second_list.index(-5))
my_first_list.insert(0, 99)
print(my_first_list)
my_second_list.pop(1)
print(my_second_list)
my_second_list.remove(6)
print(my_second_list)
my_second_list.reverse()
print(my_second_list)
my_second_list.sort()
print(my_second_list)