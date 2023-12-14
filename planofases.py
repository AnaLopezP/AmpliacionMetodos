import matplotlib.pyplot as plt
import numpy as np

#definicion de puntos iniciales y final
puntos_iniciales = []
num_puntos = int(input("Ingrese el número de puntos iniciales: "))

for i in range(num_puntos):
    u = float(input(f"Ingrese el valor inicial de u para el punto {i+1}: "))
    v = float(input(f"Ingrese el valor inicial de v para el punto {i+1}: "))
    x0 = float(input(f"Ingrese el valor inicial de x para el punto {i+1}: "))
    puntos_iniciales.append((u, v, x0))



punto_final = float(input("Ingrese el punto final: "))
n = float(input("Ingrese numero divisiones: ")) #divisiones
h = (punto_final - puntos_iniciales[0][2 ]) / n #paso

puntos = []
puntos_sol = []


#funcion 1
def funcionx(x, u, v):
    #Aquí ponemos la ecuacion diferencial de x'
    #donde u = x
    #v = y
    # tambien se puede hacer si la ec es no lineal, si hay un y^2, ponemos la u^2 y así
    return v

def funciony(x, u, v):
    #Aquí ponemos la ecuacion diferencial de y'
    return -u + u**2


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
    
    x1 = x + h
    u1 = u + h*(a1*(k11) + a2*(k21) + a3*(k31) + a4*(k41))
    v1 = v + h*(a1*(k12) + a2*(k22) + a3*(k32) + a4*(k42))  
    
    
    return x1, u1, v1
    
'''while x <= punto_final:
    x1 = x + h
    u1 = u + h*(a1*(k11) + a2*(k21) + a3*(k31) + a4*(k41))
    v1 = v + h*(a1*(k12) + a2*(k22) + a3*(k32) + a4*(k42)) 
    iteracion(x1, u1, v1, fx, fy)
    puntos.append((u1, v1))
    print(u1, v1)
    return x1, v1, u1'''

def grafica(puntos):
    for i, punto_inicial in enumerate(puntos):
        u = punto_inicial[0]
        v = punto_inicial[1]
        x_vals = [punto_inicial[2]]
        u_vals = [u]
        v_vals = [v]
    
        while x_vals[-1] < punto_final:
            x, u, v = iteracion(x_vals[-1], u_vals[-1], v_vals[-1], funcionx, funciony)
            x_vals.append(x)
            u_vals.append(u)
            v_vals.append(v)
            print(u, v)

        plt.plot(u_vals, v_vals, label=f'Curva {i+1}')
        
    plt.xlabel('u')
    plt.ylabel('v')
    plt.legend()
    plt.show()


grafica(puntos_iniciales)

