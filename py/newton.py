import timeit
import sympy

'''
Aproximación del cero en la función func utilizando el método Newton-Raphson

Estructura: xk, error, k = newton(x0,func,tol,iterMax)

Paramentros: x0 = valor inicial
            func = función en texto a la que se va aproximar el cero
            tol = tolerancia de la aproximación
            iterMax = iteraciones máximas a realizar
            
            xk = aproximación del cero
            error = error del método dado por |func(xk)|
            k = iteraciones realizadas

Ejemplo de uso: xk, error, k = newton(2.5,'math.exp(x)-2*x-10',1e-10,1000)
'''
def newton(x0, func, tol, iterMax):
    x = sympy.Symbol('x')  # Definir x como un símbolo
    f = eval(func) # Definir el string como una función
    fd = f.diff(x) #Calcular la derivada de la función func

    xk = x0
    k = 1
    while k < iterMax:
        if fd.subs(x, xk) != 0:
            xk = xk - (f.subs(x, xk) / fd.subs(x, xk))
        else:
            print("La derivada de la función no cumple con el método de Newton")

        error = abs(f.subs(x, xk))
        if error < tol:
            break
        k += 1
    return xk, error, k

print("Método de Newton-Raphson \n")
# Ejemplo de uso
xk, error, k = newton(2.5, 'sympy.exp(x)-2*x-10', 1e-10, 1000)
print("\n La aproximación del cero:", xk)
print("\n Error generado:", error)
print("\n Iteraciones realizadas:", k)

# Medidor de tiempo
tiempo_ejecucion = timeit.timeit(lambda: newton(2.5, 'sympy.exp(x)-2*x-10', 1e-10, 1000), number=1)
print("\n Tiempo de ejecución:", tiempo_ejecucion, "segundos")
