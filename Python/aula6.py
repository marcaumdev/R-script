import numpy as np
import random

vetor = list(range(1,11))
print(vetor)

vetor2 = list(range(2,21,2))
print(vetor2)

vetor100 = list(range(1,101))
vetor100soma= sum(vetor100)
print(vetor100soma)

vetor1000 = [random.randrange(1, 1001, 1) for i in range(50)]
print(vetor1000)
maxVetor1000 = max(vetor1000)
minVetor1000 = min(vetor1000)
print("Vetor máximo = ",maxVetor1000)
print("Vetor mínimo = ",minVetor1000)

def ehPrimo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = []
num = 2

while len(primos) < 10:
    if ehPrimo(num):
        primos.append(num)
    num += 1
print(primos)

vetorNormal = [random.randint(1,100) for _ in range(20)]
vetorInvertido = vetorNormal[::-1]
print("Normal: ", vetorNormal)
print("Normal Invertido: ",vetorInvertido)

matriz = np.arange(1,10).reshape(3,3)
print(matriz)

matrizIdentidade = np.eye(4)
print(matrizIdentidade)

matriz1 = np.array([[1,2], [3,4]])
matriz2 = np.array([[5,6], [7,8]])
matrizSoma = matriz1 + matriz2
print(matrizSoma)

matrizMult = matriz1@matriz2
print(matrizMult)

matrizNormal = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(matrizNormal)

matrizTransposta = np.transpose(matrizNormal)
print(matrizTransposta)

determinante = np.linalg.det(matrizNormal)
print(determinante)