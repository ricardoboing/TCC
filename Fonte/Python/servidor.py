import socket
import pygame

from threading import Thread, Lock
from bd.agendamento import *
from bd.no_iot import *

SERVER_HOST = "192.168.50.179"
SERVER_INTERFACE_PORT = 8081
SERVER_IOT_PORT = 8080
CLIENTE_IOT_PORT = 8080
IOT_ADDRESS_LIST = []

MUSIC_ADDRESS = "musica.mp3"

################
## SERVER IOT ##
################
def ativar_servidor_iot(mutex):
    global IOT_ADDRESS_LIST

    serverSocket = socket.socket()
    serverSocket.bind((SERVER_HOST, SERVER_IOT_PORT))
    serverSocket.listen()

    print("SERVER CONNECT - HOST: %s | PORT: %s (IOT)" %(SERVER_HOST, SERVER_IOT_PORT))

    try:
        while True:
            conexao, ip = serverSocket.accept()
            mutex.acquire()

            if ip[0] not in IOT_ADDRESS_LIST:
                IOT_ADDRESS_LIST.append(ip[0])
            
            mutex.release()

    finally:
        conexao.close()
    serverSocket.close()

######################
## SERVER INTERFACE ##
######################
def ativar_servidor_interface(mutex, eventoAtual):
    serverSocket = socket.socket()
    serverSocket.bind((SERVER_HOST, SERVER_INTERFACE_PORT))
    serverSocket.listen()

    print("SERVER CONNECT - HOST: %s | PORT: %s (INTERFACE)" %(SERVER_HOST, SERVER_INTERFACE_PORT))

    pygame.init()
    pygame.mixer.music.load(MUSIC_ADDRESS)

    try:
        while True:
            conexao = serverSocket.accept()[0]
            print("CLIENT CONNECT -------\n")

            operacao = str(ler_conteudo_conexao(conexao,1))

            mutex.acquire()

            # INSERIR EVENTO
            if operacao == 'a':
                print("_INSERIR EVENTO")
                valorDeRetorno = bd_agendamento_insert(conexao)
                eventoAtual.buscar_proximo_evento()

            # REMOVER EVENTO
            elif operacao == 'b':
                print("_REMOVER EVENTO")
                valorDeRetorno = bd_agendamento_remove(conexao)
                eventoAtual.buscar_proximo_evento()

            # UPDATE EVENTO
            elif operacao == 'c':
                print("_UPDATE EVENTO")
                valorDeRetorno = bd_agendamento_update(conexao)
                eventoAtual.buscar_proximo_evento()

            # SELECT EVENTO
            elif operacao == 'd':
                print("_SELECT EVENTO")
                valorDeRetorno = bd_agendamento_select(conexao)

            # SELECT_ALL EVENTO NO BANCO DE DADOS
            elif operacao == 'e':
                print("_SELECT_ALL EVENTO")
                valorDeRetorno = bd_agendamento_select_all()

            # CONTROLE_NO_IOT
            elif operacao == 'f':
                print("_CONTROLE_NO_IOT")
                valorDeRetorno = no_iot_enviar_comando()

            # CONTROLE_SOM
            elif operacao == 'g':
                print("_CONTROLE_SOM")
                comando = ler_conteudo_conexao(conexao,1)

                # Comando de alterar o volume do som precisa dos 3 bytes do volume
                if comando != "a":
                    comando += ler_conteudo_conexao(conexao,3)

                valorDeRetorno = som_configurar(comando)

            # GET ESTIMATIVA DE CONSUMO
            elif operacao == "h":
                print("_GET ESTIMATIVA DE CONSUMO")
                valorDeRetorno = bd_no_iot_select_estimativa_de_consumo()

            # REINICIAR ESTIMATIVA DA BATERIA
            elif operacao == "i":
                print("_REINICIAR ESTIMATIVA DA BATERIA")
                valorDeRetorno = bd_no_iot_reset_estimativa_da_bateria()

            # SELECT CONFIGURACOES NO_IOT
            elif operacao == "j":
                print("_SELECT CONFIGURACOES NO_IOT")
                valorDeRetorno = bd_no_iot_select_configuracoes()

            # UPDATE CONFIGURACOES NO_IOT
            elif operacao == "k":
                print("_UPDATE CONFIGURACOES NO_IOT")
                valorDeRetorno = bd_no_iot_update_configuracoes(conexao)

            mutex.release()

            conexao.sendall(valorDeRetorno.encode())

            print ("\nCLIENT DISCONNECT -------\n");
            conexao.close()
    finally:
        conexao.close()
    serverSocket.close()

    mutex.release()

def som_configurar(comando):
    operacao = comando[0:1]

    if operacao == "a":
        pygame.mixer.music.stop()
    else:
        volume = int(comando[1:])
        volume /= 100
        
        pygame.mixer.music.set_volume(volume)

        if operacao == "b":
            pygame.mixer.music.play(-1)

    return "1"

def no_iot_enviar_comando():
    global IOT_ADDRESS_LIST
    global mutex

    for address in IOT_ADDRESS_LIST:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.connect((address, CLIENTE_IOT_PORT))
            server.sendall("a".encode())

    return "1"