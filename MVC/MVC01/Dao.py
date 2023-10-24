from random import *
Arquivo = "ToDo.txt"

class DaoAdicionarTarefa:
    def __init__(self, tarefa):
        self.tarefa = tarefa

    def AdicionarTarefa(self, x):
        with open(Arquivo, "a") as arquivo:
            arquivo.write(f"{x} \t {self.tarefa}\n")
        return True
        
class DaoListarTarefa:
    def listar(self):
        with open(Arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        return linhas
    
    
    






