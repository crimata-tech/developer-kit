# app.py

import time
import queue
import asyncio


class AppInit:
    """All apps need to inherit this.

    """
    def __init__(self, name):
        self.name = name #eg. "Settings"

        self.input_queue = queue.Queue()
        self.output_queue = queue.Queue()

        # "on" or "off"
        self.on = True

    # Low level non-blocking IO methods:

    def send_agent(self, intent):
        self.output_queue.put(intent)

    def recv_agent(self):
        intent = False

        try:
            intent = self.input_queue.get_nowait()
        except queue.Empty:
            pass

        return intent

    # Platform calls these:

    def run(self, crimata_id):
        self.crimata_id = crimata_id

        asyncio.run(self.main_())

    def end(self):
        self.end_processes()
        self.on = False
