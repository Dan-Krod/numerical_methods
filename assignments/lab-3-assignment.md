# Newton's Method and ε-Algorithm for Solving Systems of Nonlinear Equations

### Objective
Study the most common iterative method for solving systems of nonlinear equations, Newton's method, and the extrapolation method, ε-algorithm.

### Theoretical Information

1. **Overview of Methods for Solving Systems of Nonlinear Equations**
The task involves finding solutions to systems of nonlinear equations, which is a common requirement in scientific and technical fields. This can be accomplished using Newton's method and the ε-algorithm.

2. **Extrapolation Methods**
- Scalar ε-Algorithm
The ε-algorithm, developed by Peter Wynn in 1956, improves the convergence of the sequence ```S = (s_0, s_1, s_2, ... s_i)```. This algorithm consists of the following steps:
- **Initialization**: ```for (j = 0, 1, 2, ...)```
```markdown
ε(j)_{-1} = 0 (artificially)
```
  - **Iteration**: ```for (k, j = 0, 1, 2, ...)```
```markdown
The scalar ε-algorithm forms a square matrix of size (n + 1) × (n + 1), where n is an odd number of elements in the sequence (S_n).
```
Example implementation in C++:
```cpp
const int n = 5;
double e[n + 1][n + 1] = {{0, 4}, {0, 2.667}, {0, 3.467}, {0, 2.895}, {0, 3.339}, {0, 0}};
for (int k = 1; k <= n - 1; k++) {
    for (int j = 0; j++) {
        e[j][k + 1] = e[j + 1][k - 1] + 1 / (e[j + 1][k] - e[j][k]);
    }
}
```

3. **Application of the ε-Algorithm for Nonlinear Systems:**
To find the solution of a nonlinear system with a given accuracy ```ε```, the system must be transformed into an equivalent form (suitable for the simple iteration method). The condition roughly means that in the vicinity of the solution, the derivatives ```∂g_i / ∂x``` for all ```i``` and ```j``` should be "sufficiently small in magnitude." In other words, the system should be transformed so that the functions ```g_i``` change weakly with the change of arguments, i.e., they should be "almost constant."
---
## Task #6: Initial Approximations for Roots
For the ε-algorithm: ```q = 2```, ```p = 2```

### Algorithm

1. **Initialization**:
    - Setting initial values: ```m``` (dimension of the system of equations), ```q``` (can be set as ```q = m```), ```n = 2q + 1``` (dimension of the ```(S_n)``` sequence), ```p``` (number of initial iterations).
    - Set the initial approximation ```x(0)_i``` for ```i = (1, m)```, and the relative error ```ε``` in percentage.
2. **Set Zeros in the ε-Matrix**:
   - Set zeros in the ε-matrix for the case when ```k = −1```.
3. **Perform Initial Iterations**:
   - Perform ```p``` initial iterations.
4. **Set Initial Values for the ```(S_n)``` Sequence**:
   - Set the initial values for the ```(S_n)``` sequence.
5. **Generate the ```(S_n)``` Sequence**:
   - During the sequence generation stage, check the convergence of the method.
6. **Extrapolation Stage**:
   - Calculate the inverse vector using the Samuelson rotation procedure and find the limit of the ```(S_n)``` sequence corresponding to the element of the matrix ```e0, n, i```. Assign the found limit to the vector of unknowns.
7. **Check Condition for Terminating the Iterative Process**:
   - If it is not met, repeat the refinement process (step 4).
8. **Verification of Algorithm**:
   - Substitute the found values ```x1, x2, xm``` into the system of equations ```F(x) = 0```. The function values ```f_i``` for ```i = 1, m``` should be close to zero, depending on the chosen value of ```ε```.

### Recommendations for Implementation
1. Set the initial conditions appropriately.
2. Use a numeric library like NumPy for precise mathematical operations.
3. Ensure proper handling of interval boundaries and convergence checks.

### Input Data
The input data will be:
- ```m = 2```
- ```q = 2```
- ```p = 2```
- ```n = 2 * q - 1```
- ```x_initial = [0.1, 0.1]```
  
> **⚠️ Note:** More detailed input data can be found in the `input_data` folder, specifically in the `input_data(lab-3)` file.

#### Function Definitions:
```python
def f1(x1, x2):
    denominator = x1**2 + x2**2
    return (x1 / denominator) + 0.4 - x1

def f2(x1, x2):
    denominator = x1**2 + x2**2
    return (-x2 / denominator) + 1.4 - x2
```

### Expected Output
- Iteration 1: Initial values ```x = [0.1, 0.1]```
- Iteration 2: Updated values ```x = [1.1267865054998407, 0.9552899635109329]```
- Iteration 3: Updated values ```x = [0.9557836979179284, 0.8905602224868227]```
- Iteration 4: Updated values ```x = [0.9637051471401556, 0.882544933435486]```
- Iteration 5: Updated values ```x = [0.9639787503408704, 0.8832704389877885]```
- Iteration 6: Updated values ```x = [0.9639257529687999, 0.8832663930784491]```
- Iteration 7: Updated values ```x = [0.9639275394204873, 0.8832632187713386]```
- Convergence achieved!
- Result: ```x = [0.9639276848248708, 0.8832634216784485]```
- Function values: ```f1(x) = -1.609904987098787e-08```, ```f2(x) = 1.1772563035528094e-08```
