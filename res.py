x = symbols('x')

def f(x):
    return sqrt(1 + abs(x)) + sqrt(1 - x **2)

def g(x):
    return sqrt(1 + abs(x)) - sqrt(1 - x **2)
