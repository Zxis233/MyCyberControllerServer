import subprocess
import threading
import time


class GameMonitor:
    def __init__(self, callback):
        self.callback = callback
        self.started = False

    def gamer(self):
        self.monit_game_started()

    def monit_game_started(self):
        while True:
            process_name = 'League of Legends.exe'
            callall = 'TASKLIST'
            outputall = subprocess.check_output(callall, shell=True)
            outputstringall = str(outputall)
            if process_name in outputstringall:
                print("Locked.")
                if self.callback:
                    self.callback()
            else:
                pass

            time.sleep(5)

    def start(self):
        gamer_threading = threading.Thread(target=self.gamer, args=())
        gamer_threading.start()
        self.started = True
