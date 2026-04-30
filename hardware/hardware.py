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
        # Run the hardware, for example by executing processes on the processors
        print(f"Thick: {self.clock.current_time}")
        self.clock.tick()  # Simulate time passing
        for processor in self.processors:
            if not processor.isOn:
                processor.execute(task)  # Execute a task on the processor     