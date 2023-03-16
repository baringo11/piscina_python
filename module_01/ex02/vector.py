class Vector :
    def __init__(self, values) :
        if isinstance(values, list) :
            if all(isinstance(i, list) and len(i) == 1 for i in values) :
                self.values = values # vector columna [[1.], [2.], [3.]]
                self.shape = (len(values), 1)
            else :
                self.values = values # vector fila [[1., 2., 3.]]
                self.shape = (1, len(values[0]))
        elif isinstance(values, tuple):
            if values[0] > values[1]:
                raise ValueError("Invalid range: the first value must be less than the second value.")
            self.values = [[float(i)] for i in range(values[0], values[1])]
            self.shape = (len(self.values), 1)
        elif isinstance(values, int):
            self.values = [[float(i)] for i in range(values)]
            self.shape = (values, 1)
        else :
            raise ValueError("Invalid arg for constructing Vector")

    def dot(self, vector) :
        if self.shape != vector.shape :
            raise ValueError("Shapes aren't equal")
        return self * vector

    def T(self) :
        result = []
        for i in range(self.shape[1]):
            row = []
            for j in range(self.shape[0]):
                row.append(self.values[j][i])
            result.append(row)
        return Vector(result)

    def __str__(self):
        return str(self.values)

    def __add__(self, other):
        if isinstance(other, (int, float)) :
            other = Vector([[other] * self.shape[1]] * self.shape[0])
        if isinstance(other, Vector) :
            if self.shape != other.shape:
                raise ValueError("Shapes aren't equal")
            return Vector([[x + y for x, y in zip(a, b)] for a, b in zip(self.values, other.values)])

    def __mul__(self, other):
        if isinstance(other, (int, float)) :
            other = Vector([[other] * self.shape[1]] * self.shape[0])
        if isinstance(other, Vector) :
            if self.shape != other.shape:
                raise ValueError("Shapes aren't equal")
            return Vector([[x * y for x, y in zip(a, b)] for a, b in zip(self.values, other.values)])

    
