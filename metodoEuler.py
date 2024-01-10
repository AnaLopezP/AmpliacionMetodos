import matplotlib.pyplot as plt
import numpy as np

#definicion de puntos iniciales y final
punto_inicial = float(input("Ingrese el punto inicial x0: ")) 
y0 = float(input("Ingrese el valor de y0: "))
punto_final = float(input("Ingrese el punto final xi: "))
n = float(input("Ingrese numero divisiones: ")) #divisiones
h = (punto_final - punto_inicial) / n #paso
puntos = []
puntos_sol = []
#funcion 1
#Aqui se pone la funcion F (es decir la y' despejada)
def f1(x, y):
    return y - x**2 + 1

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
#Aquí se itera la solucion con la C calculada. 
def iteracion_solucion(x, f):
    while x <= punto_final:
        x1 = x + h
        y1 =h*f(x)
        iteracion_solucion(x1, f)
        puntos_sol.append((x1, y1))
        print(x1, y1)
        return x1, y1
    
#Funciones particulares con la C calculada. cambio la C según el valor inicial. Es decir aquí se pone la y(x). 
def solucion(x):
    return x**2 + 2*x + 1 - 0.5*np.exp(x)
def solucion2(x):
    return x**2 + 2*x + 1 - np.exp(x)
def solucion3(x):
    return x**2 + 2*x + 1 - 2*np.exp(x)



iteracion(punto_inicial, y0, f1)
grafica(puntos)
'''iteracion_solucion(punto_inicial, solucion)
grafica(puntos_sol)
puntos_sol = []
iteracion_solucion(punto_inicial, solucion2)
grafica(puntos_sol)
puntos_sol = []
iteracion_solucion(punto_inicial, solucion3)
grafica(puntos_sol)'''