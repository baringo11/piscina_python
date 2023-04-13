import sys

len = len(sys.argv)
if (len > 2) :
    exit(print('Error: more than one argument are provided'))
if (len == 2):
    try:
        n = int(sys.argv[1])
        if (n % 2) :
            print('I\'m Odd.')
        elif (n == 0) :
            print('I\'m Zero.')
        else :
            print('I\'m Even.')
    except:
        print('Error: argument is not an integer')
