def adcionar_tarefa(tarefas):
    descricao = input ("\nDescrição da tarefa: ")
    prioridade = input("\nPrioridade ( 1 -5, 1 = mais baixa: ")
    
    while not (prioridade.isdigit() and 1<= int(prioridade) <= 5):
        print ("\nDigite um valor de 1 a 5")
        prioridade = input("\nPrioridade ( 1 -5, 1 = mais baixa: ")

    tarefa = {
        "descricao": descricao,
        "prioridade": int(prioridade),
        "status" : "pendente"
        
    }
    
    tarefas.append(tarefa)
    
def pegar_prioridade(tarefas):
    return tarefas ["prioridade"]
    
def listar_tarefa(tarefas):
    if len(tarefas) == 0:
        print("\n nenhuma tarefa")
        return
    
    tarefas.sort(key = pegar_prioridade)
    
    print ("\n TAREFAS")
    for i , t in enumerate (tarefas):
        print (f"{i +1 }. {t["descricao"]} [prioridade: {t["prioridade"]}] - Status: {t["status"]}")


def marcar_tarefa(tarefas):
    if len(tarefas) == 0:
        print("\n nenhuma tarefa para macar")
        return
    
    listar_tarefa(tarefas)
    
    escolha = input("\nDigite a tarefa concluida: ")
    
    while not (escolha.isdigit() and 1<= int(escolha) <= len(tarefas)):
        print ("\nDigite o valor da tarefa")
        escolha = input("\nDigite a tarefa concluida: ")
    
    
    indice = int(escolha) - 1
    
    tarefas[indice]["status"] = "concluida"
    print ("tarefa marcada como concluida")
    
    
    
def main():
    tarefas = []
    while True:
        print ("\n\n==MENU==")
        print ("\n 1 - Adcionar tarefas")
        print ("\n 2 - Listar tarefas")
        print ("\n 3 - Marca tarefa como concluida")
        print ("\n 4 - Sair")
        
        escolha = input("\n Escolha uma opcao: ")
        
        if escolha == "1":
            adcionar_tarefa(tarefas)
            
        elif escolha == "2":
            listar_tarefa(tarefas)
            
        elif escolha == "3":
            marcar_tarefa(tarefas)
        
        elif escolha == "4":
            print("\n obrigado")
            break
        
        else:
            print ("\n escolha opcao valida!")
            
    
 #if __name__ == "__main__":
main()