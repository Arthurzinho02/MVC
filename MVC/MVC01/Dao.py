from random import *
Arquivo = "ToDo.txt"

class DaoMudarTarefa:
    def mudarTarefa(self, tarefa_Antiga, tarefa_Nova):
        with open(Arquivo, "r") as arquivo:
            conteudo = arquivo.read()

        conteudo_Atualizado = conteudo.replace(tarefa_Antiga, tarefa_Nova)
        with open(Arquivo, "w") as arquivo2:
            arquivo2.write(conteudo_Atualizado)

class DaoAdicionarTarefa:
    def __init__(self, tarefa):
        self.tarefa = tarefa

    def AdicionarTarefa(self, x):
        with open(Arquivo, "a") as arquivo:
            arquivo.write(f"A\t{x}\t{self.tarefa}\n")
        return True
        
class DaoListarTarefa:
    def listar(self):
        with open(Arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        return linhas
    
    
    






