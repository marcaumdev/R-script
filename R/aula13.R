soma <- function(a, b){
    return(a+b)
}

print(soma(2,2))

par <- function(numero){
  return(numero %% 2 == 0)
}
print(par(10))

media <- function(lista){
  return(mean(lista))
}
print(media(c(1,2,3,4,5)))

somaMatriz <- function(matriz){
  return(sum(matriz))
}
matriz <- matrix(1:9, nrow = 3, ncol = 3)
print(somaMatriz(matriz))

palindromo <- function(palavra){
   return(palavra == stringi::stri_reverse(palavra))
}

print(palindromo("ovo"))
print(palindromo("bala"))

contaVogais <- function(string){
    vogais <- c("a", "e", "i", "o", "u")
    return (sum(tolower(strsplit(string, NULL)[[1]]) %in% vogais))
}

print(contaVogais("paralelepipedo"))

a <- matrix(c(1,2,3,4), nrow = 2, ncol = 2, byrow=TRUE)
b <- matrix(c(5,6,7,8), nrow = 2, ncol = 2, byrow=TRUE)

produtoMatriz <- function(matrizA, matrizB){
    return(matrizA %*% matrizB)
}

print(produtoMatriz(a,b))

fatorial <- function(n){
    if(n == 0){
        return(1)
    }
    return(n * fatorial(n-1))
}

print(fatorial(5))

somaNNumeros <- function(n){
    if(n == 0){
        return(0)
    }
    return(n + somaNNumeros(n-1))
}

print(somaNNumeros(10))