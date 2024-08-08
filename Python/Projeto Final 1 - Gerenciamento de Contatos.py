contatos = {
    "pessoa1":{"nome":"Marcos", "numero":"(11) 96243-9022"},
    "pessoa2":{"nome" : "Juan", "numero" : "(11) 99257-7165"},
    "pessoa3":{"nome" : "Renata", "numero" : "(11) 94242-2610"},
    "pessoa4":{"nome" : "Bill", "numero" : "(11) 94899-6369"}
}
print()
for chave, valor in contatos.items():
    print(f"Nome: {valor['nome']}, Número: {valor['numero']}")

contatos.update({"pessoa5":{"nome":"Santos", "numero":"(11) 11111-1111"}})

print()
for chave, valor in contatos.items():
    print(f"Nome: {valor['nome']}, Número: {valor['numero']}")

contatos.pop("pessoa4")

print()
for chave, valor in contatos.items():
    print(f"Nome: {valor['nome']}, Número: {valor['numero']}")
