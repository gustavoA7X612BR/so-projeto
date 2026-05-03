class Scheduler:
    """Escalonador de tarefas do sistema operacional, responsável por gerenciar as tarefas prontas e em espera, e decidir qual tarefa deve ser executada a seguir."""
    def __init__(self, hardware, tasks=[], algorithm="FCFS"):
        """Inicializa o escalonador com o hardware e o algoritmo de escalonamento a ser utilizado.
        args:
            hardware (Hardware): O hardware do sistema operacional, contendo os processadores e o relógio.
            algorithm (str): O algoritmo de escalonamento a ser utilizado (padrão: "FCFS").
        """
        self.hardware = hardware
        self.algorithm = algorithm
        self.tasks = tasks
        self.readyQueue = []  # Fila de tarefas prontas para execução

    def tasksRemove(self, task):
        """Remove e retorna uma tarefa da lista de tarefas restantes, com base no ID da tarefa."""
        if task in self.tasks:
            self.tasks.remove(task)
            return task
        return None

    def readyTasksDequeue(self):
        """Remove e retorna a próxima tarefa da fila de prontas, de acordo com o algoritmo de escalonamento.
        returns:
            Task: A próxima tarefa a ser executada, ou None se a fila de prontas estiver vazia.
        """
        if self.readyQueue:
            return self.readyQueue.pop(0)  # Remove e retorna a primeira tarefa da fila de prontas
        return None
    
    def addTaskToReadyQueue(self, task):
        """Adiciona uma tarefa à fila de prontas do escalonador.
        args:
            task (Task): A tarefa a ser adicionada à fila de prontas.
        """
        self.readyQueue.append(task) # Adiciona a tarefa à fila de prontas

        if self.algorithm == "SRTF":
            self.readyQueue.sort(key=lambda t: t.remaining_time)  # Ordena a fila de prontas pelo tempo restante (SRTF)
        elif self.algorithm == "SJF":
            self.readyQueue.sort(key=lambda t: t.duration)  # Ordena a fila de prontas pela duração (SJF)
        elif self.algorithm == "PRIOc" or self.algorithm == "PRIOp":
            self.readyQueue.sort(key=lambda t: t.priority, reverse=True)  # Ordena a fila de prontas pela prioridade (PRIOc)
    
    def preemptProcessorRunningTask(self, processor):
        """Preempta a tarefa atualmente em execução em um processador, colocando-a de volta na fila de prontas.
        args:
            processor (Processor): O processador cuja tarefa em execução deve ser preemptada.
        """
        if processor.task:
            self.addTaskToReadyQueue(processor.removeTask())  # Remove a tarefa do processador e a adiciona de volta à fila de prontas
    
    def tryPreempt(self, processor):
        if self.algorithm == "SRTF":
            if processor.isOn and processor.task and self.readyQueue and processor.task.remaining_time > self.readyQueue[0].remaining_time:
                print(f"Tarefa {processor.task.task_id} tem tempo restante maior que a tarefa {self.readyQueue[0].task_id} na fila de prontas. Preemptando...")
                self.preemptProcessorRunningTask(processor)  # Preempta a tarefa atualmente em execução no processador

        elif self.algorithm == "RR":
            if self.hardware.clock.current_time - processor.task.lastRunStartTime >= 2:
                print(f"Tarefa {processor.task.task_id} atingiu o tempo de quantum no processador {self.hardware.processors.index(processor)}. Preemptando...")
                self.preemptProcessorRunningTask(processor)  # Preempta a tarefa atualmente em execução no processador

        elif self.algorithm == "PRIOp":
            if processor.isOn and processor.task and self.readyQueue and processor.task.priority < self.readyQueue[0].priority:
                print(f"Tarefa {processor.task.task_id} tem prioridade menor que a tarefa {self.readyQueue[0].task_id} na fila de prontas. Preemptando...")
                self.preemptProcessorRunningTask(processor)  # Preempta a tarefa atualmente em execução no processador

    def setTaskToProcessor(self, processor, task):
        """Atribui uma tarefa a um processador, removendo-a da fila de prontas.
        args:
            processor (Processor): O processador ao qual a tarefa deve ser atribuída.
            task (Task): A tarefa a ser atribuída ao processador.
        """
        task.lastRunStartTime = self.hardware.clock.current_time  # Registra o tempo de início da execução da tarefa
        processor.setTask(task)  # Atribui a tarefa ao processador
        self.readyQueue.remove(task)  # Remove a tarefa da fila de prontas
    
    def schedule(self):
        print(f"\n====== Instante de tempo: {self.hardware.clock.current_time}. ===============================")
        print("Tarefas restantes para iniciar:", [t.task_id for t in self.tasks])
        print("Fila de prontas:", [t.task_id for t in self.readyQueue])

        for task in self.tasks[:]: # Cria uma cópia da lista de tarefas para iterar, permitindo a remoção de tarefas durante a iteração
            if task.startTime == self.hardware.clock.current_time:
                print(f"Adicionando tarefa {task.task_id} à fila de prontas.")
                self.addTaskToReadyQueue(self.tasksRemove(task))  # Remove a tarefa da lista de tarefas restantes e a adiciona à fila de prontas    

        for processor in self.hardware.processors:
            # 1: Verifica se a tarefa em execução no processador foi concluída ou se deve ser preemptada
            if processor.task:
                if processor.task.remaining_time <= 0:
                    print(f"Tarefa {processor.task.task_id} concluída no processador {self.hardware.processors.index(processor)}.")
                    processor.task = None
                else:
                    self.tryPreempt(processor)
            
            # 2: Atribui uma nova tarefa ao processador se ele estiver ocioso ou se a tarefa atual tiver sido preemptada    
            for task in self.readyQueue:
                if not processor.isOn or (processor.isOn and processor.task is None): 
                    print(f"Atribuindo tarefa {task.task_id} ao processador {self.hardware.processors.index(processor)}.")

                    self.setTaskToProcessor(processor, task)  # Atribui a tarefa ao processador
                    break  # Move para o próximo processador
            
            # 3: Desliga o processador se após o escalonamento ele estiver ocioso (sem tarefa para processar)
            if processor.isOn and not processor.task:
                print(f"Processador {self.hardware.processors.index(processor)} está ocioso. Desligando...")
                processor.shutdown()  # Desliga o processador se não houver tarefa para processar
