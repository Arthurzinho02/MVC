from model import *

class ControllerAdicionarTarefa:
    def __init__(self, tarefa):
        try:
            self.tarefa = tarefa
            x = randint(1000,9999)
            cont = -1
            if len(todo.ListarTarefa()) > 1:
                for tarefas in todo.ListarTarefa():
                    cont += 1
                    if cont >= 1:
                        tarefas = tarefas[:4]
                        tarefas = int(tarefas)
                        if x != tarefas: 
                            if self.tarefa == "":
                                print("Digite novamente, tarefa inválida")
                            else:
                                if todo.AdicionarTarefas(self.tarefa, x) == True:
                                    print("Tarefa adicionada")
                                    break
                                else:
                                    print("Tarefa não foi adiconada")
                                    break
                        else:
                            x = randint(1000,9999)
            else:
                if self.tarefa == "":
                    print("Digite novamente, tarefa inválida")
                else:
                    if todo.AdicionarTarefas(self.tarefa, x) == True:
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
