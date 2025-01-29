# Numerical Integration Methods for Definite Integrals

### Objective
To study the primary methods for calculating definite integrals.

### Theoretical Information

1. **Overview of Definite Integral Calculation:**
The problem of finding a definite integral often arises in practice when solving scientific and technical problems. The function ```f(x)``` is continuous on the interval ```[a, b]```. The lower limit ```a``` is less than the upper limit ```b```. When ```a = b```, the integral equals zero. The exact value of the definite integral is calculated using the Newton-Leibniz formula:
```
∫[a, b] f(x) dx = F(b) - F(a)
```
where ```F``` is the antiderivative of the function ```f(x)```. However, this formula is not always applicable due to the following reasons:
- The function ```f(x)``` cannot be integrated directly, i.e., its antiderivative cannot be expressed in terms of elementary functions.
- The values of the function ```f(x)``` for the given interval are provided in tabular form. In such cases, approximate methods are used to calculate the definite integral.

2. **Analytical Methods**
The idea behind analytical methods is to replace the integrand function ```f(x)``` on the interval ```([a, b]``` with a certain analytically defined function ```p(x)```, whose antiderivative can be easily found. For instance, if the function ```f(x)``` can be expanded into a Taylor series or a trigonometric series on the interval ```[a, b]```, then the partial sum of this series can be used as ```p(x)```. The desired integral of this function is easily calculated since it is either a polynomial or a linear combination of ```sin(kx)``` and ```cos(kx)```.

3. **Numerical Methods**
According to Riemann's definition (1826-1866, a famous German mathematician), the definite integral is considered as the limit of the integral sum when the interval of partition tends to zero. In geometric terms, the Riemann integral sum equals the area of the curvilinear figure bounded by the curve ```y = f(x) ```, the lines ```x = a``` and ```x = b```, ```x(-axis)```. Based on the Riemann integral sum, the main numerical methods for calculating definite integrals are developed. By omitting the limit sign ```lim```, we obtain the quadrature formula
    ```
    ∫[a, b] f(x) dx ≈ Σ(α_i * f(x_i))
    ```
    where ```f(x_i)``` is the value of the function at the interpolation nodes ```x_i```, ```α_i``` are numerical coefficients (weights of the quadrature formula), and the right-hand side of the formula is the quadrature sum. Different numerical integration methods (quadrature formulas) are obtained depending on the method of calculation—rectangular, trapezoidal, parabolic, spline methods, etc.

4. **Method of Rectangles**
In this simplest case, the small curvilinear figures are replaced by ordinary rectangles with a base ```h = (b - a) / n``` (where ```n``` is the number of partitions) and a height equal to the function value at the point ```x_i```. We calculate the sum of the areas of these rectangles.

---
## Task #6: Method of Right Rectangles with n = 30

### Algorithm

1. **Initialization**: 
    - Set the values of the lower and upper integration limits ```a``` and ```b```, and the number of partitions ```n```.
2. **Calculate Step Size**: 
    - Compute the step size ```h``` for moving across the interval. The initial value for ```x``` is the first point after the lower limit since we use the method of right rectangles.
3. **Integration Loop**: 
    - In a loop, for each step, add the function value at the current point to the sum. After each iteration, increase the value of ```x``` by the calculated step.
4. **Obtain Approximate Integral**: 
    - After the loop, multiply the accumulated sum by the step size to obtain the approximate value of the integral.
5. **Verification**: 
    - Calculate the exact value of the integral using the Newton-Leibniz formula for verification.

### Recommendations for Implementation
1. Set the initial conditions appropriately.
2. Use a numeric library like NumPy for precise mathematical operations.
3. Ensure proper handling of interval boundaries and convergence checks.

### Input Data
The input data will be:
- **Integration Function**:
```python
def function_to_integrate(x):
    return x * math.exp(3 * x)
```
- **Limits**:
```python
low_limit = 1
up_limit = 2
intervals = 30
```
- **Antiderivative Function**:
```python
def antiderivative(x):
    return (math.exp(3 * x) * (3 * x - 1)) / 9
```
> **⚠️ Note:** More detailed input data can be found in the `input_data` folder, specifically in the `input_data(lab-4)` file.

### Expected Output
- Integral using the right rectangles method: ```233.03051072877489```
- Exact integral result: ```219.6636548463667```
- Difference between the approximate and exact result ```for (n = 30): 13.366855882408174```
