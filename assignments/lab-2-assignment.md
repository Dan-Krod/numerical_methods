# Methods for refining the roots of nonlinear equations

### Objective
Study the primary methods for refining the roots of nonlinear equations with one variable.

### Theoretical Information

1. **Overview of Nonlinear Equation Root Finding:**
   The problem of finding the roots of a nonlinear equation with one variable ```f(x) = 0``` often arises in practice as a basic step in solving scientific and technical problems. At first glance, it appears simple, but finding an exact solution is possible only when ```f(x)``` is a polynomial of degree ```n <= 4```. Finding the exact solution involves a specific procedure to compute the root based on the equation parameters (e.g., for the equation ```ax^2 + bx + c = 0)```. The root (solution) of the equation is the value of x for which ```f(x) = 0```. A root x is called a simple root if ```f'(x) ≠ 0```. Otherwise, if ```f'(x) = 0```, the root x is called a multiple root.

2. **Main Stages of Solving:**
The problem of finding the root of a nonlinear equation is solved in three stages:
    - Localization of the root or selection of the initial approximation x0.
    - Iterative refinement of the root.
    - Checking the convergence condition of the iterative process.

3. **Chord Method**
In literature, this method is also known as the false position method, linear interpolation method, and the method of proportional parts. Given an interval ```[a, b]``` where the root x is localized, and ```f(a) * f(b) < 0```, the idea of the chord method is to approximate the curve ```y = f(x)``` over the small interval ```[a, b]``` with a chord. The approximate root x is taken as the point of intersection of the chord with the Ox-axis. The chord equation AB is:
    ```
    (y - f(b)) / (f(b) - f(a)) = (x - a) / (b - a)
    ```
    At the intersection with the Ox-axis, y = 0, and x = x0. Rewriting the equation gives:
    ```
    x0 = a - (f(a) * (b - a)) / (f(b) - f(a))
    ```
    Next, we compute the function value ```f(x0)```. If ```f(a) * f(x0) < 0```, we discard the interval ```[x0, b]```, otherwise, we discard the interval ```[a, x0]```. This is implemented by assigning the value of x0 to either a or b. We then build a new chord and find its intersection with the Ox-axis according to the equation:
    ```
    xk = ak - (f(ak) * (bk - ak)) / (f(bk) - f(ak))
    ```
    The iterative process stops when the condition of proximity between two successive approximations is met:
    ```
    | xk - x(k-1) | < ε
    ```
---
## Task #6: Chord Method with Root Localization Search for ```x ∈ [-2, 3]```

### Algorithm

1. Initialization:
    - Setting initial values for lower bound (lower_bound), upper bound (upper_bound), and the allowable error (epsilon).
    - Defining the function whose root needs to be found: ```polynom_func(x) = x³ + x - 3```.
    - Initially calculating the function values at the lower and upper bounds: ```f_lower = polynom_func(lower_bound) and f_upper = polynom_func(upper_bound)```.

2. Checking Initial Interval Boundaries:
    - If the function values at the lower and upper bounds have the same sign (i.e., their product is greater than zero), a root between these points is not guaranteed.
    - Correcting the interval boundaries: ```if f_lower * f_upper > 0```, the boundaries are adjusted: if the absolute value of the function at the upper bound is greater than at the lower bound, a step is taken to search for the root. The boundaries are shifted until an interval is found where the function values at the lower and upper bounds have opposite signs.

3. Main Part: Chord Method:
    - Root-finding loop: after identifying the interval where a root is possible, the algorithm starts computing new approximations of the root using the chord method.
    - Formula for calculating the new point:
   
    ```
    cur_x = lower_bound - f_lower * ((upper_bound - lower_bound) / (f_upper - f_lower))
    ```
   Here, cur_x is the new approximate point located on the chord between the lower and upper bounds.

4. Checking Convergence:
    - Checking if the solution accuracy has been achieved by comparing the change between the previous and current points (previous_x and cur_x). If the relative change is less than epsilon, the algorithm stops.

5. Updating Interval Boundaries:
    - If the function value at the new point cur_x has the same sign as at the lower bound, lower_bound is updated to cur_x. If the function value at cur_x has the opposite sign to that at the lower bound, the upper bound is updated to cur_x. The process repeats until the desired accuracy is achieved.

6. Completing the Algorithm:
    - When the stopping condition is met, and the relative error becomes less than epsilon, the computed value cur_x is accepted as the root of the equation. The found root is returned.

### Recommendations for Implementation
1. Set the initial conditions appropriately.
2. Use a numeric library like NumPy for precise mathematical operations.
3. Ensure proper handling of interval boundaries and convergence checks.


### Input Data:
The input data is as follows:
- ```lower_bound = -2```
- ```upper_bound = 3```
- ```epsilon = 0.0001```

#### Function Definition:
```python
def f(x):
    return x**3 + x - 3
```
> **⚠️ Note:** More detailed input data can be found in the `input_data` folder, specifically in the `input_data(lab-2)` file.

### Expected Output:
The found root is approximately: ```1.2134101046643253```
