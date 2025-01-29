# Analysis of Dynamic Processes in Nonlinear Compensating Circuits of Control Systems

### Objective
To study and analyze the dynamic processes in nonlinear compensating circuits of control systems using numerical methods for solving differential equations, particularly the Runge-Kutta method. To apply these methods to model a nonlinear RLC circuit considering the inductance changes depending on the current and obtain time dependencies of voltage and currents. To visualize the results and draw conclusions about the efficiency and accuracy of the selected integration method.

### Theoretical Information

1. **Introduction:**
In engineering practice, it is often necessary to deal with technical systems and technological processes whose characteristics change continuously over time. Such phenomena are typically described by differential equations. An ordinary differential equation has an infinite set of solutions. To find a specific solution, additional conditions are required. When the additional conditions are given for a single value of the independent variable, it is a Cauchy problem. If the additional conditions are given for two or more values of the independent variable, it is a boundary value problem. In the Cauchy problem, the additional conditions are called initial, and in the boundary problem, they are boundary conditions.

2. **Cauchy Problem:**
Let us formulate the Cauchy problem. Given a differential equation and an initial condition ```x(t₀) = x₀```, it is required to determine the function ```x(t)``` on the interval ```t ∈ [0, tₖ]``` that satisfies the equation and the initial condition.

    Methods for solving the Cauchy problem can be divided into two groups: explicit and implicit. Each group is further divided into single-step methods, where the next point ```x(t₀ + h)``` requires information from only one previous step ```x(t₀)``` (e.g., Euler's method and Runge-Kutta methods), and multistep methods (prediction and correction), where finding the next point ```x(t₀ + h)``` requires information from more than one previous point (e.g., Adams, Milne, Hamming methods). These are numerical methods for solving differential equations, providing the solution in the form of a table of values.
    These methods can be applied to solve systems of nonlinear differential equations. They are also suitable for solving higher-order equations because a differential equation of order ```n``` can always be reduced to a system of ```n``` first-order differential equations.

3. **Runge-Kutta Methods for Systems of Ordinary Differential Equations:**
The Runge-Kutta methods comprise a family of numerical methods for solving first-order differential equations. The most commonly used method is the fourth-order Runge-Kutta method (known as "the Runge-Kutta method"). Other modifications of this method are provided below.

---

## Task #6: Runge-Kutta Method for Nonlinear RLC Circuit

Formulate a system of algebraic-differential equations and calculate the transient process of the circuit using the given method. Plot the graph of the transient process of the output voltage ```U₂```.

### Explanation of the Algorithm

1. **Initialization**:
    - Set initial values for the lower and upper integration limits and the number of partitions.
    - Set initial conditions:
        - Maximum voltage ```U_max = 100 V```, signal frequency ```f = 50 Hz```, component parameters: ```R₁ = 4 Ω```, ```R₂ = 12 Ω```, ```R₃ = 230 Ω```, ```R₄ = 40 Ω```, ```L₁ = 0.42 H```, and ```C₁ = 0.24 × 10⁻³ F```.
        - Set maximum simulation time ```t_max = 0.2 s``` and integration step ```h = 0.00001 s```.
        - Initialize time grid and arrays:
            - Create time array ```t```, containing time values from 0 to ```t_max``` with step ```h```.
            - Initialize zero arrays for currents ```i₁``` (current through ```L₁```), ```i₂``` (current through ```R₂``` and ```R₃```), and voltage ```U₂``` (output voltage across ```R₃```).

2. **Calculate Step Size**:
    - Compute the step size ```h``` for moving across the interval. The initial value for ```x``` is the first point after the lower limit since we use the method of right rectangles.

3. **Integration Loop Using Runge-Kutta Method**:
    - In a loop, for each step, add the function value at the current point to the sum. After each iteration, increase the value of ```x``` by the calculated step.
    - Compute currents and voltages starting from the second element of the array ```i = 1``` using the Runge-Kutta method for each time step:
        1) Update current through ```L₁```:
        ``` 
        i₁[i] = i₁[i-1] + h * ((U₁[i-1] - R₁ * i₁[i-1] - U₂[i-1]) / L₁)
        ```
        2) Update voltage across capacitor ```C₁```:
        ``` 
        U₂[i] = U₂[i-1] + h * ((i₁[i-1] - i₂[i-1]) / C₁)
        ```
        3) Update current through ```R₂``` and ```R₃```:
        ``` 
        i₂[i] = i₂[i-1] + h * (U₂[i-1] / (R₂ + R₃))
        ```

4. **Obtain Approximate Integral**:
    - After the loop, multiply the accumulated sum by the step size to obtain the approximate value of the integral.

5. **Verification and Visualization**:
    - Calculate the exact value of the integral using the Newton-Leibniz formula for verification.
    - Plot the transient process graph:
        - After the calculation loop, plot the graph of voltage ```U₂``` versus time, showing the transient process of the output voltage across ```R₃```.
    - Display the graph showing the change in output voltage ```U₂``` over time, demonstrating the transient process in the circuit.


### Recommendations for Implementation
1. Set the initial conditions appropriately.
2. Use a numeric library like NumPy for precise mathematical operations.
3. Ensure proper handling of interval boundaries and convergence checks.

### Input Data
The input data will be:
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

C1 = 0.24e-3
L_max = 13
L_min = 1.3
L2 = 0.42
R1 = 4
R2 = 12
R3 = 230
R4 = 40
i_min = 1
i_max = 2
a = 0.009
T = 2 * a
u1_amp = 10
```
> **⚠️ Note:** More detailed input data can be found in the `input_date` folder, specifically in the `input_date(lab-6)` file.

### Expected Output  
The output data consists of generated **graphs** based on the input parameters.  
> **⚠️ Note:** More detailed output data and graphs can be found in the `output_data` folder, specifically in the `output_data(1)/(2)/(3)(lab-6)` file.  
