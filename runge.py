import numpy as np
import matplotlib.pyplot as plt

def heun_method(f, y0, x0, xn, h):
   
    valores_x = []
    valores_y = []
    x = x0
    y = y0
    while x <= xn:
        valores_x.append(x)
        valores_y.append(y)

        k1 = f(x, y)
        print("el valor de k1 es", k1)
        k2 = f(x + h, y + k1*h)
        print ("El valor de K2 es" , k2)
        print (y)
        y = y + 0.5 *h* (k1 + k2)
        x = x + h
    return valores_x,valores_y

# Solicitar al usuario ingresar la ecuación diferencial
def introducir_ecuacion(x, y):
    # Modifica esta función según la ecuación diferencial que desees resolver
    return x *np.sqrt(y)
def Grarficar_funcion(ecuación,y0, x0, xn,h):
    # Resuelve la ecuación diferencial utilizando el método de Heun
    valores_x, valores_y = heun_method(introducir_ecuacion, y0, x0, xn, h)
    # Grafica de la solución
    plt.plot(valores_x, valores_y, label='Solución y(x)')
    plt.xlabel('Tiempo (x)')
    plt.ylabel('y(x)')
    plt.legend()
    plt.show()
# Condiciones iniciales
y0 = float(input("Ingrese el valor inicial de y(0): "))
x0 = float(input("Ingrese el valor de x(0): "))
xn = float(input("Ingrese el valor final de x: "))
h = float(input("Ingrese el tamaño del paso (h): "))

Grarficar_funcion(introducir_ecuacion,y0,x0,xn, h)