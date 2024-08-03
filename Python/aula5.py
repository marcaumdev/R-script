import numpy as np
import math

matriz = np.array([[1,2,3],[4,5,6]])
print(matriz)
print(matriz.shape)

A = np.random.rand(2,2)
print("Matriz A:\n", A)

B = np.random.rand(3,4)
print("Matriz B:\n", B)

I = np.identity(3)
print("Matriz de identidade:\n", I)

A2 = np.random.rand(3,2)
A2T = np.transpose(A2)

print("Matriz A2:\n",A2)
print("Matriz A2 Transposta:\n",A2T)

Amult = np.array([[1, -3, 5], [8, 0, 3]])
Bmult = np.array([[2, 4], [6, 10], [1, 5]])

multm = np.matmul(Amult, Bmult)
print("A multiplicação entre as matrizes é:\n", multm)

Adet = np.array([[1,9,5],[3,7,8],[10,4,2]])
detA = np.linalg.det(Adet)
print("O determinante da matriz é:\n", detA)

r2 = math.sqrt(2)
r3 = math.sqrt(3)
r6 = math.sqrt(6)

Ad = np.array([2,5,-3], [1,4,7], [-1,0,6])
Bd = np.array([r2,2,1], [-1,r3,3], [3,2,r6])

determA = np.linalg.det(Ad)
print("O determinante da matriz A é:\n", determA)

determB = np.linalg.det(Bd)
print("O determinante da matriz B é:\n", determB)