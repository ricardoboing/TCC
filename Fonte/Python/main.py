from threading import Thread, Lock

from servidor import ativar_servidor
from porta_serial import porta_serial
from evento import *

if __name__ == "__main__":
	eventoAtual = Evento()
	eventoAtual.buscar_proximo_evento()

	#porta_serial(evento)
	mutex = Lock()

	threadDoServidor = Thread(target=ativar_servidor, args=(mutex,eventoAtual))
	threadDaPortaSerial = Thread(target=porta_serial, args=(mutex,eventoAtual))

	threadDoServidor.start()
	threadDaPortaSerial.start()

	threadDoServidor.join()
	threadDaPortaSerial.join()