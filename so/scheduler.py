class Scheduler:
    """Escalonador de tarefas do sistema operacional, responsável por gerenciar as tarefas prontas e em espera, e decidir qual tarefa deve ser executada a seguir."""
    def __init__(self, hardware):
        self.hardware = hardware
        self.ready_queue = []  # List of TCBs that are ready to run
        #self.waiting_queue = []  # List of TCBs that are waiting for an event
        self.current_task = None  # The currently running task

    def add_task(self, tcb):
        self.ready_queue.append(tcb)

    def schedule(self):
        for processor in self.hardware.processors:
            if not processor.isOn:  # If the processor is idle
                if self.ready_queue:
                    self.current_task = self.ready_queue.pop(0)  # Get the next task from the ready queue
                    self.current_task.state = 'running'
                else:
                    processor.shutdown()  # No tasks to run, shut down the processor