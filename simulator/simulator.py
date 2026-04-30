import time
from hardware.hardware import Hardware
from so import So

class Simulator:
    """Simulador do sistema operacional, responsável por criar o hardware, iniciar o sistema operacional e controlar a execução da simulação."""
    def __init__(self, num_processors=4, tasks=[]):
        """Inicializa o simulador com um número especificado de processadores e uma lista de tarefas.
        args:
            num_processors (int): O número de processadores a serem simulados.
            tasks (list): Uma lista de tarefas (TCBs) para serem adicionadas ao sistema operacional.
        """
        hardware = Hardware(num_processors)
        self.os = So(hardware, tasks)
        self.is_running = False
    def start(self):
        print("Simulação iniciada.")
        self.is_running = True
        while self.is_running:
            self.os.run()
            time.sleep(1)  # Simulate time passing between runs

    def stop(self):
        print("Simulação parada.")
        self.is_running = False