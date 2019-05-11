from threading import Thread, Lock
import serial
import time

def serial_read(mutex=Lock()):
	porta = serial.Serial("/dev/ttyUSB0", 9600)

	time.sleep(1)
	read = porta.read()

	while (True):
		#mutex.acquire()

		read = porta.read()
		print(read)

		#porta.write(str.encode("w"))
		#mutex.release()

	serial.close()


def porta_serial(mutex):
	#threadDeAtivarSom = Thread(target=ativar_som, args=(mutex,))
	#threadDeAtivarSom.start()

	serial_read(mutex)
