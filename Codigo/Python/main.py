import socket

SERVER_HOST = "yyy.yyy.yyy.yyy"
SERVER_PORT = 8081

def ativar_servidor():
    serverSocket = socket.socket()
    serverSocket.bind((SERVER_HOST, SERVER_PORT))
    serverSocket.listen()
    
    while True:
        conexao = serverSocket.accept()[0]
        
        dados = conexao.recv(4096)
        dados = dados.decode('utf-8')

        print(dados);
        print ("\n")
        conexao.close()

    serverSocket.close()

if __name__ == "__main__":
	ativar_servidor()