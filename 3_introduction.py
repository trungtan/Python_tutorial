# 3. Introduction to Python - simple calculation
print (5/3) # division always returns a floating point number
print((50 - 5*6)/4)

print(7 // 3)   # floor division discards the fractional part
print(7 % 3)   # remainder

print(2**8)    # "**" is power


# variable assignment
squared = 2 * 8
print("The squared is", squared)

# ########## WORK WITH STRING: immutable data type (cannot change)
# using single quotes
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

# ########## WORK WITH LIST: mutable data type
print('\n------------------------------------------------------\n')
squares = [1, 4, 9, 16, 25]

# slide operations
print(len(squares), squares[:2], squares[2:4], squares[:1] + squares[2:3])  # use PLUS concat like string

squares[0] = 2**3
squares.append(3**4)        # add to the end
print(squares[:])

# bulk-changing with slide
squares[-3:-1] = ['x', 'y', ['nested', 'list']]
print(squares)

# ########## Some new features
# multiple assignment
a, b = 0, 1
while b < 10:       # The body of the loop is indented: indentation is Python’s way of grouping statements
    print(b, end=', ')      # set the end-line character
    a, b = b, a + b
