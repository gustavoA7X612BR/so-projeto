class Clock:
    """Simula o clock do sistema operacional, mantendo o tempo atual e permitindo avançar o tempo."""
    def __init__(self):
        """Inicializa o clock com o tempo atual definido como zero."""
        self.current_time = 0 # 

    def tick(self):
        """Avança o tempo do clock em um tick (por exemplo, 1 unidade de tempo)."""
        self.current_time += 1