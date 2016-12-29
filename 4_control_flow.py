# 4. More Control Flow Tools
# https://docs.python.org/3.6/tutorial/controlflow.html

# x = int(input("Enter a number: "))
x = 10
if x < 0:
    x = 0
    print('%(num)d: Negative changed to zero' % {'num': x})
elif x == 0:
    print('Zero!')
else:
    print('%(num)10d: Positive' % {'num': x})

# FOR loop
#   range(10)       loop 1 to 9
#   range(5, 10)    loop 5 to 9
#   range(0, 10, 3)       loop 0 to 9 step 3

words = ['cat', 'window', 'defenestrate']
for i in range(len(words)):
    words[i] += ' checked'
print(words, end=', ')
print()

for w in words:     # loop through a list
    print(w)

for w in words[:]:     # loop through a COPY of a list
    print(w)

print(range(10)) # range() return successive items when you iterate over it, but it doesn't create a list to save memory
odds = list(range(1, 10, 2))        # list() creates a list from iterables
print(odds)
print()

# check prime numbers from 2 to 10
for number in range(2,10):
    for child in range(2, number):
        if number % child == 0:
            print(number, '=', child, ' * ', number//child)
            break
    else:
        print(number, 'is a prime number')

for number in range(0, 10):
    if number % 2 == 0:
        print(number, 'is even number')
        continue
    print(number, 'is odds')


class MyEmptyClass:
    pass    # pass works like an empty-code-block, a note for further implement

