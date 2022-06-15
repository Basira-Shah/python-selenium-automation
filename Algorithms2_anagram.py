def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}    # here we create dictionary

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True



tests1_pos = 'abcd'     # POSITIVE
tests2_pos = 'badc'     # POSITIVE
tests1_neg = 'abcd'     # NEGATIVE
tests2_neg = 'abca'     # NEGATIVE

print(is_anagram(tests2_pos, tests1_pos))
print(is_anagram(tests2_neg, tests1_neg))