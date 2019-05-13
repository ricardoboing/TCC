import socket
from threading import Thread, Lock
from bd.evento import *

SERVER_HOST = "192.168.25.6"#"192.168.50.179"#
SERVER_PORT = 8081

def ativar_servidor():
    serverSocket = socket.socket()
    serverSocket.bind((SERVER_HOST, SERVER_PORT))
    serverSocket.listen()
    
    print("SERVER CONNECT - HOST: %s | PORT : %s" %(SERVER_HOST, SERVER_PORT))

    try:
        while True:
            conexao = serverSocket.accept()[0]
            print("CLIENT CONNECT -------\n")

            operacao = str(ler_conteudo_conexao(conexao,1))

            # INSERIR EVENTO (somDesabilitado)
            if operacao == 'a':
                print("_INSERIR EVENTO (somDesabilitado)")
                valorDeRetorno = bd_evento_insert(conexao, 0)
            # INSERIR EVENTO (somHabilitado)
            if operacao == 'A':
                print("_INSERIR EVENTO (somHabilitado)")
                valorDeRetorno = bd_evento_insert(conexao, 1)
            
            # REMOVER EVENTO
            elif operacao == 'b':
                print("_REMOVER EVENTO")
                valorDeRetorno = bd_evento_delete(conexao)
            
            # UPDATE EVENTO (somDesabilitado)
            elif operacao == 'c':
                print("_UPDATE EVENTO (somDesabilitado)")
                valorDeRetorno = bd_evento_update(conexao, 0)
            # UPDATE EVENTO (somHabilitado)
            elif operacao == 'C':
                print("_UPDATE EVENTO (somHabilitado)")
                valorDeRetorno = bd_evento_update(conexao, 1)
            
            # SELECT EVENTO
            elif operacao == 'd':
                print("_SELECT EVENTO")
                valorDeRetorno = bd_evento_select(conexao)

            # SELECT_ALL EVENTO NO BANCO DE DADOS
            elif operacao == 'e':
                print("_SELECT_ALL EVENTO")
                valorDeRetorno = bd_evento_select_all()

            # SELECT ESTIMATIVA DE CONSUMO
            elif operacao == 'f':
                print("_SELECT ESTIMATIVA DE CONSUMO")
                valorDeRetorno = "abcdefghij123456089"

            conexao.sendall(valorDeRetorno.encode())

            print ("\nCLIENT DISCONNECT -------\n");
            conexao.close()
            break
    finally:
        conexao.close()
    serverSocket.close()