
# O(n)
def pair_sum(arr, k):
    if len(arr) < 2:
        return

    sum_set = set()

    for num in arr:
        target_value = k - num       # here we subtract the target value which is 16 from the numbers in array
        if target_value not in sum_set:
            sum_set.add(num)
        else:
            return [target_value, num]


test_data = [3, 7, 5, 9, 15, 3]
test_target = 16

print(pair_sum(test_data, test_target))
