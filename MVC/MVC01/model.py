from Dao import *

class ToDo:
    def AdicionarTarefas(self, tarefa):
        self.tarefa = tarefa
        dao = DaoAdicionarTarefa(self.tarefa)
        return dao.AdicionarTarefa()

    def ExcluirTarefa(self, excluir):
        return True
    
    def ListarTarefa(self):
        dao = DaoListarTarefa()
        return dao.listar()

todo = ToDo()