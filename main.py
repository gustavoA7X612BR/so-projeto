import sys
from simulator import Simulator
from so.tcb import tcb

"""class tcb:
    ""Estrutura de dados para representar o Control Block de uma tarefa (TCB) no sistema operacional.""
    def __init__(self, task_id, priority, color="#FFFFFF",startTime=0, duration=0):
        self.task_id = task_id
        self.priority = priority
        self.color = color

        self.state = 'ready'  # Possible states: 'ready', 'running', 'waiting', 'terminated'
        self.context = None  # Placeholder for the task's context (e.g., registers, stack pointer)
        self.remaining_time = duration  # Time remaining for the task to complete (for simulation purposes)
        self.startTime = startTime  # Time when the task is created or scheduled to start

    def __repr__(self):
        return f"TCB(task_id={self.task_id}, priority={self.priority}, state='{self.state}')"
"""
tarefas = [
    # TCB(task_id, start_time, duration)
    tcb(1, 2, "ff0000", 0, 5), # Task 1 starts at time 1 and runs for 5 time units
    tcb(2, 3, "00ff00", 0, 2), # Task 2 starts at time 1 and runs for 5 time units
    tcb(3, 1, "0000ff", 1, 4), # Task 3 starts at time 7 and runs for 5 time units
    tcb(4, 4, "ffff00", 3, 1), # Task 4 starts at time 7 and runs for 5 time units
    tcb(5, 5, "ff00ff", 5, 2), # Task 5 starts at time 7 and runs for 5 time units
]

num_processors = int(sys.argv[1]) if len(sys.argv) > 1 else 1
mode = sys.argv[2] if len(sys.argv) > 2 else "auto"

simulator = Simulator(mode, num_processors, tarefas)
simulator.start()