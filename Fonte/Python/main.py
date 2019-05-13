from threading import Thread, Lock

from servidor import *
from porta_serial import porta_serial
from util.codificar import *
from bd.evento import bd_evento_select

if __name__ == "__main__":
    #banco_proximo_evento()
    #ativar_servidor()
    #mutex = Lock()
    print(codificar_nome("Ricardo ae"))
	#bd_evento_select("25055")

    #threadDoServidor = Thread(target=ativar_servidor, args=(mutex,))
    #threadDaPortaSerial = Thread(target=porta_serial, args=(mutex,))

    #threadDoServidor.start()
    #threadDaPortaSerial.start()

    #threadDoServidor.join()
    #threadDaPortaSerial.join()