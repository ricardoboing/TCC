import pymysql
from util import *

DATABASE_HOST = "localhost"
DATABASE_USER = "boing"
DATABASE_PASSWORD = "boing12345"
DATABASE_NAME = "tcc"

# Le o conteudo recebido em uma conexao socket
def ler_conteudo_conexao(conexao, numeroBytes):
    return str(conexao.recv(numeroBytes).decode('utf-8'))

def banco(query):
    print(query)

    # Conecta ao banco de dados
    conexao = pymysql.connect(
        host=DATABASE_HOST,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        db=DATABASE_NAME
    )

    try:
        # Insere query ao banco de dados
        with conexao.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
        conexao.commit()

    finally:
        # Cancela operacao
        conexao.rollback()
    
    conexao.close()

    return data

def remover_evento(conexao, length_pacote):
    subQuery = ""
    numeroDeIds = int( (length_pacote-1)/4 );
    
    for c in range(numeroDeIds):
        idEvento = ler_conteudo_conexao(conexao,4)
        
        if c > 0:
            subQuery += ","
        subQuery += idEvento

    query = "DELETE FROM evento WHERE idEvento in ("+subQuery+");"
    banco(query)

# Atualiza as informacoes de um evento de acordo
# com os dados recebidos em uma conexao socket
def update_evento(conexao):
    idEvento = ler_conteudo_conexao(conexao,4)
    domingo = ler_conteudo_conexao(conexao,1)
    segunda = ler_conteudo_conexao(conexao,1)
    terca = ler_conteudo_conexao(conexao,1)
    quarta = ler_conteudo_conexao(conexao,1)
    quinta = ler_conteudo_conexao(conexao,1)
    sexta = ler_conteudo_conexao(conexao,1)
    sabado = ler_conteudo_conexao(conexao,1)
    somTocar = ler_conteudo_conexao(conexao,1)
    
    if somTocar == "1":
        somVolume = ler_conteudo_conexao(conexao,3)
        somTempoDuracao = ler_conteudo_conexao(conexao,2)
    else:
        somVolume = '000'
        somTempoDuracao = '00'
    
    horario = ler_conteudo_conexao(conexao,2)
    horario += ":"
    horario += ler_conteudo_conexao(conexao,2)

    lengthNome = int(ler_conteudo_conexao(conexao,2))
    nome = ler_conteudo_conexao(conexao,lengthNome)

    query = "UPDATE evento SET "
    query += "somTempoDuracao=%s," %(somTempoDuracao)
    query += "somVolume=%s," %(somVolume)
    query += "somTocar=%s," %(somTocar)
    query += "horario='%s'," %(horario)
    query += "nome='%s'," %(nome)
    query += "domingo=%s," %(domingo)
    query += "segunda=%s," %(segunda)
    query += "terca=%s," %(terca)
    query += "quarta=%s," %(quarta)
    query += "quinta=%s," %(quinta)
    query += "sexta=%s," %(sexta)
    query += "sabado=%s " %(sabado)
    query += "WHERE idEvento=%s;" %(idEvento)

    banco(query)

def insert_evento(conexao):
    domingo = ler_conteudo_conexao(conexao,1)
    segunda = ler_conteudo_conexao(conexao,1)
    terca = ler_conteudo_conexao(conexao,1)
    quarta = ler_conteudo_conexao(conexao,1)
    quinta = ler_conteudo_conexao(conexao,1)
    sexta = ler_conteudo_conexao(conexao,1)
    sabado = ler_conteudo_conexao(conexao,1)
    somTocar = ler_conteudo_conexao(conexao,1)
    
    if somTocar == "1":
        somVolume = ler_conteudo_conexao(conexao,3)
        somTempoDuracao = ler_conteudo_conexao(conexao,2)
    else:
        somVolume = '000'
        somTempoDuracao = '00'
    
    horario = ler_conteudo_conexao(conexao,2)
    horario += ":"
    horario += ler_conteudo_conexao(conexao,2)

    lengthNome = int(ler_conteudo_conexao(conexao,2))
    nome = conexao.recv(lengthNome).decode('utf-8')

    query = "INSERT INTO "
    query += "evento(nome,horario,domingo,segunda,terca,quarta,quinta,sexta,sabado,somTocar,somVolume,somTempoDuracao) "
    query += "VALUES("
    query += "'%s'," %(nome)
    query += "'%s'," %(horario)
    query += "%s," %(domingo)
    query += "%s," %(segunda)
    query += "%s," %(terca)
    query += "%s," %(quarta)
    query += "%s," %(quinta)
    query += "%s," %(sexta)
    query += "%s," %(sabado)
    query += "%s," %(somTocar)
    query += "%s," %(somVolume)
    query += "%s);" %(somTempoDuracao)
    banco(query)

def select_eventos():
    query = "SELECT idEvento,nome,domingo,segunda,terca,quarta,quinta,sexta,sabado,horario FROM evento;"
    data = banco(query)
    
    retorno = ""

    for linha in data:
        idEvento = str(linha[0])
        nome = str(linha[1]) # nao pode ter ascento
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

        hora = formatar_digitos(hora, 2)
        minuto = formatar_digitos(minuto, 2)

        lengthNome = str(len(nome))
        lengthNome = formatar_digitos(lengthNome, 2)

        lengthId = str(len(idEvento))
        lengthId = formatar_digitos(lengthId, 2)

        retorno += domingo
        retorno += segunda
        retorno += terca
        retorno += quarta
        retorno += quinta
        retorno += sexta
        retorno += sabado
        retorno += hora
        retorno += minuto
        retorno += lengthNome
        retorno += lengthId
        retorno += nome
        retorno += idEvento
    
    return retorno

def select_evento(conexao):
    idEvento = ler_conteudo_conexao(conexao,4)

    query = "SELECT nome,domingo,segunda,terca,quarta,quinta,sexta,sabado,horario,somTocar,somVolume,somTempoDuracao "
    query += "FROM evento where idEvento="+idEvento+";"
    data = banco(query)
    
    retorno = ""

    for linha in data:
        nome = str(linha[0]) # nao pode ter ascento
        domingo = str(linha[1])
        segunda = str(linha[2])
        terca = str(linha[3])
        quarta = str(linha[4])
        quinta = str(linha[5])
        sexta = str(linha[6])
        sabado = str(linha[7])

        horario = str(linha[8]).split(":")
        hora = formatar_digitos(horario[0], 2)
        minuto = formatar_digitos(horario[1], 2)
        
        somTocar = str(linha[9])
        
        somVolume = str(linha[10])
        somVolume = formatar_digitos(somVolume, 3)
        
        somTempoDuracao = str(linha[11])
        somTempoDuracao = formatar_digitos(somTempoDuracao, 2)

        lengthNome = str(len(nome))
        lengthNome = formatar_digitos(lengthNome, 2)

        lengthId = str(len(idEvento))
        lengthId = formatar_digitos(lengthId, 2)

        retorno += domingo
        retorno += segunda
        retorno += terca
        retorno += quarta
        retorno += quinta
        retorno += sexta
        retorno += sabado
        retorno += hora
        retorno += minuto
        if somTocar == "1":
            retorno += "1"
            retorno += somVolume
            retorno += somTempoDuracao
        else:
            retorno += "0"
        retorno += lengthNome
        retorno += nome
    
    return retorno