try:
    resultado = 10/0
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida")

lista = [1, 2, 3]

try:
    elemento = lista[5]
except IndexError:
    print("Erro: índice fora dos limites da lista")

dicionario = {"a":1, "b":2,"c":3, "d":4}

try:
    elemento = dicionario["e"]
except KeyError:
    print("Erro: essa chave não existe no dicionário")

def main():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1/num2

    except ZeroDivisionError as e:
        print("Erro: divisão por zero não permitida")
    except ValueError as e:
        print("Vai dividir uma letra mano???")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    else:
        print(f"O resultado da divisão é {resultado}")
    finally:
        print("programa finalizado!")

main()

string = "1"
try:
    numero = int(string)
except ValueError:
    print("Erro: conversão de string para inteiro falhou")
else:
    print("Conversão feita com sucesso")

dicionario = {"a":[1,2,3], "b":[4,5,6]}
try:
    elemento = dicionario["c"][0]
except KeyError:
    print("Erro: Chave inexistente no dicionario")
except IndexError:
    print("Erro: Índice fora dos limites da lista")