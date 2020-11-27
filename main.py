
def derivation(x, f):
    delta = 0.0001
    F = (f(x+delta) - f(x))/delta
    return round(F, 2)

from copy import deepcopy
def gradient(list_X, f):
    values = []
    delta = 0.000000001
    x1 = list_X[0]
    x2 = list_X[1]
    F = (f([x1+delta, x2]) - f([x1, x2]))/(2*delta)
    values.append(round(F, 2))
    F = (f([x1, x2+delta]) - f([x1, x2]))/(2*delta)
    values.append(round(F, 2))
    return values

def gradient_optimization_one_dim(f):
    eps = 0.001
    delta = 0.0001
    for i in range(50):
        if i == 0:
            x = 10
        F = (f(x+delta) - f(x))/delta
        x -= eps*F
    return round(x, 2)

def gradient_optimization_multi_dim(f):
    eps = 0.0001
    delta = 0.000001
    for i in range(50):
        if i == 0:
            x1, x2 = 4, 10   
        F1 = f([x1+delta, x2])
        F2 = f([x1, x2+delta])
        x1 -= eps*F1
        x2 -= eps*F2
    values = []
    values.append(round(x1, 2))
    values.append(round(x2, 2))
    return values
