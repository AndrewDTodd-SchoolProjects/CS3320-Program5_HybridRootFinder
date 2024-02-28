import numpy as np
import math

#'''
def zero(a, b, f):
    f_a = f(a)
    f_b = f(b)
    
    f_d = 1

    #find c using method of regula falsi
    c = a - ((b - a) / (f_b - f_a)) * f_a
    
    d = 1
    machine_epsilon = np.finfo(float).eps

    f_c = f(c)
    function_evaluations = 3
    loop_iterations = 0

    while True:
        #check c that it wont fall outside the interval, adjust by ulp if needed
        if(c <= a):
            c = a + machine_epsilon * abs(a)
        elif(c >= b):
            c = b - machine_epsilon * abs(b)

        if(np.sign(f_a) == np.sign(f_c)):
            d = a - f_a * (c - a) / (f_c - f_a)
        else:
            d = b - f_b * (c - b) / (f_c - f_b)

        if not a < d < b:
            d = (a + b) / 2

        f_d = f(d)
        function_evaluations += 1

        if(abs(c - d) >= .5 * abs(a - b)):
            d = (a + b) / 2
            f_d = f(d)
            function_evaluations += 1

        if(f_a * f_d < 0):
            b = d
            f_b = f_d
        else:
            a = d
            f_a = f_d

        c = a - ((b - a) / (f_b - f_a)) * f_a

        if(abs(f_d) < machine_epsilon or abs(c - d) < c * machine_epsilon):
            break

        f_c = f(c)
        function_evaluations += 1
        loop_iterations += 1

    return c, function_evaluations, loop_iterations, f_c
#'''
'''
def zero(a, b, f):
    epsilon = np.finfo(float).eps  # System epsilon

    f_a, f_b = f(a), f(b)
    function_evaluations = 2

    loop_iterations = 0

    if np.sign(f(a)) == np.sign(f(b)):
        return None  # No sign change in the interval [a, b]
    
    while abs(b - a) > max(a, b) * epsilon:  # Convergence criterion
        # False Position
        c = b - f_b * (b - a) / (f_b - f_a)

        #check c that it wont fall outside the interval, adjust by ulp if needed
        if(c <= a):
            c = a + epsilon * abs(a)
        elif(c >= b):
            c = b - epsilon * abs(b)

        f_c = f(c)
        function_evaluations += 1
        
        # Secant Search
        if np.sign(f_a) == np.sign(f_c):
            d = a - f(a) * (a - c) / (f_a - f_c)
        else:
            d = b - f(b) * (b - c) / (f_b - f_c)
        
        # Check if d falls outside of the interval [a, b]
        if d <= a or d >= b:
            # Bisection
            d = (a + b) / 2

        f_d = f(d)
        function_evaluations += 1
        
        # Update the interval
        if np.sign(f_c) != np.sign(f_d):
            a, b = c, d
            f_a, f_b = f_c, f_d
        else:
            a, b = d, c
            f_a, f_b = f_d, f_c
        
        # If the length of [c,d] is not less than half of [a,b], then do a bisection step
        if abs(b - a) >= abs(c - d) / 2:
            d = (a + b) / 2

        loop_iterations += 1
    
    return (a + b) / 2, function_evaluations, loop_iterations, f_c
'''
    

def TestOneFunc(x):
    return x * math.cos(x) + math.sin(x)

def TestTwoFunc(x):
    return (math.e ** (-x)) - x

if __name__ == '__main__':
    TestOneFunc_root1, functionEval, iter, f_c = zero(2, 3, TestOneFunc)
    print(f"First positive root of first function: {TestOneFunc_root1}")
    print(f"Took {functionEval} function evaluations")
    print(f"With {iter} iterations of the loop")
    print(f"Function evaluates to {f_c} at produced root")
    print()

    TestOneFunc_root2, functionEval, iter, f_c = zero(4, 5, TestOneFunc)
    print(f"Second positive root of first function: {TestOneFunc_root2}")
    print(f"Took {functionEval} function evaluations")
    print(f"With {iter} iterations of the loop")
    print(f"Function evaluates to {f_c} at produced root")
    print()

    TestTwoFunc_root1, functionEval, iter, f_c = zero(0, 1, TestTwoFunc)
    print(f"Positive root of second function: {TestTwoFunc_root1}")
    print(f"Took {functionEval} function evaluations")
    print(f"With {iter} iterations of the loop")
    print(f"Function evaluates to {f_c} at produced root")
    print()