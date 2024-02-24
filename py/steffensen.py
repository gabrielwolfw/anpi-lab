
import math
import timeit
'''
Aproximación del cero utilizando el método de la Steffensen
Estructura: xk, error, k = secante(x0,x1,func,tol,iterMax)
Paramentros:[x0,x1] = intervalo para la busqueda del cero en la función
            func = función a evaluar con el método de la secante
            tol = tolerancia para la aproximación
            iterMax = iteraciones máximas 

            xk = aproximación del cero
            error = error del método dado por |func(xk)|
            k = iteraciones realizadas

Ejemplo de uso: xk, error, k = steffensen(2,3,'math.exp(x)-2*x-10',1e-10,1000)
'''
def steffensen(x0, x1, func, tol, iterMax):
    f = lambda x: eval(func)

    if f(x1 + f(x1)) - f(x1) != 0:
        k = 0
        while k < iterMax:
            xk = x1 - ((f(x1)**2)/(f(x1 + f(x1)) - f(x1)))

            error = abs(xk - x1)
            if error < tol:
                break
            # Actualización de valores x1 y x0
            x0 = x1
            x1 = xk

            k += 1
        return xk, error, k
    else:
        print("Hay valores no validos para calcular con el metodo de Steffensen") 

print("Método de Steffensen\n")
xk, error, k = steffensen(2,3,'math.exp(x)-2*x-10',1e-10,1000)
print("\nLa aproximación del cero: ", xk)
print("\nEl eror es: ", error)
print("\nEl total de iteraciones: ", k)

tiempo_ejecucion = timeit.timeit(lambda:steffensen(2,3,'math.exp(x)-2*x-10',1e-10,1000),number=1)
print("\nEl tiempo fue de: ", tiempo_ejecucion, "segundos")