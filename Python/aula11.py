numero = 5

if numero > 0:
    print(f"O número {numero} é positivo")
elif numero == 0:
    print(f"O número é zero")
else:
    print(f"O número {numero} é negativo")

palavra = "marcos"

if(len(palavra) > 5):
    print(f"A palavra {palavra} tem mais que 5 caracteres")
elif(len(palavra) == 5):
    print(f"A palavra {palavra} tem exatemente 5 caracteres")
else:
    print(f"A palavra {palavra} tem menos que 5 caracteres")

ano = 2024
if(ano % 4 == 0 and ano % 100 != 0):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")

numero = 15
if numero >= 10 and numero <= 20:
    print(f"O numero {numero} está entre 10 e 20")
else:
    print(f"O numero {numero} não está entre 10 e 20")

variavel = "er42te"

if any(c.isalpha() for c in variavel) and any(c.isdigit() for c in variavel):
    print(f"a string {variavel} possui letras e numeros")
else:
    print(f"a string {variavel} não possui letras e numeros")

idade = 25

if idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")

mes = 7
if mes in [12, 1, 2]:
    print("Verão")
elif mes in [6, 7, 8]:
    print("Inverno")
elif mes in [9, 10, 11]:
    print("Verão")
elif mes in [3, 4, 5]:
    print("Verão")
else:
    print("Mês inválido")


for num in range(1, 11):
    print(num)

lista = [1,2,3,4,5]

for num in lista:
    print(num)

dicionario = {"a":1, "b":2,"c":3, "d":4}
for chave, valor in dicionario.items():
    print(f"{chave}:{valor}")

x = 1
while x < 11:
    print(x)
    x += 1