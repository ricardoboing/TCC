from threading import Thread, Lock

from servidor import ativar_servidor
from porta_serial import porta_serial
from evento import *

if __name__ == "__main__":
	eventoAtual = Evento()
	eventoAtual.buscar_proximo_evento()
	k = "ebcéã"
	a = k.encode("utf8")
	b = str(len(a))+k
	print(k)
	print(a)
	print(len(a))
	#print(ord(a[0:1]))
	
	#porta_serial(evento)
	
	mutex = Lock()

	threadDoServidor = Thread(target=ativar_servidor, args=(mutex,eventoAtual))
	#threadDaPortaSerial = Thread(target=porta_serial, args=(mutex,eventoAtual))

	threadDoServidor.start()
	#threadDaPortaSerial.start()

	threadDoServidor.join()
	#threadDaPortaSerial.join()