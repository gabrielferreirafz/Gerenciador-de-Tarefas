"""
Módulo responsável por Iniciar e tratar uma Tarefa
"""
from statusEprazo import Status_e_Prazo
from prioridade import Prioridade

class Tarefas:
    def __init__(self,titulo,prazo,prioridade):
        """
        Inicia uma nova tarefa com titulo, prazo e prioridade
        
        :param titulo: Nome da tarefa
        :type titulo: str
        :param status_prazo: Prazo da tarefa no formato DD/MM/YYYY e status da tarefa já por padrão como "Pendente"
        :type status_prazo: str 
        :param prioridade: Prioridade da tarefa
        :type prioridade: str
        """
        self.titulo = titulo
        self.status_prazo = Status_e_Prazo('pendente', prazo)
        self.prioridade = Prioridade(prioridade)

    def __str__(self):
        """
        Retorna o título de uma tarefa 
        
        :return: retorna a exibição apenas do título de uma tarefa
        :rtype: str
        """
        return self.titulo
    
    def exibição_atributos(self):
        return f'Tarefa: {self.titulo} | Status: {self.status_prazo.status_tarefa} | Prazo: {self.status_prazo.prazo_tarefa} | Prioridade: {self.prioridade}'
    
     

    
        

    
        


