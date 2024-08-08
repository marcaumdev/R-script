
dicionario = {"nome" : "Marcos", "idade" : "19", "cidade" : "São Paulo"}
dicionario.pop("cidade")
print(dicionario)

formato = {"nome": "ana","idade": 25, "cidade":"são paulo"}

dicionario = {
    "pessoa1":{"nome":"Ana", "idade":"25", "cidade":"Sao Paulo"},
    "pessoa2":{"nome" : "Renata", "idade" : 18, "cidade" : "Santo André"},
    "pessoa3":{"nome" : "Matheus", "idade" : 19, "cidade" : "Poá"},
    "pessoa4":{"nome" : "Bill", "idade" : 25, "cidade" : "Heliíopoles"}
}
for chave, valor in dicionario.items():
    print(f"Nome: {valor['nome']}, Idade: {valor['idade']}, Cidade: {valor['cidade']}")

soma = 10 + 20
print(soma)

subtracao = 30 - 15
print(subtracao)

mult = 6 * 7
print(mult)

div = 81/9
print(div)

exp = 2 ** 10
print(exp)

elev = 2 ^ 10
print(elev)

resto = 29 % 5
print(resto)

resultado = 8 > 5
print(resultado)

resultado = 3 <= 10
print(resultado)

resultado = 5 < 7 < 10
print(resultado)

resultado = 12 % 2 == 0 & 10 < 12 < 15
print(resultado)

numero = 25
resultado = (numero % 3 == 0 or numero % 5 == 0) and (numero > 20 and numero < 30)
print(resultado)

def elegivelParaPremio(idade, membroAtivo):
    return (idade > 18 and membroAtivo) or (idade > 60)

print(elegivelParaPremio(25, True))
print(elegivelParaPremio(65, False))
print(elegivelParaPremio(30, False))