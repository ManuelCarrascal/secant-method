import numpy as np

def f(x):
    return np.exp(-x) - x

def secante(f, x0, x1, N=100, emax=0.0001):
    fx0, fx1 = f(x0), f(x1)
    print(f"Iteracion: 0, x0: {x0:.4f}, x1: {x1:.4f}, f(x0): {fx0:.4f}, f(x1): {fx1:.4f}, Error: -")
    for k in range(1, N+1):
        fp = (f(x1) - f(x0)) / (x1 - x0)
        x = x1 - f(x1) / fp
        e = abs((x - x1) / x)
        if e < emax:
            break
        x0, x1 = x1, x
        print(f"Iteracion: {k}, Raiz: {x:.4f}, Error: {e:.4f}")

secante(f, 1, 0)