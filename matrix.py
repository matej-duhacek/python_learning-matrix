import numpy as np

values = np.arange(15).reshape(5, 3)
print(values)
print(values.shape)
print(values.ndim)
print(values.size)


class Matrix(object):
    def __init__(self, matrix_string):
        pass

    def row(self, index):
        pass

    def column(self, index):
        pass

    def get_transformed_matrix(self):
        pass;
