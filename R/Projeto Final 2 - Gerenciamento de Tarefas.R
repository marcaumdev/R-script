tarefas <- list(
  "tarefa1"<-list(tarefa = "Arrumar Quarto", status = FALSE),
  "tarefa2"<-list(tarefa = "Tirar Lixo", status = TRUE),
  "tarefa3"<-list(tarefa = "Lavar Roupa", status = TRUE),
  "tarefa4"<-list(tarefa = "Varrer cozinha", status = FALSE)
)

for(tarefa in tarefas){
  print(paste("Tarefa:", tarefa$tarefa, "Status:", tarefa$status))
}

tarefas <- c(tarefas, list("tarefa5"<-list(tarefa = "Passear com cachorro", status = TRUE)))

print("")

for(tarefa in tarefas){
  print(paste("Tarefa:", tarefa$tarefa, "Status:", tarefa$status))
}

tarefaFeita <- tarefas[4] 
tarefaFeita$status <- TRUE
tarefas[4] <- tarefaFeita

print("")

for(tarefa in tarefas){
  print(paste("Tarefa:", tarefa$tarefa, "Status:", tarefa$status))
}