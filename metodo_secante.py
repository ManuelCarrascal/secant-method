import sympy as sp

def metodo_secante(self, f, x0, x1, tol, max_iter):
        tabla = []
        iteracion = 0
        x = sp.symbols('x')
        x_vals = []
        f_vals = []
        while iteracion < max_iter:
            f_x0 = sp.N(f.subs(x, x0))
            f_x1 = sp.N(f.subs(x, x1))
            if iteracion == 0:
                xi = f"x0={x0:.4f}, x1={x1:.4f}"
                ea = '-'
                tabla.append(["Iteración", "xi", "F(xi)", "|Ea|"])
                tabla.append([iteracion, xi, "f(x0)={:.4f}, f(x1)={:.4f}".format(f_x0, f_x1), '-'])
            else:
                xi = x1 - (((x0 - x1) * f_x1) / (f_x0 - f_x1))
                if x1 != 0:
                    ea = abs((xi - x1) / x1) * 100
                else:
                    ea = abs(xi - x1) * 100
                tabla.append([iteracion, f"x{iteracion}={xi:.4f}", "f(x{})={:.4f}".format(iteracion, sp.N(f.subs(x, xi))), "{:.4f}".format(ea)])
                x_vals.append(xi)
                f_vals.append(sp.N(f.subs(x, xi)))
                if ea < tol:
                    break
                x0 = x1
                x1 = xi
            iteracion += 1
        return tabla, x_vals, f_vals
