from so.scheduler import Scheduler

class So:
    def __init__(self, hardware, algorithm, tasks=[]):
        self.hardware = hardware
        self.scheduler = Scheduler(hardware, tasks, algorithm)

    def run(self):
        self.scheduler.schedule()  # Executa o escalonamento das tarefas, que por sua vez executa as tarefas nos processadores e interage com o clock do hardware

        self.hardware.run()
