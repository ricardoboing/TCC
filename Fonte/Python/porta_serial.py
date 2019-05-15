import serial
import time

from threading import Thread, Lock
#from evento import *

def serial_read(evento):#mutex=Lock()):
	porta = serial.Serial("/dev/ttyUSB0", 9600)
	read = porta.read()

	while (True):
		#mutex.acquire()

		read = porta.read(1)
		print(read)

		if read == b"A":
			if evento.disparar_agora() == 1:
				print("Disparou")
				porta.write(b'B')
			else:
				print("Nao disparou")
				porta.write(b'C')

		#porta.write(str.encode("w"))
		#mutex.release()

	serial.close()

def porta_serial(evento):
	#threadDeAtivarSom = Thread(target=ativar_som, args=(mutex,))
	#threadDeAtivarSom.start()

	serial_read(evento)
