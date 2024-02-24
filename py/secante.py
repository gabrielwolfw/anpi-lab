import math
import timeit
'''
Aproximación del cero utilizando el método de la secante
Estructura: xk, error, k = secante(x0,x1,func,tol,iterMax)
Paramentros:[x0,x1] = intervalo para la busqueda del cero en la función
            func = función a evaluar con el método de la secante
            tol = tolerancia para la aproximación
            iterMax = iteraciones máximas 

            xk = aproximación del cero
            error = error del método dado por |func(xk)|
            k = iteraciones realizadas

Ejemplo de uso: xk, error, k = secante(2,3,'math.exp(x)-2*x-10',1e-10,1000)
'''
def secante(x0, x1, func, tol, iterMax):
    f = lambda x: eval(func)
    if f(x1) - f(x0) != 0:
        k = 1
        while k < iterMax:
            xk = x1 - ((f(x1) * (x1 - x0))/(f(x1) - f(x0))) # Calculo de la aproximación del cero 

            error = abs(xk - x1) # Calculando la diferencia entre xk y x1 para el error
            if error < tol:
                break
            
            # Actualización de valores x0 y x1
            x0 = x1
            x1 = xk

            k += 1 # Suma de la iteración
        return xk, error, k
 
    else:
        print(f"Los valores {xk} y {x0} no cumplen con el método de la secante")

print("Método de la Secante")
#ejemplo de uso
xk, error, k = secante(2,3,'math.exp(x)-2*x-10',1e-10,1000)
print("\n La aproximación del cero:", xk)
print("\n Error generado:", error)
print("\n Itereaciones realizadas:", k)


# Medidor de tiempo -> Usar la lambda permite medir el tiempo con más precisión
tiempo_ejecucion = timeit.timeit(lambda: secante(2,3,'math.exp(x)-2*x-10',1e-10,1000), number=1)
print("\nTiempo de ejecución:", tiempo_ejecucion, "segundos")