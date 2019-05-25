import threading

# Importando o PyGame
import pygame
from time import sleep

globalVar = "d"
globalVar2 = 1

def tocar_som(evento):
	global globalVar
	global globalVar2

	while True:
		evento.wait()
		evento.clear()

		if globalVar == "a":
			print("a %s | %f" %(globalVar, globalVar2))
			pygame.mixer.music.stop()

		elif globalVar == "b":
			pygame.mixer.music.play()
			print("b %s | %f" %(globalVar, globalVar2))
		
		elif globalVar == "c":
			pygame.mixer.music.set_volume(globalVar2)
			print("c %s | %f" %(globalVar, globalVar2))
		
		else:
			pygame.mixer.music.set_volume(globalVar2)
			print("d %s | %f" %(globalVar, globalVar2))




	
def teste(evento):
	global globalVar
	global globalVar2

	while True:
		print("Teste1")

		if globalVar == "a":
			globalVar = "b"

		elif globalVar == "b":
			globalVar = "c"
			globalVar2 = 1
		
		elif globalVar == "c":
			globalVar = "d"
			globalVar2 = 0.2
		
		else:
			globalVar = "a"

		evento.set()
		sleep(5)

#if __name__ == "__main__":
def som(evento):
	pygame.init()
	pygame.mixer.music.load("musica.mp3")

	thread = threading.Thread(target=teste, args=(evento))
	thread.start()
	thread.join()