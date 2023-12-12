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

'''
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
'''
print("Para el problema de los conejos y los zorros:")
p = float(input("Ingrese el valor de p: "))
q = float(input("Ingrese el valor de q: "))
r = float(input("Ingrese el valor de r: "))
s = float(input("Ingrese el valor de s: "))
#funcion 1
def funcionx(x, u, v):
    #donde u = x
    #v = y
    # tambien se puede hacer si la ec es no lineal, si hay un y^2, ponemos la u^2 y así
    return p*u -q*u*v

def funciony(x, u, v):
    return -r*u + s*u*v


def iteracion(x, u, v, fx, fy):
    # en los sistemas, las u' y las v' ahora son expresiones, osea que tanto las k1 como las k2 van a llamar a una funcion
    k11 = fx(x, u, v)
    k12 = fy(x, u, v)
    k21 = fx(x + h/2, u + (h/2)*k11, v + (h/2)*k12)
    k22 = fy(x + h/2, u + (h/2)*k11, v + (h/2)*k12)
    k31 = fx(x + h/2, u + (h/2)*k21, v + (h/2)*k22)
    k32 = fy(x + h/2, u + (h/2)*k21, v + (h/2)*k22)
    k41 = fx(x + h, u + h*k31, v + h*k32)
    k42 = fy(x + h, u + h*k31, v + h*k32)
    
    a1 = 1/6
    a2 = 1/3
    a3 = 1/3
    a4 = 1/6
    
    while x <= punto_final:
        x1 = x + h
        u1 = u + h*(a1*(k11) + a2*(k21) + a3*(k31) + a4*(k41))
        v1 = v + h*(a1*(k12) + a2*(k22) + a3*(k32) + a4*(k42)) 
        iteracion(x1, u1, v1, fx, fy)
        puntos.append((x1, v1))
        puntos_sol.append((x1, u1))
        print(x1, v1)
        print(x1, u1)
        return x1, v1, u1

def grafica(puntos, puntos_sol):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for i in puntos:
        x1.append(i[0])
        y1.append(i[1])
    for i in puntos_sol:
        x2.append(i[0])
        y2.append(i[1])
    plt.plot(x1, y1)
    plt.plot(x2, y2)    
    plt.show()
    
iteracion(punto_inicial, u, v, funcionx, funciony)
grafica(puntos, puntos_sol)

