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

def f2(x, y):
    return (y - x*x + 1)


def f3(x, y):
    return (x*y)/(x**2 + y**2)

def f4(x, y):
    return (x+y)/(x-y)

def iteracion(x, y, f):
    while x <= punto_final:
        x1 = x + h
        z1 = y + h*f(x, y)
        y1 = y + (h/2)*(f(x, y) + f(x1, z1))
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
    
iteracion(punto_inicial, y0, f2)


grafica(puntos)

'''La solución aproximada es w = -8.20, con la funcion f1. La solución real es y(6) = -8.20. Hay un error de 0'''
'''En la funcion 2, la solucion aprox es w = -11.4539. La solucion real y(4) = -11.46. El error es de 0.0061'''