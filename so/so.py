from so.scheduler import Scheduler


class So:
    def __init__(self, hardware, tasks=[]):
        self.hardware = hardware
        self.scheduler = Scheduler(hardware)
        self.tasks = tasks
        self.readyQueue = []

    def run(self):
        print(f"====== Instante de tempo: {self.hardware.clock.current_time}. ===============================")
        print("Tarefas restantes para iniciar:", [t.task_id for t in self.tasks])
        print("Fila de prontas:", [t.task_id for t in self.readyQueue])

        for task in self.tasks[:]:
            if task.startTime == self.hardware.clock.current_time:
                print(f"Adicionando tarefa {task.task_id} à fila de prontas.")
                self.readyQueue.append(task)  # Adiciona a tarefa à fila de prontas
                self.tasks.remove(task)  # Remove a tarefa da lista de tarefas pendentes
                # TESTE Shortest Remaining Time First (SRTF)   
                self.readyQueue.sort(key=lambda t: t.remaining_time)  # Ordena a fila de prontas pelo tempo restante (SRTF)

        # TESTE Shortest Job First (SJF)
        #self.readyQueue.sort(key=lambda t: t.remaining_time)  # Ordena a fila de prontas pelo tempo restante (SJF)

        # TESTE PRIOc
        #self.readyQueue.sort(key=lambda t: t.priority, reverse=True)  # Ordena a fila de prontas pela prioridade (PRIOc)

        for processor in self.hardware.processors:
            if processor.task:
                if processor.task.remaining_time <= 0:
                    print(f"Tarefa {processor.task.task_id} concluída no processador {self.hardware.processors.index(processor)}.")
                    processor.task = None
                else:
                    # PREEMPÇÂO
                    # SRTF
                    if processor.isOn and processor.task and self.readyQueue and processor.task.remaining_time > self.readyQueue[0].remaining_time:
                        print(f"Tarefa {processor.task.task_id} tem tempo restante maior que a tarefa {self.readyQueue[0].task_id} na fila de prontas. Preemptando...")
                        self.readyQueue.append(processor.task)  # Recoloca a tarefa atual na fila de prontas
                        self.readyQueue.sort(key=lambda t: t.remaining_time)  # Reordena a fila de prontas pelo tempo restante (SRTF)
                        processor.task = None  # Libera o processador para a próxima tarefa
                #else:
                #    if self.hardware.clock.current_time - processor.task.lastRunStartTime >= 2:
                #        print(f"Tarefa {processor.task.task_id} atingiu o tempo de quantum no processador {self.hardware.processors.index(processor)}. Preemptando...")
                #        self.readyQueue.append(processor.task)  # Recoloca a tarefa na fila de prontas
                #        processor.task = None  # Libera o processador para a próxima tarefa
                #else:
                    #print(f"Processador {self.hardware.processors.index(processor)} está processando a tarefa {processor.task.task_id}. Tempo restante: {processor.task.remaining_time}")


            for task in self.readyQueue:
                if not processor.isOn or (processor.isOn and processor.task is None): 
                    print(f"Atribuindo tarefa {task.task_id} ao processador {self.hardware.processors.index(processor)}.")

                    task.lastRunStartTime = self.hardware.clock.current_time  # Registra o tempo de início da execução da tarefa
                    processor.setTask(task)  # Atribui a tarefa ao processador
                    self.readyQueue.remove(task)  # Remove a tarefa da fila de prontas
                    break  # Move para o próximo processador
            
            if processor.isOn and not processor.task:
                print(f"Processador {self.hardware.processors.index(processor)} está ocioso. Desligando...")
                processor.shutdown()  # Desliga o processador se não houver tarefa para processar

        self.hardware.run()
