import matplotlib.pyplot as plt
punto_inicial = int(input("Ingrese el punto inicial: "))
punto_final = int(input("Ingrese el punto final: "))
N = 100
h = (punto_final - punto_inicial) / N
puntos = []

def f(x, y):
    return (2-x-y)/(x-y+4)

def iteracion(x, y):
    while x <= punto_final:
        x1 = x + h
        y1 = y + h*f(x, y)
        iteracion(x1, y1)
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
    
iteracion(punto_inicial, 4)
grafica(puntos)