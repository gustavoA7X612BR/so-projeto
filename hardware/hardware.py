from hardware.clock import Clock
from hardware.processor import Processor

class Hardware:
    """
    Simula o hardware do sistema operacional, incluindo o clock e os processadores.
    """
    def __init__(self, num_processors):
        """Inicializa o hardware com um número especificado de processadores e um clock."""
        self.clock = Clock()
        self.processors = [Processor(self.clock) for _ in range(num_processors)]
    def run(self, task=None): 
        """Simula a execução do hardware, processando tarefas nos processadores.
            args:
                task (tcb): A tarefa a ser processada (opcional). Se None, os processadores ficarão ociosos.
        """
        self.clock.tick()  # Simulate time passing
        for processor in self.processors:
            if not processor.isOn:
                print(f"Processador {self.processors.index(processor)} está desligado.")
            else:
                processor.execute()  # Simulate the processor executing a task