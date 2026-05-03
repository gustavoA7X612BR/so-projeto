class Snapshot:
    """Classe para representar um snapshot do estado do sistema operacional em um determinado momento."""
    def __init__(self, readyQueue, processors, tasks):
        # O indice do snapshot é o tempo atual do sistema, a fila de prontas, as tarefas em execução nos processadores e as tarefas pendentes
        self.tasks = tasks.copy()  # Cópia da lista de tarefas que ainda não iniciaram
        self.readyQueue = readyQueue.copy()  # Cópia da fila de prontas
        self.processors = [processor.task for processor in processors]  # Lista das tarefas atualmente em execução nos processadores