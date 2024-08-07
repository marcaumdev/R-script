import pandas as pd
import random

cores = pd.Categorical(['vermelho', 'azul', 'roxo'])
print(cores)

diasSemana = pd.Categorical(['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'])
print(diasSemana)

niveis = pd.Categorical(["Baixo", "Alto", "Médio"], categories=["Baixo", "Médio", "Alto"], ordered = True)
print(niveis)

numeros = niveis.codes
print(numeros)

tamanhos = pd.Categorical(["Pequeno", "Médio", "Grande"], categories = ["Pequeno", "Médio", "Grande"], ordered = True)
tamanhos2 = tamanhos.rename_categories({"Pequeno":"Extra Pequeno"})
print(tamanhos2)

categorias = ["baixo", "médio", "alto"]
vetor = [random.choice(categorias) for _ in range(100)]
fatores = pd.Categorical(vetor, categories = categorias, ordered = True)
frequencias = pd.value_counts(fatores)
print(frequencias)

lista = [1,2,3,4,5]
print(lista)

lista.append(6)
print(lista)

lista.pop(2)
print(lista)

listaInvertida = lista[::-1]
print(listaInvertida)


matriz = [[1,2,3], [4,5,6], [7,8,9]]
somaLinhas = [sum(linha)for linha in matriz]
print(somaLinhas)

tupla = (1,2,3,4,5)
print(tupla)

print(tupla[2])

tupla1 = (1,2,3)
tupla2 = (4,5,6)
tuplaConcatenada = tupla1 + tupla2
print(tuplaConcatenada)

existe = 3 in tupla
print(existe)

indice = tupla.index(4)
print(indice)

dicionario = {"nome":"Marcos", "idade":"19", "cidade":"São Paulo"}
idade = dicionario["idade"]
print(dicionario)
print(idade)

dicionario["profissão"] = "programador"
print(dicionario)