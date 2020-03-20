import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str(self.matrix)

    # Matrizenaddition
    def __add__(self, other):
        res1 = np.array(self.matrix)
        res2 = np.array(other.matrix)
        if not res1.shape == res2.shape:
            raise Exception("Die Matrizen müssen die selbe Anzahl an Spalten und Zeilen haben!")
        return Matrix(res1 + res2)

    # Skalarmultiplikation oder Matrizenmultiplikation
    def __mul__(self, other):
        if isinstance(other, Matrix):
            res1 = np.matrix(self.matrix)
            res2 = np.matrix(other.matrix)
            if not res1.shape[-1] == res2.shape[-2]:
                raise Exception("Die Anzahl der Spalten der ersten Matrix muss mit der Anzahl der Zeilen der zweiten Matrix übereinstimmen!")            
            np.dot(res1, res2)
            return Matrix(np.dot(res1, res2))
        else:
            return Matrix(np.matrix(self.matrix) * other)


matrix = Matrix([
    [2, 5, 8],
    [5, 3, 4]
])

matrix2 = Matrix([
    [2, 5],
    [5, 3],
    [8, 4]
])

result = matrix * 5
print("1", result)
print("\n")

result = matrix + matrix
print("2", result)
print("\n")

result = matrix * matrix2
print("3", result)
