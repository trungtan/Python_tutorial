# https://docs.python.org/3.5/tutorial/interpreter.html
# Test parsing argument by running:
#    python 2_Interpreter.py -f "first value" -s "second value" "other value"
#

import sys

# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])
# print(sys.argv[3])

count = len(sys.argv)
for i in range(count):
    print(i, ' ', sys.argv[i])
