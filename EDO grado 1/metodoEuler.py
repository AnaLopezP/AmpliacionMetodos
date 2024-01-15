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
    return 9.8 - (0.5/(10-0.1*x))*y

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
    return x**2 / np.exp(x**2)
def solucion2(x):
    return (1 + x**2) / np.exp(x**2)
def solucion3(x):
    return (-1 + x**2) / np.exp(x**2)

'''Para las soluciones particulares, da igual el valor de y0, ya que ese se usa solo en el método original.
De esta manera, la primera gráfica tendrá que coincidir con la gráfica exacta de la solución particular, únicamente en el punto que haya insertadop x0, y0. '''

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