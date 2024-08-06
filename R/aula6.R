vetor <- 1:10
print(vetor)

vetor2 <- seq(2, 20, by = 2)
print(vetor2)

vetor100 <- 1:100
vetor100soma <- sum(vetor100)
print(vetor100soma)

vetor1000 <- sample(1:1000, 50, replace = TRUE)
maior <- max(vetor1000)
menor <- min(vetor1000)
print(paste("Menor: ", menor, "Maior: ", maior))

ehPrimo <- function(n){
    if (n <= 1) {
        return(FALSE)
    }
    for (i in 2:sqrt(n)) {
        if (n %% i == 0) {
            return(FALSE)
        }
    }
    return(TRUE)
}

primos <- c()
num <- 2
while (length(primos) < 10){
    if(ehPrimo(num)){
        primos <- c(primos, num)
    }
    num <- num + 1
}

print(primos)

vetorNormal <- sample(1:100, 20, replace = TRUE)
vetorInvertido <- rev(vetorNormal)
print(vetorNormal)
print(vetorInvertido)

matriz <- matrix(1:9, nrow = 3, ncol = 3)
print(matriz)

matrizIdentidade <- diag(4)
print(matrizIdentidade)

matriz1 <- matrix(c(1,2,3,4), nrow = 2, ncol =  2)
matriz2 <- matrix(c(5,6,7,8), nrow = 2, ncol =  2)

matrizSoma <- matriz1 + matriz2
print(matrizSoma)

matrizMult <- matriz1 %*% matriz2
print(matrizMult)

matrizNormal <- matrix(1:9, nrow = 3, ncol = 3)
print(matrizNormal)
matrizTransposta <- t(matrizNormal)
print(matrizTransposta)

determinante <- det(matrizNormal)
print(determinante)