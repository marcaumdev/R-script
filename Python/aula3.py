#variáveis
nome = "Marcos"
idade = 19
altura = 1.72
brasileiro = True

print("Nome: ", nome)
print("Idade: ", idade)
print("Altura: ", altura)
print("Brasileiro: ", brasileiro)

print(type(nome))
print(type(idade))
print(type(altura))
print(type(brasileiro))

#float
PI = 3.14159

#mensagem
mensagem = "qualé rapaziada"
print(mensagem)
print(type(mensagem))

#inteiro
numero = 100

#data/hora
from datetime import datetime
data_atual = datetime.now()
print(data_atual)

#enumerar
from enum import Enum

class DiasDaSemana(Enum):
  Segunda = 1
  Terca = 2
  Quarta = 3
  Quinta = 4
  Sexta = 5
  Sabado = 6
  Domingo = 7

print(DiasDaSemana.Quarta.name)
print(DiasDaSemana.Quarta.value)
