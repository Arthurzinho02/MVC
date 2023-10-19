from model import *

class ControllerAdicionarTarefa:
    def __init__(self, tarefa):
        try:
            self.tarefa = tarefa
            if self.tarefa == "":
                print("Digite novamente, tarefa inválida")
            else:
                if todo.AdicionarTarefas(self.tarefa) == True:
                    print("Tarefa adicionada")
                else:
                    print("Tarefa não foi adiconada")
        except Exception:
            print("Inválido")


class ControllerExcluirTarefa:
    def __init__(self, excluir):
        try:
            x = int (excluir)
            self.excluir = x - 1

            if todo.ExcluirTarefa(self.excluir) == True:
                print("Tarefa excluida")
            else:
                print("Tarefa não foi exclui")
        except Exception:
            print("Número Inválido")


class ControllerListarTarefa:
    def __init__(self):
        try:
            cont = -1
            for tarefas in todo.ListarTarefa():
                cont += 1
                if cont >= 1:
                    tarefas = tarefas[7:-1]
                    print(f"{cont} - {tarefas}")
        except Exception:
            print("Inválido")
