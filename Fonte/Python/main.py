#from threading import Thread, Lock

from servidor import *
from porta_serial import porta_serial
from evento import *

if __name__ == "__main__":
    #banco_proximo_evento()
    #evento = Evento()
    #evento.buscar_proximo_evento()
    #print(evento.idEvento)

    porta_serial(evento)
    #mutex = Lock()
    #ativar_servidor()
    #threadDoServidor = Thread(target=ativar_servidor, args=(mutex,))
    #threadDaPortaSerial = Thread(target=porta_serial, args=(mutex,))

    #threadDoServidor.start()
    #threadDaPortaSerial.start()

    #threadDoServidor.join()
    #threadDaPortaSerial.join()