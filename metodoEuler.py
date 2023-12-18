import matplotlib.pyplot as plt
import numpy as np

#definicion de puntos iniciales y final
punto_inicial = float(input("Ingrese el punto inicial: ")) 
y0 = float(input("Ingrese el valor de y0: "))
punto_final = float(input("Ingrese el punto final: "))
n = float(input("Ingrese numero divisiones: ")) #divisiones
h = (punto_final - punto_inicial) / n #paso
puntos = []
puntos_sol = []
#funcion 1
def f1(x, y):
    return (-2*x*(np.exp(x**2)*y-1)/np.exp(x**2))

def iteracion(x, y, f):
    if x > punto_final:
        return x, y
    x1 = x + h
    y1 =y + h*f(x, y)
    iteracion(x1, y1, f)
    puntos.append((x1, y1))
    print(x1, y1)
    return x1, y1

def grafica(puntos):
    x = []
    y = []
    for i in puntos:
        x.append(i[0])
        y.append(i[1])
    plt.plot(x, y)
    plt.show()
    

#Funcion para iterar con la solucion particular
def iteracion_solucion(x, f):
    while x <= punto_final:
        x1 = x + h
        y1 =h*f(x)
        iteracion_solucion(x1, f)
        puntos_sol.append((x1, y1))
        print(x1, y1)
        return x1, y1
    
#Funciones particulares con la C calculada. cambio la C según el valor inicial
def solucion(x):
    return ((x**2)/np.exp(x**2))



iteracion(punto_inicial, y0, f1)
grafica(puntos)
iteracion_solucion(punto_inicial, solucion)
grafica(puntos_sol)
