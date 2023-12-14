import matplotlib.pyplot as plt
import numpy as np
#definicion de puntos iniciales y final
punto_inicial = float(input("Ingrese el punto inicial: "))
y0 = float(input("Ingrese el valor de y0: "))
punto_final = float(input("Ingrese el punto final: "))
n = float(input("Ingrese numero divisiones: ")) #divisiones
h = (punto_final - punto_inicial) / n #paso
puntos = []

#funcion 1
def f1(x, y):
    return (2-3*x-y)/(x-1)

def derf1(x, y):
    return (3*x + 2*y - 1)/(x-1)**2

def iteracion(x, y, yder, f):
    while x <= punto_final:
        x1 = x + h
        y1 = y + h*f(x, y) + ((h**2)/2)*(yder(x, y))
        iteracion(x1, y1, yder, f)
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
    
iteracion(punto_inicial, y0, derf1, f1)
grafica(puntos)