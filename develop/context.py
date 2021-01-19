# context.py

import queue


class Contexts:
    """States to keep track of during app execution.

    """
    def __init__(self):
        self.stm = {}

        # Health status of endpoint processes.
        self.thread_state = True

        # Custom blocking services running.
        self.processes = {}

    def end_processes(self):
        for k, v in self.processes.items():
            self.end_process(v)

    def end_process(self, process):
        if process.is_alive():
            process.raiseExc(SystemExit)