from model import *

class ControllerMudarTarefa:
    def __init__(self, tarefa_Nova, indice, Letra):
        try:
            indice = int(indice)
            if tarefa_Nova == "":
                print("Digite novamente, tarefa inválida")
            else:

                lista_id = []
                dao = DaoListarTarefa()
                cont = -1
                for tarefas in dao.listar():
                    cont += 1
                    if cont >= 1:
                        letra = tarefas[:1]
                        if letra == "A":
                            lista = tarefas.split("\t", 4)               
                            id = lista[1]
                            id = int(id)
                            lista_id.append(id)
                if indice <= len(lista_id):
                    indice -=1
                    cont = -1
                    for tarefas in dao.listar():
                        cont += 1
                        if cont >= 1:
                            lista = tarefas.split("\t", 4)               
                            id = lista[1]
                            id = int(id)
                            tarefa_A = tarefas[7:-1]
                            if id == lista_id[indice]:
                                if Letra == "A":
                                    tarefa_Atualizada = f"A\t{id}\t{tarefa_Nova}\n"
                                    todo.MudarTarefa(tarefas, tarefa_Atualizada)
                                    break
                                else:
                                    tarefa_Atualizada = f"{Letra}\t{id}\t{tarefa_A}\n"
                                    todo.MudarTarefa(tarefas, tarefa_Atualizada)
                                    break
                else:
                    print("Indice inválido, tente novamente")
        except Exception:
            print("Inválido")


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
                        lista = tarefas.split("\t", 4)               
                        id = lista[1]
                        id = int(id)
                        if x != id: 
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

class ControllerListarTarefa:
    def __init__(self, Letra):
        try:
            cont = -1
            for tarefas in todo.ListarTarefa():
                cont += 1
                if cont >= 1:
                    letra = tarefas[:1]
                    if letra == Letra:
                        tarefas = tarefas[7:-1]
                        print(f"{cont} - {tarefas}")
                    else:
                        cont -= 1
        except Exception:
            print("Inválido")
