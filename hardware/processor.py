class Processor:
    """Simula um processador do sistema operacional, capaz de executar tarefas e interagir com o clock."""
    def __init__(self, clock):
        """Inicializa o processador com uma referência ao clock do sistema.
            args:
                clock (Clock): O clock do sistema para sincronização de tempo.
        """
        self.clock = clock
        self.isOn = False
        self.task = None

    def setTask(self, task):
        self.task = task
        self.isOn = True

    def removeTask(self):
        task = self.task
        self.task = None
        return task

    def execute(self):
        """Executa uma tarefa no processador, simulando o processamento e a passagem do tempo.
            args:
                task (tcb): A tarefa a ser executada pelo processador.
        """
        self.isOn = True
        if self.task:
            print(f"Processando {self.task} no processador. Tempo restante: {self.task.remaining_time}")
            self.task.remaining_time -= 1  # Simula o processamento da tarefa, reduzindo o tempo restante
    def shutdown(self):
        self.isOn = False
        self.task = None