from controller import *
import os

print("Bem vindo ao Todo")
while True:
    print("Qual você deseja: \n[1] Adicionar tarefa \n[2] Listar tarefa \n[3] Alterar tarefa \n[4] Concluir Tarefa \n[5] Listar tarefas concluidos \n[6] Excluir\n[7] Sair")
    opção = input(">> ")
    os.system("cls")
    match opção:
        case "1":
            print("===Adiconar===")
            tarefa = input("Digite a tarefa: ")
            adicionartarefa = ControllerAdicionarTarefa(tarefa)
            os.system("pause")
            os.system("cls")        

        case "2":
            print("===Lista===")
            listartarefa = ControllerListarTarefa("A")
            os.system("pause")
            os.system("cls")      

        case "3":
            print("===Alterar===")
            listartarefa = ControllerListarTarefa("A")
            indice = input("Digite o indice da tarefa a ser alterada: ")
            tarefa_nova = input("Digite a nova tarefa: ")
            mudartarefa = ControllerMudarTarefa(tarefa_nova, indice, "A")
            os.system("pause")
            os.system("cls")      

        case "4":
            print("===Concluir===")
            print("Lista:")
            listartarefa = ControllerListarTarefa("A")
            indice = input("Digite o índice da tarefa a ser concluida: ")
            excluirtarefa = ControllerMudarTarefa("  ", indice, "C")
            os.system("pause")
            os.system("cls")

        case "5":
            print("===Lista das concluidas===")
            listartarefa = ControllerListarTarefa("C")
            os.system("pause")
            os.system("cls")   

        case "6":
            print("===Exluir===")
            print("Lista:")
            listartarefa = ControllerListarTarefa("A")
            indice = input("Digite o índice da tarefa a ser excluida: ")
            excluirtarefa = ControllerMudarTarefa("  ", indice, "E")
            os.system("pause")
            os.system("cls")

        case "7":
            break
            
        case _:
            print("Inválido")

                   