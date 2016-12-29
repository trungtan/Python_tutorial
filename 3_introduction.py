# 3. Introduction to Python - simple calculation
print (5/3) # division always returns a floating point number
print((50 - 5*6)/4)

print(7 // 3)   # floor division discards the fractional part
print(7 % 3)   # remainder

print(2**8)    # "**" is power


# variable assignment
squared = 2 * 8
print("The squared is", squared)

# work with string: using single quotes
# ... double qouptes will consider special characters in side (like PHP)
str = 'It\'s Python!\n The "shortest" language.'
print(str)

str = r"It's Python!\n The \"shortest\" language."
print(str)

# One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included
# but it’s possible to prevent this by adding a \ at the end of the line
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Two ore more strings (not string variables) next to each other are automatically concatenated.
print('py' "thon")

prefix = 'string variable'
print(prefix + ' concatened with other string by PLUS')

# string characters can be get by index, but cannot be changed
# word[:2]   # character from the beginning to position 2 (excluded)
# word[4:]   # characters from position 4 (included) to the end
# word[-2:]  # characters from the second-last (included) to the end
# However, out of range slice indexes are handled gracefully when used for slicing:
word = 'string variable'
print(len(word), word[0], word[-1], word[:4] + word[4:], word[-4:], word[7:100])

# string format https://docs.python.org/3.6/library/stdtypes.html#old-string-formatting
print('%(lang)s has %(num)03d quote types.' % {
        'lang': 'Python', 'num': 3
    })



