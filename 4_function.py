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

# MUTABLE and IMMUTABLE parameters