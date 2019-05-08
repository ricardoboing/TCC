import socket
from banco_de_dados import *

SERVER_HOST = "192.168.50.179"#"192.168.25.6"
SERVER_PORT = 8084

def ativar_servidor():
    serverSocket = socket.socket()
    serverSocket.bind((SERVER_HOST, SERVER_PORT))
    serverSocket.listen()
    
    print("SERVER CONNECT - HOST: %s | PORT : %s" %(SERVER_HOST, SERVER_PORT))

    try:
        while True:
            conexao = serverSocket.accept()[0]
            print("CLIENT CONNECT -------\n")

            length_pacote = int(ler_conteudo_conexao(conexao,3))
            operacao = str(ler_conteudo_conexao(conexao,1))

            # INSERIR EVENTO
            if operacao == 'a':
                print("_INSERIR EVENTO")
                
                val_enviar = "1" # SUCESSO / ERRO
                insert_evento(conexao)
            
            # REMOVER EVENTO
            elif operacao == 'b':
                print("_REMOVER EVENTO")
                
                val_enviar = "1"                
                remover_evento(conexao, length_pacote)
            
            # UPDATE EVENTO
            elif operacao == 'c':
                print("_UPDATE EVENTO")
                
                val_enviar = "1"
                update_evento(conexao)
            
            # SELECT EVENTO
            elif operacao == 'd':
                print("_SELECT EVENTO")
                
                val_enviar = select_evento(conexao)

            # SELECT_ALL EVENTO NO BANCO DE DADOS
            elif operacao == 'e':
                print("_SELECT_ALL EVENTO")
                
                val_enviar = select_eventos()

            # SELECT ESTIMATIVA DE CONSUMO
            elif operacao == 'f':
                print("_SELECT ESTIMATIVA DE CONSUMO")
                
                val_enviar = "abcdefghij123456089" #00001111 00001111 000

            #if length_pacote > 1:
            #    print("PACOTE: %s" %(conexao.recv(length_pacote).decode('utf-8')));
            print("PACOTE_SIZE: %s" %(length_pacote))
            
            conexao.sendall(val_enviar.encode())

            print ("\nCLIENT DISCONNECT -------\n");
            conexao.close()
    finally:
        conexao.close()
    serverSocket.close()