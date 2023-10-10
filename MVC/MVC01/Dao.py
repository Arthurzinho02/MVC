Arquivo = "ToDo.txt"
        
class DaoAdicionarTarefa:
    def __init__(self, tarefa):
        self.tarefa = tarefa

    def AdicionarTarefa(self):
        with open(Arquivo, "a") as arquivo:
            arquivo.write(f"{self.tarefa}\n")
        return True
        
class DaoListarTarefa:
    def listar(self):
        with open(Arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        return linhas
    
    
    






