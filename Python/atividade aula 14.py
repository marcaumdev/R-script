import numpy as np
import matplotlib.pyplot as plt

a = [-10,-5,0,5,10]
b = [-15,-10,-7,-5,-2,3,5,8,10,12,13]
arrayResultado = []

for num in a:
    resultado = num + 3
    for i in b:
        if resultado == i:
            arrayResultado.append(resultado)

print(arrayResultado)

#plot 1:
plt.figure().set_figheight(3,3) 
x= np.linspace(-10,10,50)
y1 = -3*x-10 
plt.subplot(1, 2, 1)
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('1º Equação')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.plot(x,y1)
#plt.show()
#plot 2:
y2 = 5*x+2
plt.subplot(1, 2, 2)
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('2º Equação')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.plot(x,y2)
plt.tight_layout(pad=3.0)
#plt.show()

def calcularLucro(pecas):
    c = np.sqrt(pecas) - 4000*pecas
    r = 8500*pecas - np.sqrt(pecas)
    l = r - c
    print(l)

calcularLucro(3000)
calcularLucro(3125)
calcularLucro(3250)
calcularLucro(3500)