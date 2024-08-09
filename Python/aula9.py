import numpy as np
import matplotlib.pyplot as plt


def graficoSub(x, y, titulo, local):
    plt.subplot(2,2,local)
    plt.xlabel('x', fontsize=15)
    plt.ylabel('y', fontsize=15)
    plt.title(titulo)
    plt.plot(x,y)

aPonto = []
bPonto = []

def adicionaPonto(a, nome):
    x = int(input(f'Digite o valor de x do ponto {nome}: '))
    a.append(x)
    y = int(input(f'Digite o valor de y do ponto {nome}: '))
    a.append(y)
    print(a)

def calculaA(a, b):
    aVar = (a[1] - b[1]) / (a[0] - b[0])
    return aVar

def calculaB(b, a):
    b = b[1] - (a*b[0])
    return b

x=np.array([-2,-1,0,1,2])
y=2*x
print(y)

#grafico(x,y, 'grafico teste')

adicionaPonto(aPonto, "A")
adicionaPonto(bPonto, "B")

a = calculaA(aPonto, bPonto)
b = calculaB(bPonto, a)
print("y = ax + b")
print(f"y = {a}x + {b}")

#y = ax + b

x=np.arange(-10, 10, 1 , dtype=int)
y=a*x+b

#grafico(x,y, 'Função Afim')

y = 2*x+6
graficoSub(x,y, 'Função 1', 1)
y = -3*x+1
graficoSub(x,y, 'Função 2', 2)
y = x-1/5
graficoSub(x,y, 'Função 3', 3)
y = -6*x-2
graficoSub(x,y, 'Função 4', 4)
plt.show()