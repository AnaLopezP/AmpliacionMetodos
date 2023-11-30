#es igual que el método de primer orden, pero se agrega una variable con un CV, formando un vector
#es el mismo problema pero vectorial
import matplotlib.pyplot as plt
import numpy as np

#definicion de puntos iniciales y final
punto_inicial = float(input("Ingrese el punto inicial: "))
u = float(input("Ingrese el valor inicial de u: "))
v = float(input("Ingrese el valor inicial de v: "))
punto_final = float(input("Ingrese el punto final: "))
n = float(input("Ingrese numero divisiones: ")) #divisiones
h = (punto_final - punto_inicial) / n #paso
puntos = []
puntos_sol = []

#funcion
def f1(x, y):
    return (-2*x*(np.exp(x**2)*y-1)/np.exp(x**2))

def iteracion(x, u, v, a, b, f):
    while x <= punto_final:
        x1 = x + h
        u1 = u + h*v
        v1 = v + h*(-b* u - a*v + f(x))
        iteracion(x1, u1, v1, a, b, f)
        puntos.append((x1, u1))
        print(x1, u1)
        return x1, u1

def grafica(puntos):
    x = []
    y = []
    for i in puntos:
        x.append(i[0])
        y.append(i[1])
    plt.plot(x, y)
    plt.show()
    
    
'''def iteracion_solucion(x, f):
    while x <= punto_final:
        x1 = x + h
        y1 =h*f(x)
        iteracion_solucion(x1, f)
        puntos_sol.append((x1, y1))
        print(x1, y1)
        return x1, y1'''
    
'''def solucion1(x):
    return ((x**2)/np.exp(x**2))

def solucion2(x):
    return ((1 + x**2)/np.exp(x**2))

def solucion3(x):
    return (-1 + (x**2)/np.exp(x**2))'''

'''
iteracion(punto_inicial, y0, f1)
grafica(puntos)
iteracion_solucion(punto_inicial, solucion1)
grafica(puntos_sol)
puntos_sol = []
iteracion_solucion(punto_inicial, solucion2)
grafica(puntos_sol)
puntos_sol = []
iteracion_solucion(punto_inicial, solucion3)
grafica(puntos_sol)'''