import tarefas

class Usuario:
    def __init__(self,nome):
        self.nome = nome
        self.lista_tarefas = []

    def adicionar_tarefa(self, titulo, prazo, prioridade):
        nova_tarefa = tarefas.Tarefas(titulo, prazo, prioridade)
        self.lista_tarefas.append(nova_tarefa)

    def exibir_lista(self):
        print('Lista de Tarefas')
        for tarefa in self.lista_tarefas:
            print(f"-{tarefa.titulo}") # ele ta puxando automatico o __str__ que mostra logo todos os dados de uma tarefa, oq eu não quero. Quero que mostre apenas os titulos das tarefas e somente se o usuario pedir mostrar os dados de uma tarefa especifica

    def remover_tarefa(self, tarefa_removida):
        if tarefa_removida in self.lista_tarefas:
            self.lista_tarefas.remove(tarefa_removida)
            



