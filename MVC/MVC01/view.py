from controller import *
import os

print("Bem vindo ao Todo")
while True:
    print("Qual você deseja: \n[1] Adicionar \n[2] Excluir \n[3] Listar \n[4] Sair")
    opção = input(">> ")
    os.system("cls")
    match opção:
        case "1":
            tarefa = input("Digite a tarefa: ")
            adicionartarefa = ControllerAdicionarTarefa(tarefa)
            os.system("pause")
            os.system("cls")        
        case "2":
            print("Lista:")
            listartarefa = ControlarListarTarefa()
            excluir = input("Digite o índice da tarefa a ser excluida: ")
            excluirtarefa = ControllerExcluirTarefa(excluir)
            os.system("pause")
            os.system("cls")
            print("Lista Nova:")        
            listartarefa = ControlarListarTarefa()
            os.system("pause")
            os.system("cls")


        case "3":
            listartarefa = ControlarListarTarefa()
            os.system("pause")
            os.system("cls")        

        case "4":
            break
            
        case _:
            print("Inválido")

                   