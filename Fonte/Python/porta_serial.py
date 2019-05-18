import serial
import time

from threading import Thread, Lock

def serial_read(mutex, evento):#mutex=Lock()):
	porta = serial.Serial("/dev/ttyUSB0", 9600)
	read = porta.read()

	while (True):
		read = porta.read(1)
		print(read)

		mutex.acquire()
		
		if read == b"A":
			if evento.disparar_agora() == 1:
				print("Disparou")
				porta.write(b'B')
			else:
				print("Nao disparou")
				porta.write(b'C')

		#porta.write(str.encode("w"))
		mutex.release()

	serial.close()

def porta_serial(mutex, evento):
	#threadDeAtivarSom = Thread(target=ativar_som, args=(mutex,evento))
	#threadDeAtivarSom.start()

	serial_read(mutex, evento)
