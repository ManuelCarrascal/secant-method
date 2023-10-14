import sympy as sp

def metodo_secante(self, f, x0, x1, tol, max_iter):
    """
    Implementa el método de la secante para encontrar una raíz de una función f(x).

    Args:
        f (sympy expression): Función a la que se le busca la raíz.
        x0 (float): Primer valor inicial.
        x1 (float): Segundo valor inicial.
        tol (float): Tolerancia para el error absoluto.
        max_iter (int): Número máximo de iteraciones.

    Returns:
        tuple: Una tupla que contiene:
            - Una lista con la tabla de iteraciones.
            - Una lista con los valores de x obtenidos en cada iteración.
            - Una lista con los valores de f(x) obtenidos en cada iteración.
    """
    tabla = []  # Lista para almacenar la tabla de iteraciones.
    iteracion = 0  # Contador de iteraciones.
    x = sp.symbols('x')  # Símbolo x para usar en la función.
    x_vals = []  # Lista para almacenar los valores de x obtenidos en cada iteración.
    f_vals = []  # Lista para almacenar los valores de f(x) obtenidos en cada iteración.
    while iteracion < max_iter:
        f_x0 = sp.N(f.subs(x, x0))  # Evalúa f(x) en x0.
        f_x1 = sp.N(f.subs(x, x1))  # Evalúa f(x) en x1.
        if iteracion == 0:
            xi = f"x0={x0:.4f}, x1={x1:.4f}"
            ea = '-'
            tabla.append(["Iteración", "xi", "F(xi)", "|Ea|"])
            tabla.append([iteracion, xi, "f(x0)={:.4f}, f(x1)={:.4f}".format(f_x0, f_x1), '-'])
        else:
            xi = x1 - (((x0 - x1) * f_x1) / (f_x0 - f_x1))  # Calcula el siguiente valor de x.
            if x1 != 0:
                ea = abs((xi - x1) / x1) * 100  # Calcula el error absoluto.
            else:
                ea = abs(xi - x1) * 100
            tabla.append([iteracion, f"x{iteracion}={xi:.4f}", "f(x{})={:.4f}".format(iteracion, sp.N(f.subs(x, xi))), "{:.4f}".format(ea)])
            x_vals.append(xi)
            f_vals.append(sp.N(f.subs(x, xi)))
            if ea < tol:  # Si el error absoluto es menor que la tolerancia, se detiene el método.
                break
            x0 = x1  # Actualiza los valores de x.
            x1 = xi
        iteracion += 1
    return tabla, x_vals, f_vals
