import numpy as np

def gaussian_method(matrix):
    determinant = 1  
    matrix = np.array(matrix, dtype=float)  
    size = matrix.shape[0]  

    for cur_column in range(size):
        max_val = abs(matrix[cur_column, cur_column])
        pivot_row = cur_column
        for row in range(cur_column + 1, size):
            if abs(matrix[row, cur_column]) > max_val:
                max_val = abs(matrix[row, cur_column])
                pivot_row = row

        if pivot_row != cur_column:
            matrix[[cur_column, pivot_row]] = matrix[[pivot_row, cur_column]]
            determinant *= -1 

        determinant *= matrix[cur_column, cur_column]

        for col in range(cur_column + 1, size):
            matrix[cur_column, col] /= matrix[cur_column, cur_column]

        for row in range(cur_column + 1, size):
            multiplier = matrix[row, cur_column]
            matrix[row, cur_column:] -= multiplier * matrix[cur_column, cur_column:]
    
    return determinant


A = [
    [8.3, 2.74, 4.1, 1.9],
    [3.92, 8.45, 7.66, 2.46],
    [3.77, 7.33, 8.04, 2.28],
    [2.21, 3.53, 1.69, 6.69]
]


determinant = gaussian_method(A)
print(f"The determinant of the matrix = {determinant}")

# NumPy
A_np = np.array(A, dtype=float)
det_np = np.linalg.det(A_np)
print(f"Numpy determinant = {det_np}")
