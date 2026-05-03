class tcb:
    """Estrutura de dados para representar o Control Block de uma tarefa (TCB) no sistema operacional."""
    def __init__(self, task_id, priority, color="#FFFFFF",startTime=0, duration=0):
        self.task_id = task_id
        self.priority = priority
        self.color = color

        self.state = 'ready'  # Possible states: 'ready', 'running', 'waiting', 'terminated'
        self.context = None  # Placeholder for the task's context (e.g., registers, stack pointer)
        self.duration = duration  # Total duration of the task (for simulation purposes)s
        self.remaining_time = duration  # Time remaining for the task to complete (for simulation purposes)
        self.lastRunStartTime = None  # Time when the task last started running (for simulation purposes)
        self.startTime = startTime  # Time when the task is created or scheduled to start

    def __repr__(self):
        return f"TCB(task_id={self.task_id}, priority={self.priority}, state='{self.state}')"