# 4. More Control Flow Tools - WORK WITH FUNCTION
# https://docs.python.org/3.6/tutorial/controlflow.html#defining-functions
# arguments are passed using call by value (where the value is always an object reference, not the value of the object)


def fib(n):
    """
    This section goes for the function document
    Print a Fibonacci up to n
    :param n:
    :return: None       # None = void data type
    """
    a, b = 0, 1
    while b < n:
        print(b, end=', ')
        a, b = b, a+b

print(fib.__doc__)
fib(2000)
print()


def fibonacci(n):
    """
    Another version with return
    :param n:
    :return: []
    """
    a, b = 0, 1
    result = []
    while b < n:
        result.append(a)    # faster than result + [a]
        a, b = b, a + b
    return result
print(fibonacci(100))


def default_arg(required, op1 = 10, op2 = 'just an option'):
    pass

# if the default value of a parameter is a mutable data type, it will be shared between calls
def fshare(a, L=[]):
    L.append(a)
    return L

print(fshare(1))
print(fshare(2))
print(fshare(3))

# If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
def fnone(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(fnone(1))
print(fnone(2))
print(fnone(3))

# keyword arguments: functions can be called with parameters key=value or by position
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    pass

parrot(voltage=1000000, action='VOOOOOM')
parrot('a thousand', state='pushing up the daisies')
parrot('a million', 'bereft of life', 'jump')
# parrot(voltage=5.0, 'dead')   # error: after a keyword argument must be keyword arguments
print("-" * 40)


# *arguments: position-parameters, must be put before keyword-parameters
# **keywords: parameters with key=value
def cheeseshop(kind, *arguments, **keywords):
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

