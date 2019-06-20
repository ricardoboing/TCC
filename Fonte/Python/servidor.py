import socket
import pygame

from threading import Thread, Lock
from bd.agendamento import *

SERVER_HOST = "192.168.25.36"
SERVER_INTERFACE_PORT = 8080
SERVER_IOT_PORT = 8081
CLIENTE_IOT_PORT = 8080
IOT_ADDRESS_LIST = []

MUSIC_ADDRESS = "musica.mp3"

############################# SERVER IOT ############################
# Recebe solicitacoes de dispositivos iot para serem cadastrados (IP)
# em uma lista. Posteriormente, comandos de controle sao enviados aos
# IP's cadastrados nessa lista.
# 
# ativar_servidor_interface, no_iot_enviar_comando
#####################################################################
def ativar_servidor_iot(mutex):
    global IOT_ADDRESS_LIST

    serverSocket = socket.socket()
    serverSocket.bind((SERVER_HOST, SERVER_IOT_PORT))
    serverSocket.listen()

    print("SERVER CONNECT - HOST: %s | PORT: %s (IOT)" %(SERVER_HOST, SERVER_IOT_PORT))

    try:
        while True:
            conexao, ip = serverSocket.accept()
            print("\nIOT CONNECT -------\n")
            print("IP: %s" %(ip[0]))

            # Um iot nao pode ser cadastrado em paralelo com
            # o gerenciamento de dados da camada de interface
            mutex.acquire()

            # Cadastra o ip do iot, caso ainda nao esteja na lista
            if ip[0] not in IOT_ADDRESS_LIST:
                IOT_ADDRESS_LIST.append(ip[0])
                print("IOT CADASTRADO")

            mutex.release()

            print("\nIOT DISCONNECT -------\n")
    except:
        pass
    finally:
        conexao.close()
    serverSocket.close()

########################## SERVER INTERFACE #########################
# Recebe dados da camada de interface e realiza o gerenciamento
# desses dados.
# 
# ativar_servidor_iot, no_iot_enviar_comando, som_configurar
#####################################################################
def ativar_servidor_interface(mutex, eventoAtual):
    serverSocket = socket.socket()
    serverSocket.bind((SERVER_HOST, SERVER_INTERFACE_PORT))
    serverSocket.listen()

    print("SERVER CONNECT - HOST: %s | PORT: %s (INTERFACE)" %(SERVER_HOST, SERVER_INTERFACE_PORT))

    # Inicializa a biblioteca para ativar/desativar efeitos sonoros
    # utilizados para alertar as aves.
    pygame.init()
    pygame.mixer.music.load(MUSIC_ADDRESS)

    try:
        while True:
            conexao = serverSocket.accept()[0]
            print("CLIENT CONNECT -------\n")

            operacao = str(ler_conteudo_conexao(conexao,1))

            # As operacoes nao podem ser realizadas em paralelo com
            # o cadastrado dos IP's dos dispositivos.
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
    finally:
        conexao.close()
    serverSocket.close()

########################### CONFIGURAR SOM ##########################
# Com base no comando especificado eh alterado o volume, iniciado ou
# parado a execucao do efeito sonoro (que alerta as aves sobre o
# alimento).
# 
# comando:
# a: parar som
# b: iniciar som e alterar volume
# c: alterar volume
#
# ativar_servidor_interface
#####################################################################
def som_configurar(comando):
    operacao = comando[0:1]

    # PARAR
    if operacao == "a":
        pygame.mixer.music.stop()
    else:
    # ALTERAR VOLUME [, INICIAR SOM]
        volume = int(comando[1:])
        volume /= 100

        pygame.mixer.music.set_volume(volume)

    # INICIAR
    if operacao == "b":
        pygame.mixer.music.play(-1)

    # Sucesso/erro/falha nao implementados
    return "1"

########################### CONTROLAR IOT ###########################
# Envia um comando de controle ao dispositivo iot de acordo com o IP
# do dispositivo. Os IP's sao cadastrados, inicialmente, atraves de
# um socket, na funcao ativar_servidor_iot.
#
# ativar_servidor_iot, ativar_servidor_interface
#####################################################################
def no_iot_enviar_comando():
    global IOT_ADDRESS_LIST
    global mutex

    # O comando eh enviado para todos os dispositivos iot cadastrados
    for address in IOT_ADDRESS_LIST:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
                server.connect((address, CLIENTE_IOT_PORT))
                server.sendall("a".encode())
        except:
            print("Erro ao se conectar com iot. IP: %s" %(address))
            pass
    # Sucesso/erro/falha nao implementados
    return "1"