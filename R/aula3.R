#variáveis
nome <- "Marcos"
idade <- 19
altura <- 1.72
brasileiro <- TRUE

print(nome)
print(idade)
print(altura)
print(brasileiro)

print(typeof(nome))
print(typeof(idade))
print(typeof(altura))
print(typeof(brasileiro))

#mensagem
mensagem <- "Qualquer coisa"
print(mensagem)
print(type(mensagem))

#data/hora
data_atual <- Sys.time()
data <- Sys.Date()
hora <- Sys.time()
local <- Sys.timezone()

print(data_atual)
print(data)
print(hora)
print(local)

#enumerar
DiasDaSemana <- factor(c("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"), levels = c("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"))

print(DiasDaSemana[3])
TRUE | FALSE