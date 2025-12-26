"""
Módulo responsável por definir e tratar a prioridade de uma tarefa
"""
class Prioridade():
    def __init__(self,prioridade):
        """
        Inicia uma Tarefa com prioridade
        
        :param prioridade: nível de prioridade de uma tarefa (Emergencial, Alta, Média ou Baixa)
        :type prioridade: str
        """
        self.prioridade = prioridade

    def alterar_prioridade(self,nova_prioridade):
        """
        Altera o nível de Prioridade da Tarefa(objeto)
        
        :param nova_prioridade: novo nível de prioridade de uma tarefa
            (Emergencial, Alta, Média ou Baixa)
        :type nova_prioridade: str
        """
        self.prioridade = nova_prioridade

    def __str__(self):
        """
        Retorna a prioridade da tarefa

        :return: retorna a prioridade da tarefa
        :rtype: str
        """
        return self.prioridade
    
