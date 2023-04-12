import sys

def sum(a, b):
    print("Sum:          " + str(int(a) + int(b)))
def difference(a, b):
    print("Difference:   " + str(int(a) - int(b)))
def product(a, b):
    print("Product:      " + str(int(a) * int(b)))
def quotient(a, b):
    if (int(b) == 0) :
        print("Quotient:     ERROR (division by zero)")
    else :
        print("Quotient:     " + str(int(a) / int(b)))
def remainder(a, b):
    if (int(b) == 0) :
        print("Remainder:    ERROR (modulo by zero)")
    else :
        print("Remainder:    " + str(int(a) % int(b)))

if __name__ == "__main__" :
    if (len(sys.argv) != 1 and len(sys.argv) != 3) :
        print('Error: need two arguments')
    elif (len(sys.argv) == 3) : 
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            sum(a, b)
            difference(a, b)
            product(a, b)
            quotient(a, b)
            remainder(a, b)
        except:
            print('Error: argument is not an integer')
