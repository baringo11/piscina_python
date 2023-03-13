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
    elif (len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit()) : 
        sum(sys.argv[1], sys.argv[2])
        difference(sys.argv[1], sys.argv[2])
        product(sys.argv[1], sys.argv[2])
        quotient(sys.argv[1], sys.argv[2])
        remainder(sys.argv[1], sys.argv[2])
    elif (len(sys.argv) == 3) :
        print('Error: argument is not an integer')
