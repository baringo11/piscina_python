class Vector :
    def __init__(self, values) :
        elements = 0
        vector = []
        if isinstance(values, list) :
            for i in values :
                if isinstance(i, list) :
                    if len(i) == 1 :
                        if not isinstance(i[0], float) :
                            raise ValueError("should be a float")
                        vector.append(i[0])  # vector columna [[1.], [2.], [3.]]
                        self.shape = (len(vector), 1)
                    else :
                        for f in i :
                            if not isinstance(f, float) :
                                raise ValueError("should be floats")
                            vector.append(f)  # vector fila [[1., 2., 3.]]
                            self.shape = (1, len(vector))
                else :
                    raise ValueError("should be a nested list")
        else :
            raise ValueError("should be a list")
        self.values = vector

    def dot(self, vector) :
        if self.shape != vector.shape :
            print("different shape")
            return 1
        print (self.shape[0] * vector.shape[0] + self.shape[1] * vector.shape[1])
