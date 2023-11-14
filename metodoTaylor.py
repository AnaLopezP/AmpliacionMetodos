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
    return (1+4*x*y)/(3*x*x)

def derf1(x, y):
    return (4*x*y-2)/(9*x**3)

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