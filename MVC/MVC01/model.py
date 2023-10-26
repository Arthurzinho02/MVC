from Dao import *

class ToDo:

    def MudarTarefa(self, tarefa_A, tarefa_N):
        dao = DaoMudarTarefa()
        return dao.mudarTarefa(tarefa_A, tarefa_N)
    
    def AdicionarTarefas(self, tarefa, x):
        self.tarefa = tarefa
        dao = DaoAdicionarTarefa(self.tarefa)
        return dao.AdicionarTarefa(x)
    
    def ListarTarefa(self):
        dao = DaoListarTarefa()
        return dao.listar()

todo = ToDo()