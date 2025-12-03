'''
Inicio
    print Interface menu
    input oq o usuário quer fazer
        validação de escolha do usuario
    1. ver lista de tarefas
        melhorar a lista de tarefas visualmente
    2. add tarefa
        validação de tarefa
        add tarefa
        volta para o menu
    3. remover tarefa
        validação de tarefa
        remover tarefa
        volta para o menu
    4. editar tarefa preexistente
    5. Sair do programa
Fim
'''
import os
lista_tarefas = []

def adicionar(tarefa):
    lista_tarefas.append(tarefa)
    print('A tarefa foi adicionada com sucesso!')

def remover(tarefa):
    lista_tarefas.remove(tarefa)
    print('A tarefa foi removida com sucesso!')

def ver_tarefas(lista):
    print(lista)

def menu():
    print(
    'Gerenciador de Tarefas\n'
    '1- Ver todas as tarefas\n'
    '2- Adicionar uma nova tarefa\n'
    '3- Remover uma tarefa\n'
    '4- Editar uma tarefa da lista\n'
    '5- Sair do programa'
    )

fechar_programa = False
while fechar_programa == False:
    menu()
    acao_usuario = int(input('Informe o que você deseja fazer: '))
    if acao_usuario == 1:
        os.system('cls')
        print('Lista de tarefas:')
        for tarefa in lista_tarefas:
            print(f'-{tarefa}')
        input('Pressione Enter para voltar ao menu inicial: ')
        os.system('cls')
    elif acao_usuario == 2:
        os.system('cls')
        nova_tarefa = input('informe a nova tarefa que deseja adicionar: ')
        adicionar(nova_tarefa)
        input('Pressione Enter para voltar ao menu inicial: ')
        os.system('cls')
    elif acao_usuario == 3:
        os.system('cls')
        ver_tarefas(lista_tarefas)
        tarefa_deletada = input('informe a tarefa que você deseja excluir da lista: ').lower()
        lista_tarefas.pop(lista_tarefas.index(tarefa_deletada))
        print('Tarefa excluída com sucesso!')
        input('Pressione enter para voltar ao menu inicial: ')
        os.system('cls')
    elif acao_usuario == 4:
        os.system('cls')
        ver_tarefas(lista_tarefas)
        tarefa_edit = input('qual tarefa você deseja editar: ').lower() 
        lista_tarefas[lista_tarefas.index(tarefa_edit)] = input('Qual a alteração que deseja fazer: ')
        print('Tarefa alterada com sucesso!')
        input('Pressione enter para voltar ao menu: ')
        os.system('cls')
    elif acao_usuario == 5:
        os.system('cls')
        print('Programa Finalizado')
        fechar_programa = True
