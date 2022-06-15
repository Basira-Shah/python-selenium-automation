# (n)
def compress_string(s):
    if len(s) == 0:
        return ''

    if len(s) == 1:
        return s + '1'

    compressed = ''
    cnt = 1
    i = 1

    while i < len(s):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            compressed = compressed + s[i - 1] + str(cnt)
            cnt = 1
        i += 1
    compressed = compressed + s[i -1] + str(cnt)

    return compressed


test_str = 'AAABBBCCD'  # A3B3C2D1
print(compress_string(test_str))

