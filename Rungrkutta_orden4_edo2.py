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
def f1(x, u, v):
    #a = None #el coeficiente lineal de y'
    #b = None #el coeficiente de y
    f = None #el termino independiente
    return f

def iteracion(x, u, v, f, a, b):
    '''(k11, k12) = [[0, 1], [-b (x), -a (x)]]*[[u], [v]] + [[0], [f (x)]]
    (k21, k22) = [[0, 1], [-b (x + h/2), -a (x + h/2)]]*[[u + (h/2)*k11], [v + (h/2)*k12]] + [[0], [f (x + h/2)]]
    (k31, k32) = [[0, 1], [-b (x + h/2), -a (x + h/2)]]*[[u + (h/2)*k21], [v + (h/2)*k22]] + [[0], [f (x + h/2)]]
    (k41, k42) = [[0, 1], [-b (x + h), -a (x + h)]]*[[u + h*k31], [v + h*k32]] + [[0], [f (x + h)]]
    '''
    k11 = v
    k12 = f(x, u, v)
    k21 = v + (h/2)*k11
    k22 = f(x + h/2, u + (h/2)*k11, v + (h/2)*k12)
    k31 = v + (h/2)*k21
    k32 = f(x + h/2, u + (h/2)*k21, v + (h/2)*k22)
    k41 = v + h*k31
    k42 = f(x + h, u + h*k31, v + h*k32)
    
    a1 = 1/6
    a2 = 1/3
    a3 = 1/3
    a4 = 1/6
    
    while x <= punto_final:
        x1 = x + h
        (u1, v1) = u + h*(a1*(k11, k12) + a2*(k21, k22) + a3*(k31, k32) + a4*(k41, k42))
        iteracion(x1, u1, v1, f, a, b)
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
    
iteracion(punto_inicial, y0, f1)
grafica(puntos)
