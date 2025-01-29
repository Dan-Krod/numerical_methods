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
omega = 2 * np.pi * f

t = np.arange(0, t_max, h)

U1 = U_max * np.sin(omega * t)

I1 = np.zeros_like(t)  
I2 = np.zeros_like(t)  
U2 = np.zeros_like(t) 

for i in range(1, len(t)):
    dI1_dt = (U1[i-1] - I1[i-1] * R1 - U2[i-1]) / L1
    I1[i] = I1[i-1] + h * dI1_dt 

    dU2_dt = (I1[i-1] - I2[i-1]) / C1
    U2[i] = U2[i-1] + h * dU2_dt  

    dI2_dt = U2[i-1] / (R2 + R3)
    I2[i] = I2[i-1] + h * dI2_dt  

plt.figure(figsize=(10, 6))
plt.plot(t, U2, label="Output Voltage U2 (V)", color="b")
plt.title("Transient Response of the Output Voltage U2")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.legend()
plt.show()
