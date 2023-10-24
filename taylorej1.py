import matplotlib.pyplot as plt
import numpy as np
punto_inicial = int(input("Ingrese el punto inicial: "))
punto_final = int(input("Ingrese el punto final: "))
n = 200
h = (punto_final - punto_inicial) / n
puntos = []

def f1(x, y):
    return (2-x-y)/(x-y+4)

def f2(x, y):
    return (2*x*np.exp(-3*x) )-3*y   

def iteracion(x, y, f):
    while x <= punto_final:
        x1 = x + h
        y1 = y + h*f(x, y)
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
    
iteracion(punto_inicial, 4.5, f1)
grafica(puntos)