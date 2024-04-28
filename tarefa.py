# Nossa classe das tarefas. Aqui armazenamos cada uma das tarefas
class Tarefa:
    def __init__(self, id_tarefa, titulo, descricao, data_venc_tarefa, status):
        self.id_tarefa = id_tarefa
        self.titulo = titulo
        self.descricao = descricao
        self.data_venc_tarefa = data_venc_tarefa
        self.status = status

    def __str__(self):
        return f"{self.id_tarefa} - Título: {self.titulo} | Descrição: {self.descricao} | Prazo: {self.data_venc_tarefa} | Status: {self.status}"