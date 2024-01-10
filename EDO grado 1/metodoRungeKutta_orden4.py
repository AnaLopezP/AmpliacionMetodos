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
    return y - x**2 + 1

def iteracion(x, y, f):
    k1 = f(x, y)
    k2 = f(x + (h/2), y + (h/2)*k1)
    k3 = f(x + (h/2), y + (h/2)*k2)
    k4 = f(x + h, y + h*k3)
    
    a1 = 1/6
    a2 = 1/3
    a3 = 1/3
    a4 = 1/6
    
    if x > punto_final:
        return x, y
    x1 = x + h
    y1 = y + h*(a1*k1 + a2*k2 + a3*k3 + a4*k4)
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
    
iteracion(punto_inicial, y0, f1)
grafica(puntos)