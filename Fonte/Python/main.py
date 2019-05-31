from threading import Thread, Lock

from servidor import ativar_servidor_interface, ativar_servidor_iot
from porta_serial import porta_serial
from classes.agendamento import *

#import time
#import socket

'''
def teste(mutex):
	time.sleep(1)
	HOST = "192.168.50.179"
	PORT = 8082

	c = 0
	while c < 2:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.connect((HOST, PORT))
			c = c +1

	print("oi")
'''
if __name__ == "__main__":
	eventoAtual = Evento()
	eventoAtual.buscar_proximo_evento()
	
	mutex = Lock()

	listaDeNosIot = []
	threadServidorInterface = Thread(target=ativar_servidor_interface, args=(mutex,eventoAtual))
	threadServidorIot = Thread(target=ativar_servidor_iot, args=(mutex,))

	threadServidorInterface.start()
	threadServidorIot.start()

	threadServidorInterface.join()
	threadServidorIot.join()