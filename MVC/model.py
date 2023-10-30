from Dao import *

class ToDo:

    def MudarTarefa(self, tarefa_A, tarefa_N):
        dao = DaoMudarTarefa()
        return dao.mudarTarefa(tarefa_A, tarefa_N)
    
    def AdicionarTarefas(self, tarefa):
        dao = DaoAdicionarTarefa(tarefa)
        return dao.AdicionarTarefa()
    
    def ListarTarefa(self):
        dao = DaoListarTarefa()
        return dao.listar()

todo = ToDo()