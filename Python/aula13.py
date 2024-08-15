import numpy as np

def soma(a, b):
    return a + b

print(soma(2,2))

def par(numero):
  return numero % 2 == 0
print(par(11))

def media(lista):
  return sum(lista) / len(lista)
print(media([1,2,3,4,5]))

def somaMatriz(matriz):
  return sum(sum(linha) for linha in matriz)

matriz = [[1,2,3],[4,5,6],[7,8,9]]  
print(somaMatriz(matriz))

def palindromo(palavra):
   return palavra == palavra[::-1]

print(palindromo("ovo"))
print(palindromo("bala"))

def contaVogais(string):
    vogais = "aeiou"
    return sum(1 for char in string if char.lower() in vogais)

print(contaVogais("python"))

a = [[1,2],[3,4]]
b = [[5,6],[7,8]]

def produtoMatriz(matrizA, matrizB):
   return [[sum(a*b for a,b in zip(linhaA, colunaB)) for colunaB in zip(*matrizB)] for linhaA in matrizA]

print(produtoMatriz(a,b))

def fatorial(n):
   if n == 0:
      return 1
   return n * fatorial(n-1)

print(fatorial(5))

def somaNNumeros(n):
    if n == 0:
        return 0
    
    return(n+somaNNumeros(n-1))

print(somaNNumeros(10))