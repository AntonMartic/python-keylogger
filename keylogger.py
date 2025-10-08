from pynput import keyboard

# OBS: allow IDE Input Monitoring, Accessibility, Full Disk Access in OS settings

def on_press(key):
    try:
        print(key)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()


