import asyncio

from .app import AppInit
from .agent import Agent
from .schemes import Schemes


class AppBare(AppInit, Agent, Schemes):
    """A bare application for Crimata Platform.

    Automatically handles cancel and fulfill intents. A way to easily 
    get into the game on the platform.

    """
    def __init__(self, name):
        AppInit.__init__(self, name)
        Agent.__init__(self)
        Schemes.__init__(self)

        # Is to handle.
        self.request_queue = asyncio.Queue()

    async def main_(self):
        await asyncio.gather(

            # Core loops
            self.do_tasks(), self.feed_request_queue(),

            # Developer init
            self.main())

    async def do_tasks(self):
        while self.on:

            if not self.thread_state:
                self.end()
                continue

            # Listen for intent.
            try:
                request = self.request_queue.get_nowait()

                # Do its thing.
                self.handle_request(request)

            except asyncio.QueueEmpty:
                await asyncio.sleep(0.1)

    async def feed_request_queue(self):
        while self.on:
            
            # Try to recv an intent.
            request = self.recv_agent()

            if request:
                await self.request_queue.put(request)

            await asyncio.sleep(0.1)
