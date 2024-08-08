
dicionario <- list(nome = "Marcos", idade = 19, cidade = "São Paulo")
dicionario$cidade <- NULL
print(dicionario)

dicionario <- list(
  "pessoa1"<-list(nome = "Juan", idade = 21, cidade = "Sao Paulo"),
  "pessoa2"<-list(nome = "Renata", idade = 18, cidade = "Santo André"),
  "pessoa3"<-list(nome = "Matheus", idade = 19, cidade = "Poá"),
  "pessoa4"<-list(nome = "Bill", idade = 25, cidade = "Heliíopoles")
)
print(dicionario)

for(pessoa in dicionario){
  print(paste("Nome:", pessoa$nome, "Idade", pessoa$idade, "Cidade", pessoa$cidade))
}

soma <- 10 + 20
print(soma)

subtracao <- 30 - 15
print(subtracao)

mult <- 6 * 7
print(mult)

div <- 81/9
print(div)

exp <- 2 ** 10
print(exp)

elev <- 2 ^ 10
print(elev)

resto <- 29 %% 5
print(resto)

resultado <- 8 > 5
print(resultado)

resultado <- 3 <= 10
print(resultado)

resultado <- (5 < 7) < 10
print(resultado)

resultado <- 12 %% 2 == 0 & (10 < 12) < 15
print(resultado)

numero <- 25
resultado <- (numero %% 3 == 0 | numero %% 5 == 0) & (numero > 20 & numero < 30)
print(resultado)

elegivelParaPremio<- function(idade, membroAtivo){

    return ((idade > 18 & membroAtivo) | (idade > 60))
}

print(elegivelParaPremio(25, TRUE))
print(elegivelParaPremio(65, FALSE))
print(elegivelParaPremio(30, FALSE))