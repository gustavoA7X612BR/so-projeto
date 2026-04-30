class Processor:
    """Simula um processador do sistema operacional, capaz de executar tarefas e interagir com o clock."""
    def __init__(self, clock):
        """Inicializa o processador com uma referência ao clock do sistema.
            args:
                clock (Clock): O clock do sistema para sincronização de tempo.
        """
        self.clock = clock
        self.isOn = False
    def execute(self, task):
        """Executa uma tarefa no processador, simulando o processamento e a passagem do tempo.
            args:
                task (tcb): A tarefa a ser executada pelo processador.
        """
        self.isOn = True

        if task:
            task.remaining_time -= 1  # Simula o processamento da tarefa, reduzindo o tempo restante
            print(f"Processando {task} no processador. Tempo restante: {task.remaining_time}")
        else:
            self.shutdown()
    def shutdown(self):
        """Desliga o processador, indicando que ele não está mais executando tarefas."""
        self.isOn = False