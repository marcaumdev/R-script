tryCatch({
    resultado <- 10/0
}, error = function(e){
    message("Erro: Divisão por zero não é permitida")
})

lista <- c(1,2,3)
tryCatch({
    elemento <- lista[5]
},error = function(e){
    message("Erro: índice fora dos limites da lista")
})

dicionario <- list(a=1, b=2, c=3, d=4)
tryCatch({
    elemento <- dicionario[["e"]]
},error = function(e){
    message("Erro: essa chave não existe no dicionário")
})


log_calculator <- function(x){
    tryCatch(
        expr = {
            message(log(x))
            message("Successfully executed the log(x) call.")
        },
        error = function(e){
            message('Caught an error!')
            print(e)
        },
        warning = function(w){
            message('Caught an warning!')
            print(w)
        },
        finally = {
            message('All done, quitting.')
        }
    )    
}

log_calculator(10)

string <- "abc"

tryCatch(
    expr ={
        numero <- as.integer(string)
}, warning = function(w){
    print("Erro: conversão de string para inteiro falhou")
})

dicionario <- list(a = c(1,2,3), b = c(4,5,6))
tryCatch({
    elemento <- dicionario[["c"]][1]
}, error = function(e){
    if(inherits(e, "simpleError")){
        print("Error: chave inexistente no dicionario ou indice fora dos limites da lista")
    }
})