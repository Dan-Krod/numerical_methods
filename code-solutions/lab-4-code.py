import math

def right_rectangle_method(low_limit, up_limit, intervals, function):
    step = (up_limit - low_limit) / intervals
    integral_val = 0

    cur_x = low_limit + step

    for _ in range(1, intervals + 1):
        integral_val += function(cur_x)
        cur_x += step  

    integral_val *= step
    return integral_val

def integrate_function(x):
    return x * math.exp(3 * x)

def exact_integral(low_limit, up_limit):
    # Первісна F(x) = (e^(3x) * (3x - 1)) / 9
    def primitive(x):
        return (math.exp(3 * x) * (3 * x - 1)) / 9
    
    return primitive(up_limit) - primitive(low_limit)

def main():
    low_limit = 1  
    up_limit = 2  
    intervals = 10000  

    approx_result = right_rectangle_method(low_limit, up_limit, intervals, integrate_function)
    exact_result = exact_integral(low_limit, up_limit)

    print(f"Інтегрування методом правих прямокутників: {approx_result}")
    print(f"Точний результат інтегралу: {exact_result}")
    print(f"Різниця між наближеним та точним результатом при кількості розбитів(n = {intervals}): {abs(exact_result - approx_result)}")

if __name__ == "__main__":
    main()
