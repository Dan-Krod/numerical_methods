# Direct and Iterative Methods for Solving Systems of Linear Algebraic Equations
### Objective:  
Study the most common direct and iterative methods for solving systems of linear algebraic equations, as well as their application for calculating determinants and matrix rotations.

### Theoretical Information:

1. **Overview of Methods for Solving Systems of Linear Algebraic Equations:**
   Numerical methods in linear algebra include methods for solving systems of linear algebraic equations, matrix rotations, determinant calculations, and finding eigenvalues and eigenvectors of matrices. This task focuses on solving systems of linear equations and indirectly addresses matrix rotation and determinant calculation.

2. **Gaussian Method:**
   The Gaussian method involves sequential elimination of unknowns, transforming the system of equations into an equivalent system with an upper triangular matrix, simplifying the solution process.

3. **Gaussian Method with Pivoting:**
   A problem with the basic Gaussian method occurs when the leading element is zero or close to zero, which complicates division. The Gaussian method with pivoting addresses this by sorting columns at each step, selecting the largest absolute element for computation.

---

## Task #6: Determinant Calculation Using Gaussian Method with Pivoting

### Algorithm:
1. The determinant is initialized to 1, and a copy of the matrix is made for modification.
2. At each step of the algorithm:
   - Select the pivot element in the current column.
   - Swap rows if necessary.
   - Normalize the row for element calculations.
   - Eliminate elements below the pivot element.
3. After the algorithm completes, the determinant is calculated as the product of the diagonal elements, accounting for sign changes due to row swaps.

### Recommendations for Implementation:

1. **Initialization:**
   - Set the determinant to 1.
   - Use a numeric array or matrix library like NumPy to ensure precise mathematical operations.
   - Determine the size of the matrix for iteration purposes.

2. **Iteration Through Each Column:**
   - For each column, find the pivot element (the element with the largest absolute value in the column).
   - If the pivot element is not in the current row, perform row swapping to place the largest element in the current row.
   - Normalize the current row and eliminate elements below the pivot by subtracting appropriate multiples of the pivot row from the other rows.

3. **Completion:**
   - After processing all columns, calculate the determinant as the product of the diagonal elements.
   - Consider any sign changes due to row swaps, as they affect the determinant value.

### Input Data:

The matrix for calculating the determinant will be as follows, with the variables s, k, and p as specified:

```python

s = 0.02 * k  # where k is the task number
p = group_number  # where group_number is the group number
A = [
    [8.3, 2.62 + s, 4.1, 1.9],
    [3.92, 8.45, 7.78 - s, 2.46],
    [3.77, 7.21 + s, 8.04, 2.28],
    [2.21, 3.65 - s, 1.69, 6.69]
]
```

### Expected Output:

After applying the Gaussian method with pivoting, the determinant can be calculated, and the result might be displayed like this:

```python
determinant = gaussian_method(A)
print(f"The determinant of the matrix = {determinant}")
```
