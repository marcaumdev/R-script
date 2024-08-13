dicionario <- list(a=1, b=2, c=3, d=4)
string <- readline(prompt = "Digite um valor: ")

while(string %in% dicionario){
    string <- readline(prompt = "Digite um valor: ")
}