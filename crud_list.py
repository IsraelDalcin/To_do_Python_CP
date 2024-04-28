from tarefa import Tarefa

# Classe responsável por fazer as funcionalidades da nossa lista de tarefa. Ela contém os métodos
class TarefaComListaDao:
    def __init__(self):
        self.tarefas = []
        self.id_counter = 0
    
    # Método para inserir tarefas
    def insert(self, titulo, descricao, data_venc_tarefa):
        tarefa = Tarefa(self.id_counter, titulo, descricao, data_venc_tarefa, 'Pendente')
        #self.tarefas.append(tarefa)
        self.id_counter += 1
        id = self.id_counter
        with open('arquivo.txt', 'a') as file:
            file.write(f"{id}| {tarefa.titulo}| {tarefa.descricao}| {tarefa.data_venc_tarefa}| Pendente\n")

    # Método para consultar todas as tarefas
    def selectAll(self):
        tarefas = []
        with open('arquivo.txt', 'r') as file:
            for line in file:
                id, titulo, descricao, data_venc_tarefa, status = line.strip().split('| ')
                tarefa = Tarefa(int(id), titulo, descricao, data_venc_tarefa, status)
                tarefas.append(tarefa)
        return tarefas

    # Método para atualizar uma tarefa
    def update(self, id_tarefa, titulo, descricao, data_venc_tarefa,  status):
        tarefas_atualizadas = []
        with open('arquivo.txt', 'r') as file:
            for line in file:
                id, titulo_antigo, descricao_antiga, data_venc_tarefa_antiga, status_antigo = line.strip().split('| ')
                if int(id) == id_tarefa:
                    tarefa_atualizada = Tarefa(id_tarefa, titulo, descricao, data_venc_tarefa, status)
                    tarefas_atualizadas.append(tarefa_atualizada)
                else:
                    tarefa_original = Tarefa(int(id), titulo_antigo, descricao_antiga, data_venc_tarefa_antiga, status_antigo)
                    tarefas_atualizadas.append(tarefa_original)

        with open('arquivo.txt', 'w') as file:
            for tarefa in tarefas_atualizadas:
                file.write(f"{tarefa.id_tarefa}| {tarefa.titulo}| {tarefa.descricao}| {tarefa.data_venc_tarefa}| {tarefa.status}\n")

    # Método para atualizar um único atributo, caso o usuário queira atualizar só o "título" por exemplo
    def update_unico(self, id_tarefa, titulo : str='', descricao : str='', data_venc_tarefa : str='', status : str=''):
        tarefas_atualizadas = []
        with open('arquivo.txt', 'r') as file:
            for line in file:
                id, titulo_antigo, descricao_antiga, data_venc_tarefa_antiga, status_antigo = line.strip().split('| ')
                if int(id) == id_tarefa:
                    if titulo != '':
                        tarefa_atualizada = Tarefa(id_tarefa, titulo, descricao_antiga, data_venc_tarefa_antiga, status_antigo)
                        tarefas_atualizadas.append(tarefa_atualizada)
                    elif descricao != '':
                        tarefa_atualizada = Tarefa(id_tarefa, titulo_antigo, descricao, data_venc_tarefa_antiga, status_antigo)
                        tarefas_atualizadas.append(tarefa_atualizada)
                    elif data_venc_tarefa != '':
                        tarefa_atualizada = Tarefa(id_tarefa, titulo_antigo, descricao_antiga, data_venc_tarefa, status_antigo)
                        tarefas_atualizadas.append(tarefa_atualizada)
                    elif status != '':
                        tarefa_atualizada = Tarefa(id_tarefa, titulo_antigo, descricao_antiga, data_venc_tarefa_antiga, status)
                        tarefas_atualizadas.append(tarefa_atualizada)
                else:
                    tarefa_original = Tarefa(int(id), titulo_antigo, descricao_antiga, data_venc_tarefa_antiga, status_antigo)
                    tarefas_atualizadas.append(tarefa_original)

        with open('arquivo.txt', 'w') as file:
            for tarefa in tarefas_atualizadas:
                file.write(f"{tarefa.id_tarefa}| {tarefa.titulo}| {tarefa.descricao}| {tarefa.data_venc_tarefa}| {tarefa.status}\n")

    # Método para deletar uma tarefa
    def delete(self, id_tarefa):
        with open('arquivo.txt', 'r') as file:
            lines = file.readlines()

        found = False
        with open('arquivo.txt', 'w') as file:
            for line in lines:
                print(line)
                parts = line.strip().split('| ')
                if parts[0] == str(id_tarefa):
                    found = True
                else:
                    file.write(line)
        if found:
            print(f"Tarefa com ID {id_tarefa} deletada com sucesso.")
        else:
            print(f"Tarefa com ID {id_tarefa} não encontrada.")

    # Método para selecionar pelo nome
    def select_by_name(self, id_tarefa):
        for tarefa in self.selectAll():
            if tarefa.id_tarefa == int(id_tarefa):
                return tarefa

    def troca_id(self, id_counter):
        if id_counter != 0:
            self.id_counter = id_counter





