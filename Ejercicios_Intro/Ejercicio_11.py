# • Generar una matriz "mat" de 4x4 con datos random
# • Obtener la suma de los valores de mat
# • Obtener la desviación estándar de los valores de mat
# • Obtener las sumas de las columnas de mat
import numpy as np

def describe_matrix(matrix:np.ndarray) -> None:
    matrix_sum = matrix.sum()
    matrix_dev = np.std(matrix)
    matrix_column_sum = matrix.sum(axis=1)
    print(
        f"""
        Suma: {matrix_sum}
        Desvio estandar: {matrix_dev}
        Suma columnas: {matrix_column_sum}""")

rand_mat = np.random.rand(4,4)
describe_matrix(rand_mat)