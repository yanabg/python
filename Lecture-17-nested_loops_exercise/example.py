# keyboard listener

# step 1 pip install pynput
from pynput import keyboard

def on_press():
    print("Pressed: ", event)

def on_release():
    print("Released: ", reversed)

with keyboard.Listener(on_press=on_press, on_release = on_release) as Listener:
    listener.join()
