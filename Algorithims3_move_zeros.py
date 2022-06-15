# 0 4 0 3 12  ->  4 3 12 0 0
# O(N)
def move_zeros(arr):
    j = 0
    for num in arr:
        if num != 0:
            arr[j] = num
            j += 1

    while j < len(arr):
      arr[j] = 0
      j += 1

    return arr

test_data = [0, 4, 0, 3, 12]
print(move_zeros(test_data))