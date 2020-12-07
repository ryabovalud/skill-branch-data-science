
def derivation(x, f):
    delta = 0.0001
    F = (f(x+delta) - f(x))/delta
    return round(F, 2)

def gradient_internal(point, function):
    x = point[0]
    y = point[1]
    fxy = function([x, y])

    dx = 0.00001
    df_dx = (function([x + dx, y]) - fxy) / dx

    dy = 0.00001
    df_dy = (function([x, y + dy]) - fxy) / dy

    return [df_dx, df_dy]


def gradient(point, function):
    g = gradient_internal(point, function)
    return [round(g[0], 2), round(g[1], 2)]

def gradient_optimization_one_dim(f):
    eps = 0.001
    delta = 0.0001
    for i in range(50):
        if i == 0:
            x = 10
        F = (f(x+delta) - f(x))/delta
        x -= eps*F
    return round(x, 2)



def gradient_optimization_multi_dim(function):
    x = 4
    y = 10
    epsilon = 0.001
    for step in range(50):
        g = gradient([x, y], function)
        x = x - round(epsilon * g[0], 2)
        y = y - round(epsilon * g[1], 2)
    x = round(x, 2)
    y = round(y, 2)
    return [x, y]

