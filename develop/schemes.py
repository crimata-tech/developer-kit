# schemes.py

import queue

from .context import Contexts
from .threadq import ThreadWithExc


class Schemes(Contexts):
    """Core functions of the app.

    """
    def __init__(self):
        Contexts.__init__(self)

        # Add your dev schemes here.
        self.schemes = ["fulfill", "cancel", "placeholder"]

    def handle_request(self, request):
        print(f"Settings app -> Handling {request.intent}.")

        if request.intent in self.schemes:
            attr = getattr(self, request.intent)
            attr(request)

        else:
            self.delegate(request)

    # Delegate intent to developer add on.
    def delegate(self, request):
        attr = getattr(self, request.epic)

        t = ThreadWithExc(target=self.host, args=(request.epic,))
        t.start()

        self.processes.update({request.epic: t})

    # Host endpoint process.
    def host(self, endpoint):
        try:
            attr = getattr(self, endpoint)
            attr()
        except:
            self.thread_state = False

    def fulfill(self, request):
        self.stm.update({request.epic: request})

    def cancel(self, request):
        t = self.processes.get(request.epic)
        self.end_process(t)

