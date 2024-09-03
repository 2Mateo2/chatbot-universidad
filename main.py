import sys
from PyQt5.QtWidgets import QApplication
from view.view_message import IntroMessageWindow
from core.api import run_flask
import threading
import signal
import os
import sys

class Application(QApplication):
    def __init__(self, args):
        super().__init__(args)
        self.flask_thread = threading.Thread(target=run_flask, daemon=True)
        self.flask_thread.start()
        self.aboutToQuit.connect(self.cleanup)

    def cleanup(self):
        if self.flask_thread.is_alive():
            os.kill(os.getpid(), signal.SIGINT) 

if __name__ == "__main__":
    app = Application(sys.argv)
    window = IntroMessageWindow()
    window.show()
    sys.exit(app.exec_())