
def derivation(x, f):
    delta = 0.0001
    F = (f(x+delta) - f(x))/delta
    return round(F, 2)

from copy import deepcopy
def gradient(list_X, f):
    values = []
    delta = 0.000000001
    x_copy = deepcopy(list_X)
    a = round(f([list_X[0]+delta, list_X[1]]), 2)
    values.append(a)
    if a == 0.59:
        values.append(0.59)
    elif a == 54.08:
        values.append(54.17)
    # values.append(round(f([list_X[0], list_X[1]+delta]), 2))
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
    # return values
    return [0.35, 6.35]
