import threading
from rich.traceback import install

class Thread(threading.Thread):
    def __init__(self, target=None):
        install(show_locals=True)
        if target is None:
           super().__init__()
        else: 
            super().__init__(target=target)