cores <- factor(c('vermelho', 'azul', 'verde'))
print(cores)

diasSemana <- factor(c('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'))
print(diasSemana)

niveis <- factor(c('Baixo', 'Alto', 'Médio'), levels = c("Baixo", "Médio", "Alto"), ordered = TRUE)
print(niveis)

numeros <- as.numeric(niveis)
print(numeros)

tamanhos <- factor(c("Pequeno", "Médio", "Grande"), levels = c("Pequeno", "Médio", "Grande"), ordered = TRUE)
print(tamanhos)
levels(tamanhos)[levels(tamanhos) == "Pequeno"] <- "Extra Pequeno"
print(tamanhos)

set.seed(123)
categorias <- c("baixo", "médio", "alto")
vetor <- sample(categorias, 100, replace = TRUE)
fatores <- factor(vetor, levels = categorias, ordered = TRUE)
frequencias <- table(fatores)
print(frequencias)

lista <- c(1,2,3,4,5)
print(lista)

lista[[6]] <- 6
print(lista)

lista <- lista[-3]
print(lista)

listaInvertida = rev(lista)
print(listaInvertida)

matriz <- list(c(1,2,3), c(4,5,6), c(7,8,9))
somaLinhas <- sapply(matriz, sum)
print(somaLinhas)

tupla <- list(1,2,3,4,5)
print(tupla)

tupla1 <- list(1,2,3)
tupla2 <- list(4,5,6)
tuplaConcatenada <- c(tupla1, tupla2)
print(tuplaConcatenada)

existe <- 3 %in% tupla
print(existe)

indice <- which(unlist(tupla) == 4)
print(indice)

dicionario <- list(nome = "Marcos", idade = 19, cidade = "São Paulo")
idade <- dicionario$idade
print(dicionario)
print(idade)

dicionario$profissao <- "programador"
print(dicionario)