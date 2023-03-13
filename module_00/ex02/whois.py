import sys

len = len(sys.argv)
if (len > 2) :
    exit(print('AssertionError: more than one argument are provided'))
if (len == 2 and sys.argv[1].isdigit()) :
    n = int(sys.argv[1])
    if (n % 2) :
        print('I\'m Odd.')
    elif (n == 0) :
        print('I\'m Zero.')
    else :
        print('I\'m Even.')
elif (len != 1) :
    print('AssertionError: argument is not an integer')
