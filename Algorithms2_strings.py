str = "This is my \"string\""
print(str)


str = "This is my string"
if 'i' in str:
    print("I is in our string")
else:
    print("I is not in our string!")


str = "This is my string"
print(str[0])  # T
print(str[-1]) # g
print(str[:3])   # it should stop at letter 3
print(str[5:8])
print(str[8:])

# concatination
str_1 = "This is my string."
str_2 = "This is my second string."

print(str_1 +" "+ str_2)

# Iterate string
for char in str_1:
    print(char)

# string methode.len()
print(len(str_1))

# string methode.lower()
print(str_1.lower())

# string methode.upper
print(str_1.upper())

# string methode.split()
print(str_1.split())
print(str_1.split('i'))

# string method.join()
list_str = ['This', 'is', 'a', 'list', 'of', 'string']
print(" ".join(list_str))
print("+".join(list_str))  # we can use any symbol here

# string methode.strip()
str_3 = "     This is my string.     "
print(str_3.strip())
str_4 = "111   This is my string.  1 1"
print(str_4.strip('1'))

# string methode.replace()
print(str_4.replace('i', '!'))

# string method.find()
print(str_4.find('h'))
print(str_4.find('H')) # if it didnt find so it will return -1

# string method.format()
string_w_arguments = '5 + 5 = {}'
print(string_w_arguments.format('12'))
value = 5 + 5
print(f'5 + 5 = {value}')


