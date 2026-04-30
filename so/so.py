from so.scheduler import Scheduler


class So:
    def __init__(self, hardware, tasks=[]):
        self.hardware = hardware
        self.scheduler = Scheduler(hardware)
        self.tasks = tasks
    def run(self):
        for task in self.tasks:
            if task.startTime == self.hardware.clock.current_time:
                self.scheduler.add_task(task)
        self.hardware.run()
        self.scheduler.schedule()
