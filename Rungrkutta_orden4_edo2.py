import matplotlib.pyplot as plt
import numpy as np

#definicion de puntos iniciales y final
punto_inicial = float(input("Ingrese el punto inicial: "))
u = float(input("Ingrese el valor inicial de u: "))
v = float(input("Ingrese el valor inicial de v: "))
punto_final = float(input("Ingrese el punto final: "))
n = float(input("Ingrese numero divisiones: ")) #divisiones
h = (punto_final - punto_inicial) / n #paso
puntos = []
puntos_sol = []


def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado
ene = float(input("Ingrese el valor de n: "))
uu = (-1)**ene
for m in range(0, int(ene/2)):
    sumatorio = sum((-1)**m*factorial(ene-m-1)/(factorial(m)*factorial(ene-2*m-1))*((-2)**(ene-2*m-1)))
    
uve = 1/2*sumatorio



#funcion 1
def f1(x, u, v):
    #donde u = y
    #v = y'
    #f(x) es el termino independiente. despejo y'' de la ecuacion
    # tambien se puede hacer si la ec es no lineal, si hay un y^2, ponemos la u^2 y así
    return None

def iteracion(x, u, v, f):
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
        u1 = u + h*(a1*(k11) + a2*(k21) + a3*(k31) + a4*(k41))
        v1 = v + h*(a1*(k12) + a2*(k22) + a3*(k32) + a4*(k42)) 
        iteracion(x1, u1, v1, f)
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
    
iteracion(punto_inicial, u, v, f1)
grafica(puntos)
