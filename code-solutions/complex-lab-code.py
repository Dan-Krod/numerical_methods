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

def u1(t):
    return u1_amp if (t % T) < a else 0

def L1(i1):
    if abs(i1) <= i_min:
        return L_max
    elif abs(i1) >= i_max:
        return L_min
    else:
        x = np.array([0, i_min, (i_min + i_max) / 2, i_max, 3])
        y = np.array([L_max, L_max, (L_max + L_min) / 2, L_min, L_min])
        spline = CubicSpline(x, y, bc_type='natural')
        return spline(abs(i1))

def derivatives(t, y):
    i1, i2, u_C1 = y
    L1_val = L1(i1)
    di1_dt = (u1(t) - R1 * i1 - u_C1) / L1_val
    di2_dt = (u_C1 - R2 * i2) / L2
    du_C1_dt = (i1 - i2 - u_C1 / R3 - u_C1 / R4) / C1
    return np.array([di1_dt, di2_dt, du_C1_dt])

def runge_kutta_step(x, y, h):
    K1 = h * derivatives(x, y)
    K2 = h * derivatives(x + 0.5 * h, y + 0.5 * K1)
    K3 = h * derivatives(x + h, y + 2 * K2 - K1)
    return y + (K1 + 4 * K2 + K3) / 6

dt = T / 400 
time_steps = int(5 * T / dt)  
time = np.linspace(0, 5 * T, time_steps)
results = []
y = np.array([0, 0, 0]) 

for t in time:
    u2 = y[1] * R4  
    results.append([t, *y, u1(t), u2])
    y = runge_kutta_step(t, y, dt)

results = np.array(results)
t_vals = results[:, 0]
i1_vals = results[:, 1]
i2_vals = results[:, 2]
u_C1_vals = results[:, 3]
u1_vals = results[:, 4]
u2_vals = results[:, 5]

fig1, axs1 = plt.subplots(2, 1, figsize=(10, 8))
fig1.suptitle("Результати моделювання (Сторінка 1)")

i_values = np.linspace(0, 3, 100) 
L1_values = [L1(i) for i in i_values]
axs1[0].plot(i_values, L1_values, color='blue', label="L1(i)")
axs1[0].axhline(y=L_max, color='purple', linestyle='--', label="L_max")
axs1[0].axhline(y=L_min, color='purple', linestyle='--', label="L_min")
axs1[0].axvline(x=i_min, color='orange', linestyle='--', label="i_min")
axs1[0].axvline(x=i_max, color='orange', linestyle='--', label="i_max")
axs1[0].set_xlabel("Струм i (A)")
axs1[0].set_ylabel("Індуктивність L1 (H)")
axs1[0].set_title("Залежність індуктивності L1 від струму i")
axs1[0].grid()
axs1[0].legend()

axs1[1].plot(t_vals, i1_vals, color='black', label="i1 (Струм через L1)")
axs1[1].plot(t_vals, i2_vals, color='red', label="i2 (Струм через L2)")
axs1[1].set_xlabel("Час (с)")
axs1[1].set_ylabel("Струм (А)")
axs1[1].set_title("Часові залежності струмів через індуктивності")
axs1[1].grid()
axs1[1].legend()

plt.tight_layout()

fig2, axs2 = plt.subplots(2, 1, figsize=(10, 8))
fig2.suptitle("Результати моделювання (Сторінка 2)")

axs2[0].plot(t_vals, u_C1_vals, color='green', label="u_C1 (Напруга на C1)")
axs2[0].set_xlabel("Час (с)")
axs2[0].set_ylabel("Напруга (В)")
axs2[0].set_title("Напруга на конденсаторі C1")
axs2[0].grid()
axs2[0].legend()

axs2[1].plot(t_vals, u1_vals, color='blue', label="u1 (Вхідна напруга)")
axs2[1].set_xlabel("Час (с)")
axs2[1].set_ylabel("Напруга (В)")
axs2[1].set_title("Вхідна напруга u1")
axs2[1].grid()
axs2[1].legend()

plt.tight_layout()

fig3, ax3 = plt.subplots(figsize=(10, 4))
fig3.suptitle("Результати моделювання (Сторінка 3)")

ax3.plot(t_vals, u2_vals, color='red', label="u2 (Вихідна напруга)")
ax3.set_xlabel("Час (с)")
ax3.set_ylabel("Напруга (В)")
ax3.set_title("Вихідна напруга u2")
ax3.grid()
ax3.legend()

plt.tight_layout()

plt.show()
