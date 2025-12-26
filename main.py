from usuarios import Usuario
from tarefas import Tarefas
import os

def menu():
    print(
        '1- Criar e Adicionar nova tarefa\n'
        '2- Remover tarefa da lista\n'
        '3- Editar uma tarefa da lista\n'
        '4- Ver lista de tarefas\n'
        '5- Sair do programa\n'
    )
print('Seja bem vindo ao gerenciador de Tarefas')
nome_usuario = input('Qual seu nome? ').lower()
usuario = Usuario(nome_usuario)
while True:
    menu()
    acao_usuario = int(input('Qual ação você deseja realizar: '))
    if acao_usuario == 1:
        titulo = input('Informe o nome da nova tarefa: ').lower()
        prazo = input('Qual será o prazo da tarefa:')
        prioridade = input('Qual será o nível de prioridade da tarefa: ').lower()
        usuario.adicionar_tarefa(titulo,prazo,prioridade)
    elif acao_usuario == 2:
        usuario.exibir_lista()
        tarefa_excluida = input('qual tarefa da lista você deseja excluir: ').lower()
        if tarefa_excluida in usuario.lista_tarefas:
            usuario.remover_tarefa(tarefa_excluida)
    elif acao_usuario == 4:
        usuario.exibir_lista()
        tarefa_especifica = input('deseja ver os atributos de uma tarefa específica da lista: ')
        for item in usuario.lista_tarefas:
            if item == tarefa_especifica:
    
                #usuario.lista_tarefas.index(item)
                #usuario.lista_tarefas[1] #é onde cada objeto fica armazenado agora
                # o certo é eu criar essa função na class usuario pois a conexão com a class tarefa é melhor e aqui eu apenas puxo chamando a função
