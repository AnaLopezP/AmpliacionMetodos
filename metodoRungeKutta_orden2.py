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
    return (y - x*x + 1)

def iteracion(x, y, f):
    while x <= punto_final:
        x1 = x + h
        y1 = y + h*f(x + (h/2), y + (h/2)*f(x, y))
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
#la solucion aproximada es w100 = -11.4621 y la solucion real es y(4) = -11.46. El error es de 0.0021