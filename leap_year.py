# When a user enters a year, the code detects if its a leap year or not.
# A leap year is exactly divisible by 4 exxcept for century years (years ending with 00).
# The century year is a leap year only if it is perfectly divisible by 400. For example,

# 2017 is not a leap year
# 1900 is not a leap year
# 2012 is a leap year
# 2000 is a leap year


year = int(input('Input a year to check: '))

# O(1)
if year % 4 == 0:
    if year % 100 == 0:     # is it a century year
        if year % 400 == 0:
            print(f'{year} is a leap year')
        else:
            print(f'{year} is NOT a leap year')
else:
    print(f'{year} is NOT a leap year')