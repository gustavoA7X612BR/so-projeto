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
    # Lista de tarefas do livro do professor Maziero
    tcb(1, 2, "ff0000", 0, 5), # Task 1 starts at time 1 and runs for 5 time units
    tcb(2, 3, "00ff00", 0, 2), # Task 2 starts at time 1 and runs for 5 time units
    tcb(3, 1, "0000ff", 1, 4), # Task 3 starts at time 7 and runs for 5 time units
    tcb(4, 4, "ffff00", 3, 1), # Task 4 starts at time 7 and runs for 5 time units
    tcb(5, 5, "ff00ff", 5, 2), # Task 5 starts at time 7 and runs for 5 time units
]

num_processors = int(sys.argv[1]) if len(sys.argv) > 1 else 1
algorithm = sys.argv[2] if len(sys.argv) > 2 else "FCFS"
mode = sys.argv[3] if len(sys.argv) > 3 else "auto"

accepted_algorithms = ["FCFS", "SJF", "SRTF", "RR", "PRIOc", "PRIOp"]

algorithm_descriptions = {
    "FCFS": "First-Come, First-Served: As tarefas são processadas na ordem de chegada.",
    "SJF": "Shortest Job First: A tarefa com a menor duração é processada primeiro.",
    "SRTF": "Shortest Remaining Time First: A tarefa com o menor tempo restante é processada primeiro, permitindo preempção.",
    "RR": "Round Robin: Cada tarefa recebe um quantum de tempo para execução, e as tarefas são processadas em ciclos.",
    "PRIOc": "Priority Scheduling (Cooperative): A tarefa com a maior prioridade é processada primeiro, sem permitir preempção.",
    "PRIOp": "Priority Scheduling (Preemptive): A tarefa com a maior prioridade é processada primeiro, permitindo preempção."
}

if algorithm not in accepted_algorithms:
    print(f"Algoritmo de escalonamento '{algorithm}' não é válido. Os algoritmos aceitos são: {', '.join(accepted_algorithms)}.\nUtilizando 'FCFS' como padrão.")
    algorithm = "FCFS"
print(f"Algoritmo de escalonamento: {algorithm}")
print(f"Descrição: {algorithm_descriptions.get(algorithm, 'Descrição não disponível.')}")

simulator = Simulator(mode, algorithm, num_processors, tarefas)
simulator.start()