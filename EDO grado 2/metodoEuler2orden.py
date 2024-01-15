#es igual que el método de primer orden, pero se agrega una variable con un CV, formando un vector
#es el mismo problema pero vectorial
import matplotlib.pyplot as plt
import numpy as np

#definicion de puntos iniciales y final
punto_inicial = float(input("Ingrese el punto inicial: "))
u = float(input("Ingrese el valor inicial de u: ")) #u es la y
v = float(input("Ingrese el valor inicial de v: ")) #v es la y'
punto_final = float(input("Ingrese el punto final: "))
n = float(input("Ingrese numero divisiones: ")) #divisiones
h = (punto_final - punto_inicial) / n #paso
puntos = []
puntos_sol = []

#funcion
def f1(x, u, v):
    #donde u = y
    #v = y'
    #f(x) es el termino independiente. despejo y'' de la ecuacion
    N = 0
    return (-1/x)*v - (1 - N**2/x**2)*u

def iteracion(x, u, v, f):
    if x > punto_final:
        return x, u
    x1 = x + h
    u1 = u + h*v    
    v1 = v + h*(f (x, u, v))
    iteracion(x1, u1, v1, f)
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


iteracion(punto_inicial, u, v, f1)
grafica(puntos)
    
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
grafica(puntos)
iteracion_solucion(punto_inicial, solucion1)
grafica(puntos_sol)
puntos_sol = []
iteracion_solucion(punto_inicial, solucion2)
grafica(puntos_sol)
puntos_sol = []
iteracion_solucion(punto_inicial, solucion3)
grafica(puntos_sol)'''