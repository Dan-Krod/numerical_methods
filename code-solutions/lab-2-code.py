def polynom_func(x):
    return x**3 + x - 3

def chord_method(lower_bound, upper_bound, epsilon=1e-5):
    step = 0.1
    f_lower = polynom_func(lower_bound)
    f_upper = polynom_func(upper_bound)

    while f_lower * f_upper > 0:
        if abs(f_upper) > abs(f_lower):
            step = -1 * step
            upper_bound = lower_bound + step
            f_upper = polynom_func(upper_bound)
        
        if f_lower * f_upper > 0:
            lower_bound = upper_bound
            f_lower = polynom_func(lower_bound)

    previous_x = lower_bound
    while True:
        f_lower = polynom_func(lower_bound)
        f_upper = polynom_func(upper_bound)
        
        cur_x = lower_bound - f_lower * (upper_bound - lower_bound) / (f_upper - f_lower)
        f_cur = polynom_func(cur_x)

        if abs(cur_x - previous_x) / abs(cur_x) * 100 < epsilon:
            break  

        if f_cur * f_lower > 0:
            lower_bound = cur_x
        else:
            upper_bound = cur_x
        
        previous_x = cur_x
    
    return cur_x

lower_bound = -2 
upper_bound = 3  
epsilon = 0.0001  

root = chord_method(lower_bound, upper_bound, epsilon)
print(f"Approximate root: {root}")
