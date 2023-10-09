import sympy as sp

# Función que implementa el método de la secante
def metodo_secante(f, x0, x1, tol, max_iter):
    tabla = []
    iteracion = 0
    x = sp.symbols('x')

    while iteracion < max_iter:
        f_x0 = sp.N(f.subs(x, x0))
        f_x1 = sp.N(f.subs(x, x1))

        if iteracion == 0:
            xi = x1  # En la primera iteración, xi es igual a x1
            ea = '-'  # No se calcula el error en la primera iteración
            tabla.append(["Número iteraciones", "xi", "F(xi)", "|Ea|"])
            tabla.append([iteracion, "x0={:.4f}".format(x0), "f(x0)={:.4f}".format(f_x0), '-'])
        else:
            xi = x1 - (((x0 - x1) * f_x1) / (f_x0 - f_x1))
            ea = abs((xi - x0) / xi) * 100  # Cálculo del error porcentual corregido

            tabla.append([iteracion, "x{}={:.4f}".format(iteracion, xi), "f(x{})={:.4f}".format(iteracion, f_x1), "{:.4f}".format(ea)])

            if ea < tol:
                break

            x0 = x1
            x1 = xi

        iteracion += 1

    return tabla

# Solicitar entrada de usuario para la función
expresion = input("Ingrese la función f(x) (por ejemplo, x**3 - x - 2): ")
x = sp.symbols('x')
f = sp.sympify(expresion)

# Solicitar entrada de usuario para otros parámetros
x0 = float(input("Ingrese el valor de x0: "))
x1 = float(input("Ingrese el valor de x1: "))
tol = float(input("Ingrese el porcentaje de error deseado (%): "))
max_iter = 50  # Máximo de 50 iteraciones, como se requiere

# Calcular la tabla usando el método de la secante
tabla_secante = metodo_secante(f, x0, x1, tol, max_iter)

# Imprimir la tabla con etiquetas adecuadas
for fila in tabla_secante:
    print("{:<20} {:<20} {:<20} {:<20}".format(*fila))
