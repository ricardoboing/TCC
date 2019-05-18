import socket
from threading import Thread, Lock
from bd.evento import *

SERVER_HOST = "192.168.25.6"#"192.168.50.179"#
SERVER_PORT = 8081

def ativar_servidor(mutex, eventoAtual):
    serverSocket = socket.socket()
    serverSocket.bind((SERVER_HOST, SERVER_PORT))
    serverSocket.listen()
    
    print("SERVER CONNECT - HOST: %s | PORT : %s" %(SERVER_HOST, SERVER_PORT))

    try:
        while True:
            conexao = serverSocket.accept()[0]
            print("CLIENT CONNECT -------\n")

            operacao = str(ler_conteudo_conexao(conexao,1))

            mutex.acquire()

            # INSERIR EVENTO
            if operacao == 'a':
                print("_INSERIR EVENTO")
                valorDeRetorno = bd_evento_insert(conexao)
                eventoAtual.buscar_proximo_evento()
            
            # REMOVER EVENTO
            elif operacao == 'b':
                print("_REMOVER EVENTO")
                valorDeRetorno = bd_evento_remove(conexao)
                eventoAtual.buscar_proximo_evento()
            
            # UPDATE EVENTO
            elif operacao == 'c':
                print("_UPDATE EVENTO")
                valorDeRetorno = bd_evento_update(conexao)
                eventoAtual.buscar_proximo_evento()
            
            # SELECT EVENTO
            elif operacao == 'd':
                print("_SELECT EVENTO")
                valorDeRetorno = bd_evento_select(conexao)

            # SELECT_ALL EVENTO NO BANCO DE DADOS
            elif operacao == 'e':
                print("_SELECT_ALL EVENTO")
                valorDeRetorno = bd_evento_select_all()

            mutex.release()

            conexao.sendall(valorDeRetorno.encode())

            print ("\nCLIENT DISCONNECT -------\n");
            conexao.close()
    finally:
        conexao.close()
    serverSocket.close()

    mutex.release()