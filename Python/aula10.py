import numpy as np
import matplotlib.pyplot as plt
import math

a = int(input("informe o valor de a: "))
b = int(input("informe o valor de b: "))
c = int(input("informe o valor de c: "))

def delta(a, b, c):
    delta = b**2 - (4 * a * c)
    return delta

def baskara(delta, a, b):
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)

    if(delta == 0):
        print(f"Delta tem 1 raiz que é {x1}")
    elif(delta < 0):
        print("Delta não tem raiz")
    else:
        print(f"As raízes de delta são x1 = {x1} x2 = {x2}")

def vertice(a, delta):
    y = -delta / (4 * a)
    return y

deltaValor = delta(a, b, c)
baskara(deltaValor, a, b)

x = np.arange(-50, 60, 1, dtype = int)
y = a*x**2+b*x+c

plt.plot(x, y)
plt.xlabel('x', fontsize = 15)
plt.ylabel('y', fontsize = 15)
plt.title('Função Quadrática')
plt.show()

print(math.sin(math.radians(60)))
print(math.sin(math.pi/3))

fsin=np.sin(np.linspace(0,360,360) * np.pi / 180 )
x = np.linspace(0, 360, 360)

plt.figure().set_figheight(2,3)
plt.plot(x, fsin)
plt.xlabel('x', fontsize = 15)
plt.xlabel('sin(x)', fontsize = 15)
plt.title("Função Seno")
plt.legend(["f(x) = sin(x)"])
plt.show()

fsin=np.sin(np.linspace(0,360,360) * np.pi / 180) + 2
x = np.linspace(0, 360, 360)

plt.figure().set_figheight(2,3)
plt.plot(x, fsin)
plt.xlabel('x', fontsize = 15)
plt.xlabel('sin(x)', fontsize = 15)
plt.title("Função Seno")
plt.legend(["f(x) = sin(x)"])
plt.show()