from vector import Vector

if __name__ == "__main__" :
    # CONSTRUCTOR
    print("-----CONSTRUCTOR-----")
    filaVec = Vector([[1., 2., 3.]])
    colVec = Vector([[1.],[2.], [3.]])
    print(str(filaVec) + "   " + str(filaVec.shape))
    print(str(colVec) + "   " + str(colVec.shape))

    rangoVec = Vector(6)
    rangoVec2 = Vector((5,10))
    print(str(rangoVec) + "   " + str(rangoVec.shape) )
    print(str(rangoVec2) + "   " + str(rangoVec2.shape))

    # SUMA
    print("\n-----SUMA-----")
    filaVec1 = Vector([[4., 5., 6.]])
    colVec2 = Vector([[4.],[5.], [6.]])
    print(filaVec + filaVec1)
    print(colVec + colVec2)

    print(filaVec + 5)
    print(colVec + 5)

    # MULTIPLICACION
    print("\n-----MULTIPLICACION-----")

    print(filaVec * filaVec1)
    print(colVec * colVec2)

    print(filaVec * 5)
    print(colVec * 5)
    #prueba.dot(prueba1)
   # prueba2 = Myvector("fdsdf")

    """
    # Column vector of shape n * 1
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = v1 * 5
    print(v2)
    # Expected output:
    # Vector([[0.0], [5.0], [10.0], [15.0]])
    # Row vector of shape 1 * n
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v2 = v1 * 5
    print(v2)
    # Expected output
    # Vector([[0.0, 5.0, 10.0, 15.0]])
    v2 = v1 / 2.0
    print(v2)
    # Expected output
    # Vector([[0.0], [0.5], [1.0], [1.5]])
    v1 / 0.0
    # Expected ouput
    # ZeroDivisionError: division by zero.
    2.0 / v1
    # Expected output:
    # NotImplementedError: Division of a scalar by a Vector is not defined here.
    """
    