from threading import Thread, Lock

from servidor import ativar_servidor_interface, ativar_servidor_iot, no_iot_enviar_comando
from classes.agendamento import *

import time
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

def cumprir_agendamento(mutex, eventoAtual):
	while True:
		mutex.acquire()

		if eventoAtual.disparar_agora():
			no_iot_enviar_comando()
		mutex.release()

		# Dorme ate alterar o minuto do relogio
		# Ex:
		# agora 19:30:40 e precisa acordar 19:31:00, entao: dorme 20s
		proximoMinuto = 60-int(datetime.now().strftime("%S"))
		time.sleep(proximoMinuto)

if __name__ == "__main__":
	eventoAtual = Evento()
	eventoAtual.buscar_proximo_evento()
	
	mutex = Lock()

	listaDeNosIot = []
	threadServidorIot = Thread(target=ativar_servidor_iot, args=(mutex,))
	threadServidorInterface = Thread(target=ativar_servidor_interface, args=(mutex,eventoAtual))
	threadAgendamento = Thread(target=cumprir_agendamento, args=(mutex,eventoAtual))

	threadServidorInterface.start()
	threadServidorIot.start()
	threadAgendamento.start()

	threadServidorIot.join()
	threadServidorInterface.join()
	threadAgendamento.join()