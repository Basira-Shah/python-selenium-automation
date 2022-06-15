# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

# O(n)
#def split_in_half(s):             # we split and then we swap it
#    lenght = len(s)
#    half = lenght // 2
#    add = 0

#    if lenght % 2:
#        add = 1

#    left = s[:half + add]
#    right = s[half + add:]
#    print(f'left = {left}')
#    print(f'right = {right}')

#    print(right + left)

#test_data_even = 'aaaccc'    # -> cccaaa
#test_data_odd = 'aaabccc'    # -> cccaaab
#split_in_half(test_data_odd)
#split_in_half(test_data_even)


# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

# abcde -> True
# abcdea -> False

# def uni_char(s):
#    return len(set(s)) == len(s)

# O(n)
def uni_char(s):
    chars = set()

    for let in s:
        if let in chars:
            return False
        chars.add(let)

    return True

test_data_all_uni = 'abcde'
test_data_all_dup = 'abcdea'

print(uni_char(test_data_all_uni))
print(uni_char(test_data_all_dup))