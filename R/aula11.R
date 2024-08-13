numero <- 5

if(numero > 0){
    print("O número é positivo")
}else if (numero == 0) {
    print("O número é zero")
}else {
    print("O número é negativo")
}

palavra <- "marcos"

if(nchar(palavra) > 5){
    print(paste("A palavra", palavra, "tem mais que 5 caracteres"))
}else if(nchar(palavra) == 5){
    print(paste("A palavra", palavra, "tem exatemente 5 caracteres"))
}else{
    print(paste("A palavra", palavra, "tem menos que 5 caracteres"))
}

ano <- 2024
if(ano %% 4 == 0 && ano %% 100 != 0){
    print(paste("O ano", ano, "é bissexto"))
}else{
    print(paste("O ano", ano, "não é bissexto"))
}

numero <- 15
if(numero >= 10 && numero <= 20){
    print(paste("O numero", numero, "está entre 10 e 20"))
}else{
    print(paste("O numero", numero, "não está entre 10 e 20"))
}

variavel <- "abc123"
if(any(grepl("[A-Za-z]", variavel)) && any(grepl("[0-9]", variavel))){
    print(paste("a string", variavel, "possui letras e numeros"))
}else{
    print(paste("a string", variavel, "não possui letras e numeros"))
    
}

idade <- 25

if (idade < 13){
    print("Criança")
}else if(idade < 18){
    print("Adolescente")
}else if(idade < 60){
    print("Adulto")
}else{
    print("Idoso")}

mes <- 7
if (mes %in% c(12, 1, 2)){
    print("Verão")
}else if(mes %in% c(6, 7, 8)){
    print("Inverno")
}else if(mes %in% c(9, 10, 11)){
    print("Verão")
}else if(mes %in% c(3, 4, 5)){
    print("Outono")
}else{
    print("Mês inválido")
}

for(num in 1:10){
    print(num)
}

lista <- c(1,2,3,4,5)
for (elemento in lista){
    print(elemento)
}

dicionario <- list(a=1, b=2, c=3, d=4)
for(chave in names(dicionario)){
  print(paste("Chave:", chave, "Valor", dicionario[[chave]]))
}

x <- 1
while (x < 11){
    print(x)
    x <- x + 1
}