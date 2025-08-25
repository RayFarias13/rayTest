notas = []

def adcionar_nota():
    nome = input("\nNome do aluno: ").strip()
    while nome == "":
        print("\nnome nao pode esta vazio\n")
        nome = input("\nNome do aluno: ").strip()
    
    nota = input("\nNota do aluno (0 - 10): ").strip()
    #.isdigit nao funciona com float
    while not nota.replace(".","").isdigit or not ( 0 <= float(nota)<=10):
        # ponto(.), na verificacao o isdigit nao considera, entao mudar temporariamente apenas para passar na verificacao.
        print("nota invalida, digite um numero entre 0 - 10")
        nota = input("\nNota do aluno(0 - 10): ").strip()


    disciplina = input("\nDisciplina: ").strip()
    while disciplina == "":
        print("\nDisciplina nao pode esta vazia")
        disciplina = input("\nDisciplina: ").strip()




    notas.append((nome,nota,disciplina)):
    print("\nNota adicionada com sucesso.\n")

def melhor_disciplina():
    if len(notas) == 0:
        print("\nnenhuma nota cadastrada")
        return

    disciplinas  = []

    for n in notas:
        if in n [2] not in disciplinas:
            disciplinas.append(n[2])


    print ("melhor aluno por disciplina: \n")


    for d in disciplinas:
        melhor_nota = -1
        melhor_aluno = ""

        for n in notas:
            if n[2] == d and n[1] > melhor_nota:
                melhor_nota = n[1]
                melhor_aluno = n[0]

        print (f"{d}:{melhor_aluno} {melhor_nota}")






def consultar_aluno():
    pass


def obter_nota(tupla):
    return tupla[1]

def exibir_ordenadas():
    if len(notas) == 0:
        print("\nnenhuma nota cadastrada")
        return
    
    ordenadas = sorted(notas,key=obter_nota, reverse=True)

    print("\n Notas ordenadas")
    for n in ordenadas:
        print(f"{n[1]:.2f}, {n[0]}, {n[2]}")


def main():

    while True:
        print ("\n\n==MENU==")
        print ("\n 1 - Adcionar aluno e nota")
        print ("\n 2 - Listar melhor aluno")
        print ("\n 3 - Listar nota por aluno")
        print ("\n 3 - Listar notas por ordem  decrescente")
        print ("\n 5 - Sair")
        
        escolha = input("\n Escolha uma opcao: ")
        
        if escolha == "1":
            adcionar_nota()
            
        elif escolha == "2":
            melhor_disciplina()
            
        elif escolha == "3":
            consultar_aluno()
        
        elif escolha == "4":
            exibir_ordenadas()

        elif escolha == "5":
            print ("obrigado")
            break
        
        else:
            print ("\n escolha opcao valida!")
            



if __name__ == "__main__":
    main()