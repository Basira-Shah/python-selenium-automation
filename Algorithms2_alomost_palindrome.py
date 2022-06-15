def is_almost_palindrome(s):
    for i in range(len(s)):
        temp_s = s[:i] + s[i + 1:]
        if temp_s == temp_s[::-1]:
            return True               # so here in this function we are cheking that its almost palindrome or not
                                      # we are removing one one character to checke if its a palindrome
    return False

test_s_pos = 'radkar'
test_s_neg = 'radario'
print(is_almost_palindrome(test_s_pos)) # true
print(is_almost_palindrome(test_s_neg)) # false
