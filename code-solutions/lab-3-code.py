from math import sqrt

m = 2  
q = 2  
p = 2  
n = 2 * q - 1  
x_initial = [0.1, 0.1]  

def f1(x1, x2):
    denominator = x1**2 + x2**2
    return (x1 / denominator) + 0.4 - x1

def f2(x1, x2):
    denominator = x1**2 + x2**2
    return (-x2 / denominator) + 1.4 - x2

def f(x1, x2):
    result = [f1(x1, x2), f2(x1, x2)]
    return result

def g1(x1, x2):
    denominator = x1**2 + x2**2
    return (x1 / denominator) + 0.4

def g2(x1, x2):
    denominator = x1**2 + x2**2
    return (-x2 / denominator) + 1.4

def g(x1, x2):
    result = [g1(x1, x2), g2(x1, x2)]
    return result

def e_algo(x_initial, eps):
    x = x_initial[:]

    e = [[[0, 0]] * (n + 1) for _ in range(n + 1)]

    iteration = 0  
    while True:
        iteration += 1  

        print(f"Ітерація {iteration}: Початкові значення x = {x}")
        for j in range(p):
            x = g(x[0], x[1])
        for i in range(2):
            e[0][1][i] = x[i]
        for j in range(0, n):
            x = g(x[0], x[1])
            e[j + 1][1] = x

        cond = (abs((e[1][1][0] - e[0][1][0]) / e[1][1][0]) > eps) and \
            (abs((e[1][1][1] - e[0][1][1]) / e[1][1][1]) > eps)

        if not cond:
            print("Збіжність досягнута!")
            break

        for k in range(1, n):
            for j in range(0, n - k):
                v = [0, 0]
                for i in range(m):
                    v[i] = e[j + 1][k][i] - e[j][k][i]
                summ = sum([v_i * v_i for v_i in v])  
                if summ != 0:
                    for i in range(m):
                        v[i] = v[i] / summ
                    for i in range(m):
                        e[j][k + 1][i] = e[j + 1][k - 1][i] + v[i]
                else:
                    print("Сума компонентів V дорівнює нулю, екстраполяція неможлива.")
                    return None

        for i in range(m):
            x[i] = e[n][1][i]

    return x

result = e_algo(x_initial, 1e-7)

if result:
    print(f"Результат: {result}")
    final_f = f(result[0], result[1])
    print(f"Значення функцій: f1(x) = {final_f[0]}, f2(x) = {final_f[1]}")
