punto_inicial = 0
punto_final = 2
N = 10
h = (punto_final - punto_inicial) / N

def f(x, y):
    pass

def iteracion(x, y):
    while x <= punto_final:
        x1 = x + h
        y1 = y + h*f(x, y)
        iteracion(x1, y1)
        
def polinomio_taylor(x, y):
    return y + h*f(x, y)