import os

class Gerenciador_Tarefas():
    def __init__(self):
        self.lista_tarefas = [] 
    
    def adicionar_tarefas(self, tarefa_nova):
        self.lista_tarefas.append(tarefa_nova)
        print('A tarefa foi adicionada com sucesso!')

    def remover_tarefa(self, tarefa_removida):
        self.lista_tarefas.pop(self.lista_tarefas.index(tarefa_removida))
        print('A tarefa foi removida com sucesso!')

    def ver_lista_tarefas(self):
        os.system('cls')
        print('Lista de tarefas:')
        for tarefa in self.lista_tarefas:
            print(f'-{tarefa}')

    def editar_tarefa(self, tarefa_editada):
        self.lista_tarefas[self.lista_tarefas.index(tarefa_editada)] = input('Qual a alteração que deseja fazer: ')
        print('Tarefa alterada com sucesso!')

fechar_programa = False #flag que utilizo para dar stop no while quando o usuário deseja sair do programa
usuario = Gerenciador_Tarefas()
while fechar_programa == False:
    print(
    'Gerenciador de Tarefas\n'
    '1- Ver todas as tarefas\n'
    '2- Adicionar uma nova tarefa\n'
    '3- Remover uma tarefa\n'
    '4- Editar uma tarefa da lista\n'
    '5- Sair do programa'
    )
    try:
        acao_usuario = int(input('Informe o que você deseja fazer: '))
        if acao_usuario == 1:
            os.system('cls')
            usuario.ver_lista_tarefas()
            input('Pressione Enter para voltar ao menu inicial: ')
            os.system('cls')
        elif acao_usuario == 2:
            os.system('cls')
            new_task = input('Qual tarefa deseja adicionar: ').lower()
            usuario.adicionar_tarefas(new_task)
            input('Pressione Enter para voltar ao menu inicial: ')
            os.system('cls')
        elif acao_usuario == 3:
            os.system('cls')
            usuario.ver_lista_tarefas()
            task_removed = input('Informe a Tarefa que deseja remover: ').lower()
            usuario.remover_tarefa(task_removed)
            input('Pressione enter para voltar ao menu inicial: ')
            os.system('cls')
        elif acao_usuario == 4:
            os.system('cls')
            usuario.ver_lista_tarefas()
            tarefa_editada = input('Informe a tarefa que deseja alterar: ')
            usuario.editar_tarefa(tarefa_editada)
            input('Pressione enter para voltar ao menu: ')
            os.system('cls')
        elif acao_usuario == 5:
            os.system('cls')
            print('Programa Finalizado')
            fechar_programa = True
        else: # Tratamento de erro para escolha de opção indisponível no menu
            os.system('cls')
            print('Informe uma das opções disponíveis!')
            input('Pressione enter para voltar ao menu: ')
            os.system('cls')
    except ValueError: # Tratamento de erro para valores errados (não números)
        os.system('cls')
        print('Informe um valor válido!')
        input('pressione enter para voltar ao menu principal: ')
        os.system('cls')