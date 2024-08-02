import numpy as np
import math as math

vetor = np.array([1,2,3,4,5,6,7,8])
print(vetor)

modulo = np.linalg.norm(vetor)
print(modulo)

vetor1 = np.array([-55, 12])
modulo1 = np.linalg.norm(vetor1)
print(modulo1)

vetor2 = np.array([11, -23, -4])
modulo2 = np.linalg.norm(vetor2)
print(modulo2)

u = np.array([-3, -5])
v = np.array([6, 27])

soma = u+v
print("A soma dos vetores é: ", soma)
subt = u-v
print('A subtração dos vetores é: ', subt)

multp = 9*u
print("A multiplicação é: ", multp)

multpfra = (1/3)*v
print("A multiplicação por fração é: ", multpfra)

u2 = np.array([2, (5/3)])
v2 = np.array([-1, 7])

soma2 = u2+v2
print("A soma dos vetores é: ", soma2)
subt2 = u2-v2
print('A subtração dos vetores é: ', subt2)

multp2 = 3*u2
print("A multiplicação é: ", multp2)

multpfra2 = (1/5)*v2
print("A multiplicação por fração é: ", multpfra2)

array1 = np.array([-2, 3])
array2 = np.array([7, 4])
cos = math.cos(2.36)
print("coseno: ",cos)

def calculaR(array1, array2):
    a = math.sqrt(sum(array1**2))
    b = math.sqrt(sum(array2**2))
    print("A: ",a)
    print("B: ",b)

    a2 = a**2
    b2 = b**2
    print("A quadrado: ",a2)
    print("B quadrado: ",b2)

    r = math.sqrt(a2 + b2 + 2 * a * b * cos)
    print("R: ", r)

calculaR(array1, array2)

a3 = np.array([5,4,2])
b3 = np.array([1,3,-12])

resposta = sum(a3*b3)

print(resposta)