import math
import numpy as np
import matplotlib.pyplot as plt

print(math.cos(math.radians(60)))
print(math.cos(math.pi/3))

fcos=np.cos(np.linspace(0,360,360) * np.pi / 180)
x=np.linspace(0,360,360)

plt.figure().set_figheight(2,3)
plt.plot(x, fcos)
plt.xlabel('x', fontsize=15)
plt.ylabel('cos(x)', fontsize=15)
plt.title('Função cosseno')
plt.legend(['f(x)=cos(x)'])
plt.show()

fcos=np.cos(2*(np.linspace(0,360,360) * np.pi / 180)) + np.ones(360) * (-3)
x=np.linspace(0,360,360)

plt.figure().set_figheight(2,3)
plt.plot(x, fcos)
plt.xlabel('x', fontsize=15)
plt.ylabel('cos(x)', fontsize=15)
plt.title('Função cosseno')
plt.legend(['f(x)=cos(2x)-3'])
plt.show()


print(math.tan(math.radians(60)))

print(math.tan(math.pi/3))

ftan=np.tan(np.linspace(0,360,360) * np.pi / 180)
print(np.tan(np.pi/2))
x=np.linspace(0,360,360)

plt.figure().set_figheight(2,3)
plt.plot(x, ftan)
plt.xlabel('x', fontsize=15)
plt.ylabel('tan(x)', fontsize=15)
plt.title('Função tanseno')
plt.legend(['f(x)=tan(x)'])
plt.ylim(-20, 20)
plt.show()

x = np.arange(-60, 60, 1, dtype=int)
y = x**3 + 3*x + 5

plt.plot(x, y)
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.title('Função Polinomial')
plt.show()

x = np.linspace(0.1, 10, 30)
y=2.**x

plt.xlabel('x', fontsize=15)
plt.ylabel('x', fontsize=15)
plt.title('Funcao exponencial')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.plot(x,y)
plt.show()

x=math.log(16,2)
print(x)

x=np.linspace(0.1,10,30)
y=np.log(x)

plt.xlabel('x',fontsize=15)
plt.ylabel('y',fontsize=15)
plt.title('Função logaritmo')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.plot(x,y)
plt.show()