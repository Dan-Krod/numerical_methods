# Integration of Systems of Differential Equations. Calculation of Transient Processes for RLC Circuits

### Objective
To study the primary methods for solving systems of first-order differential equations.

### Theoretical Information

1. **Overview of Differential Equation Solving**
The task involves solving systems of first-order differential equations. Euler's explicit method is one of the simplest methods for solving such problems.

2. **Euler's Explicit Method**
One-step methods are designed to solve first-order differential equations of the form:
```
dx_i / dt = f(x_i, t)
```
Euler's method is the simplest method for solving the Cauchy problem. It allows integrating first-order differential equations. Its accuracy is limited. The step ```h``` is so small that the function ```y``` differs little from a linear function. This means that the curve is replaced by tangents, and movement occurs along segments of the tangent, not the integral curve. Euler's method is based on expanding the function ```x``` in a Taylor series around the point ```t_0```. If ```h``` is small, the terms containing ```h^2```, ```h^3```, etc., are small and can be neglected. The derivative ```x'(t_0)``` is found from the equation by substituting the initial condition. This allows approximating the value of the dependent variable with a small shift ```h``` from the initial point. For a system of differential equations, Euler's explicit method is written as:
```
dx_i / dt = f(x_i, t)
```
The error of the method is of the order of ```h^2```, since terms containing ```h``` in the second and higher powers are discarded. A disadvantage of Euler's method is the accumulation of errors and the increase in computation volumes when choosing a small step ```h``` to ensure the required accuracy.

---
## Task #6: Euler's Explicit Method for an RLC Circuit
Formulate a system of differential equations and calculate the transient process of the circuit using the given method. Plot the graph of the transient process of the output voltage ```U_2```.

### Explanation of the Algorithm

1. **Initialization**:
    - Set initial values for the lower and upper integration limits ```a``` and ```b```, and the number of partitions ```n```.
    - Set initial conditions:
        - Maximum voltage ```U_max = 100V```, signal frequency ```f = 50Hz```, component parameters: ```R_1 = 5Ω```, ```R_2 = 4Ω```, ```R_3 = 7Ω```, ```L_1 = 0.01H```, and ```C_1 = 300 * 10^{-6} F```.
        - Set maximum simulation time ```t_max = 0.2s``` and integration step ```h = 0.00001s```.
        - Declare angular frequency ```ω = 2πf```.
    - Initialize time grid and arrays:
        - Create time array ```t```, containing time values from 0 to ```t_max``` with step ```h```.
        - Initialize zero arrays for currents ```I_1``` (current through ```L_1```), ```I_2``` (current through ```R_2``` and ```R_3```), and voltage ```U_2``` (output voltage across ```R_3```).

2. **Calculate Step Size**:
    - Compute the step size ```h``` for moving across the interval. The initial value for ```x``` is the first point after the lower limit since we use the method of right rectangles.

3. **Integration Loop Using Euler's Method**:
    - In a loop, for each step, add the function value at the current point to the sum. After each iteration, increase the value of ```x``` by the calculated step.
    - Compute currents and voltages starting from the second element of the array ```(i = 1)``` using Euler's method for each time step:
        1) Update current through ```L_1``` (```I_1```):
        ```I_1[i] = I_1[i-1] + h * (U_1[i-1] - I_1[i-1] * R_1 - U_2[i-1]) / L_1```
        2) Update voltage across capacitor ```C_1``` (```U_2```):
        ```U_2[i] = U_2[i-1] + h * (I_1[i-1] - I_2[i-1]) / C_1```
        3) Update current through ```R_2``` and ```R_3``` (```I_2```):
        ```I_2[i] = I_2[i-1] + h * U_2[i-1] / (R_2 + R_3)```

4. **Obtain Approximate Integral**:
    - After the loop, multiply the accumulated sum by the step size to obtain the approximate value of the integral.

5. **Verification and Visualization**:
    - Calculate the exact value of the integral using the Newton-Leibniz formula for verification.
    - Plot the transient process graph:
        - After the calculation loop, plot the graph of voltage ```U_2``` versus time, showing the transient process of the output voltage across ```R_3```.
    - Display the graph showing the change in output voltage ```U_2``` over time, demonstrating the transient process in the circuit.

### Recommendations for Implementation
1. Set the initial conditions appropriately.
2. Use a numeric library like NumPy for precise mathematical operations.
3. Ensure proper handling of interval boundaries and convergence checks.

### Input Data
The input data will be:
```python
import numpy as np
import matplotlib.pyplot as plt

U_max = 100  
f = 50  
R1 = 5  
R2 = 4  
R3 = 7  
L1 = 0.01  
C1 = 300e-6  
t_max = 0.2  
h = 0.00001  
```
> **⚠️ Note:** More detailed input data can be found in the `input_date` folder, specifically in the `input_date(lab-5)` file.

### Expected Output  
The output data consists of generated **graphs** based on the input parameters.  
> **⚠️ Note:** More detailed output data and graphs can be found in the `output_data` folder, specifically in the `output_data(lab-5)` file.  
