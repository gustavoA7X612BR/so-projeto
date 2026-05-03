import time
from hardware.hardware import Hardware
from simulator.snapshot import Snapshot
from so import So

class Simulator:
    """Simulador do sistema operacional, responsável por criar o hardware, iniciar o sistema operacional e controlar a execução da simulação."""
    def __init__(self, mode, num_processors=4, tasks=[]):
        """Inicializa o simulador com um número especificado de processadores e uma lista de tarefas.
        args:
            num_processors (int): O número de processadores a serem simulados.
            tasks (list): Uma lista de tarefas (TCBs) para serem adicionadas ao sistema operacional.
        """
        hardware = Hardware(num_processors)
        self.mode = mode
        self.os = So(hardware, tasks)
        self.is_running = False
        self.snapshots = []  # Lista para armazenar os snapshots do estado do sistema
    def start(self):
        print("Simulação iniciada.")
        if self.mode == "step":
            print("Modo de simulação: Step-by-step. Pressione Enter para avançar cada passo.")
        self.is_running = True
        while self.is_running:
            if self.mode == "step":
                input("")
            self.run()

    def run(self):
        """Executa a simulação, processando as tarefas e atualizando o estado do sistema operacional."""
        self.os.run()
        # Create a snapshot of the current state
        snapshot = Snapshot(
            readyQueue=self.os.readyQueue,
            processors=self.os.hardware.processors,
            tasks=self.os.tasks
        )
        self.snapshots.append(snapshot)
        time.sleep(1)  # Simulate time passing between runs

    def retrocede(self):
        """Permite retroceder a simulação para um estado anterior, utilizando os snapshots armazenados."""
        if self.snapshots:
            last_snapshot = self.snapshots.pop()  # Remove o último snapshot da lista
            # Restaura o estado do sistema operacional com base no snapshot
            self.os.readyQueue = last_snapshot.readyQueue
            for processor, task in zip(self.os.hardware.processors, last_snapshot.processors):
                processor.task = task
                processor.isOn = bool(task)  # Define o estado do processador com base na presença de uma tarefa
            self.os.tasks = last_snapshot.tasks
            print("Simulação retrocedida para o estado anterior.")
        else:
            print("Não há snapshots disponíveis para retroceder.")

    def stop(self):
        print("Simulação parada.")
        self.is_running = False