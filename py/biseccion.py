import math
import timeit
'''
Aproximación del cero en la función func utilizando el método de la bisección
Estructura: x,xk,k = biseccion(a,b,func,tol,iterMax)
Parametros: a,b = intervalo [a,b] donde se busca el cero 
            func = texto que representa la función a la que se aproxima el cero
            tol = toleranacia de la proximación
            iterMax = iteraciones máximas a realizar

            xk = aproximación del cero
            error = error del metodo dado por |func(xk)|
            k = iteraciones realizadas

Ejemplo de uso: xk, error, k = biseccion(2,3,'math.exp(x)-2*x-10',1e-10,1000)
'''
def biseccion(a,b,func,tol,iterMax):

    f = lambda x: eval(func) # Sustituye la x en la función func

    if f(a)*f(b) > 0: 
        print("No se cumple con el teorema de Bolzano")
    else:
        k = 1
        while k < iterMax:
            xk = (a+b)/2
            if f(a)*f(xk) < 0:
                b = xk
            else: 
                a = xk
            
            error = abs(f(xk))
            if error < tol:
                break
            
            k += 1
        return xk, error, k

print("Método de la Bisección \n")
# Ejemplo de uso
xk, error, k = biseccion(2,3,'math.exp(x)-2*x-10',1e-10,1000)
print("\n La aproximación del cero:", xk)
print("\n Error generado:", error)
print("\n Itereaciones realizadas:", k)

# Medidor de tiempo
tiempo_ejecucion = timeit.timeit(lambda: biseccion(2, 3, 'math.exp(x)-2*x-10', 1e-10, 1000), number=1)
print("\nTiempo de ejecución:", tiempo_ejecucion, "segundos")