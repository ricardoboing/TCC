import socket
import pymysql
from datetime import datetime

SERVER_HOST = "192.168.50.179"#"192.168.25.6"
SERVER_PORT = 8082

DATABASE_HOST = "localhost"
DATABASE_USER = "boing"
DATABASE_PASSWORD = "boing12345"
DATABASE_NAME = "tcc"

def banco(query):
    conexao = pymysql.connect(
        host=DATABASE_HOST,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        db=DATABASE_NAME
    )

    try:
        with conexao.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
        conexao.commit()

    finally:
        conexao.rollback()
    
    conexao.close()

    return data

def insert_evento(conexao):
    domingo = conexao.recv(1).decode('utf-8')
    segunda = conexao.recv(1).decode('utf-8')
    terca = conexao.recv(1).decode('utf-8')
    quarta = conexao.recv(1).decode('utf-8')
    quinta = conexao.recv(1).decode('utf-8')
    sexta = conexao.recv(1).decode('utf-8')
    sabado = conexao.recv(1).decode('utf-8')
    somTocar = conexao.recv(1).decode('utf-8')
    
    if somTocar == 1 or somTocar == "1":
        somVolume = conexao.recv(3).decode('utf-8')
        somTempoDuracao = conexao.recv(2).decode('utf-8')
    else:
        somVolume = '000'
        somTempoDuracao = '00'
    
    horario = conexao.recv(2).decode('utf-8')
    horario += ":"
    horario += conexao.recv(2).decode('utf-8')
    lengthNome = int(conexao.recv(2).decode('utf-8'))
    nome = conexao.recv(lengthNome).decode('utf-8')

    querry = "INSERT INTO evento(nome,horario,domingo,segunda,terca,quarta,quinta,sexta,sabado,somTocar,somVolume,somTempoDuracao) VALUES ('%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);" %(nome,horario,domingo,segunda,terca,quarta,quinta,sexta,sabado,somTocar,somVolume,somTempoDuracao)
    banco(querry)

def remover_evento(conexao, length_pacote):
    print(length_pacote)
    subQuerry = ""
    
    numeroDeIds = int( (length_pacote-1)/4 );
    print(numeroDeIds)

    for c in range(numeroDeIds):
        print(c)
        idEvento = conexao.recv(4).decode('utf-8')
        if c > 0:
            subQuerry += ","
        subQuerry += idEvento

    querry = "DELETE FROM evento WHERE idEvento in ("+subQuerry+");"
    print(querry)
    banco(querry)

def select_eventos():
    querry = "SELECT idEvento,nome,domingo,segunda,terca,quarta,quinta,sexta,sabado,horario,somTocar,somVolume,somTempoDuracao FROM evento;"
    data = banco(querry)
    
    retorno = ""

    for linha in data:
        idEvento = str(linha[0])
        nome = str(linha[1]) # nao pode ter ascento se nao buga o role ;(
        domingo = str(linha[2])
        segunda = str(linha[3])
        terca = str(linha[4])
        quarta = str(linha[5])
        quinta = str(linha[6])
        sexta = str(linha[7])
        sabado = str(linha[8])

        horario = str(linha[9]).split(":")
        hora = horario[0]
        minuto = horario[1]

        if len(hora) < 2:
            hora = "0"+hora
        if len(minuto) < 2:
            minuto = "0"+minuto

        lengthNome = len(nome)
        lengthNomeString = str(lengthNome)

        if lengthNome < 10:
            lengthNomeString = "0" + lengthNomeString

        lengthId = len(idEvento)
        lengthIdString = str(lengthId)

        if lengthId < 10:
            lengthIdString = "0" + lengthIdString

        retorno += domingo
        retorno += segunda
        retorno += terca
        retorno += quarta
        retorno += quinta
        retorno += sexta
        retorno += sabado
        retorno += hora
        retorno += minuto
        retorno += lengthNomeString
        retorno += lengthIdString
        retorno += nome;
        retorno += idEvento
    
    return retorno

def ativar_servidor():
    serverSocket = socket.socket()
    serverSocket.bind((SERVER_HOST, SERVER_PORT))
    serverSocket.listen()
    
    print("SERVER CONNECT - HOST: %s | PORT : %s" %(SERVER_HOST, SERVER_PORT))

    try:
        while True:
            conexao = serverSocket.accept()[0]
            print("CLIENT CONNECT -------\n")

            length_pacote = int(conexao.recv(3).decode('utf-8'))
            operacao = conexao.recv(1).decode('utf-8')

            # INSERIR EVENTO
            if operacao == 'a':
                print("_INSERIR EVENTO")
                insert_evento(conexao)
                val_enviar = "1" # SUCESSO / ERRO
                conexao.sendall(val_enviar.encode())
            # REMOVER EVENTO
            elif operacao == 'b':
                print("_REMOVER EVENTO")
                remover_evento(conexao, length_pacote)
                # DELETE FROM Evento WHERE idEvento=4;
                val_enviar = "1"
                conexao.sendall(val_enviar.encode())
            # UPDATE EVENTO
            elif operacao == 'c':
                print("_UPDATE EVENTO")
                # UPDATE Evento SET somTempoDuracao=1,somTocar=1,horario='08:07',nome='Evento Y',domingo=1,segunda=1,terca=1,quarta=1,quinta=1,sexta=1,sabado=1 WHERE idEvento=5;
            # UPDATE TARIFA
            elif operacao == 'd':
                print("_UPDATE TARIFA")
            # SELECT_ALL EVENTO NO BANCO DE DADOS
            elif operacao == 'g':
                print("_SELECT_ALL EVENTO")
                # PRECISA ENVIAR SUCESSO / ERRO JUNTO
                val_enviar = select_eventos()
                # SELECT * FROM Evento;
                conexao.sendall(val_enviar.encode())
            elif operacao == 'e':
                print("_SELECT ESTIMATIVA DE CONSUMO")
                
                val_enviar = "abcdefghij123456089" #00001111 00001111 000
                conexao.sendall(val_enviar.encode())
            elif operacao == 'f':
                print("_SELECT EVENTO")
                # SELECT * FROM Evento WHERE idEvento=1;

            if length_pacote > 1:
                print("PACOTE: %s" %(conexao.recv(length_pacote).decode('utf-8')));
            print("PACOTE_SIZE: %s" %(length_pacote))
            
            print ("\nCLIENT DISCONNECT -------\n");
            conexao.close()
    finally:
        conexao.close()
    serverSocket.close()

if __name__ == "__main__":
	ativar_servidor()
