import numpy as np 

A = np.array([[6,1,1],
              [4,-2,5],
              [2,8,7]])
invA = np.linalg.inv(A)
print('A inversa da matriz A é:\n', invA)

fatoracao = []

def fatoraPrimo():
    n = int(input("Digite um numero positivo e inteiro: "))

    fator = 2
    while n != 1:
        while n % fator == 0:
            n /= fator
            fatoracao.append(fator)

        fator += 1
    
    print(fatoracao)

fatoraPrimo()

a = np.array([[0,2],[2,3]])
w,v=np.linalg.eig(a)
print("E-value: ", w)
print("E-vector:\n ", v)