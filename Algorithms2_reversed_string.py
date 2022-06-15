# Given a string. Resturn a reversed string.
# abcde  edcba

# O(n)
def reversed_string(s):
    reversed_s = ''
    index = len(s) -1
    while index >= 0:
        reversed_s += s[index]
        index -= 1
    return reversed_s

test_s = 'abcde'
print(reversed_string(test_s))   # edcba
