"""
Módulo responsável por gerenciar status e prazo de uma tarefa
"""
import datetime

class Status_e_Prazo:
    """
    Classe responsável por definir e tratar o status e prazo de uma tarefa(objeto)
    """
    def __init__(self,status_tarefa,prazo_tarefa):
        """
        Inicia o status e o prazo de uma tarefa(objeto)
        
        :param status_tarefa: status de uma tarefa (Concluída, Em andamento, Pendente e Atrasada)
        :type status_tarefa: str
        :param prazo_tarefa: prazo para conclusão da tarefa no formato DD/MM/YYYY
        :type prazo_tarefa: str

        :raises ValueError: se o prazo estiver no formato errado do strptime
        """
        self.status_tarefa = status_tarefa
        self.prazo_tarefa = datetime.datetime.strptime(prazo_tarefa, "%d/%m/%Y")

    def alterar_status(self,novo_estado):
        """
        Altera o status de uma tarefa existente(objeto)
        
        :param novo_estado: novo status que a tarefa vai assumir
        :type novo_estado: str
        """
        self.status_tarefa = novo_estado

    def check_atraso(self):
        """
        Checa se uma tarefa está atrasada ou não

        Se o prazo da tarefa for menor que a data atual, o status da tarefa é alterado para "Atrasado". Senão, o status permanece o mesmo.
        """
        if self.prazo_tarefa < datetime.datetime.now():
            self.alterar_status('atrasado')
        else:
            pass

    def tempo_restante(self):
        """
        Calcula o tempo que resta para a tarefa ser concluída (prazo da tarefa - data/hora atual)

        :return: tempo que resta para concluir a tarefa
        :rtype: datetime.timedelta 
        """
        tempo_restante = self.prazo_tarefa - datetime.datetime.now()
        return tempo_restante

    def __str__(self):
        """
        Retorna o status da tarefa
        
        :return: retorna o status da instância
        :rtype: str
        """
        return self.status_tarefa
