from datetime import datetime, date

from bd.sql import banco, ler_conteudo_conexao
from util import *

idProximoEvento = 0
diaProximoEvento = ""
horarioProximoEvento = ""
tocarSom = False
volumeSom = 0
somTempoDuracaoSom = 0

def proximo_evento(diaEvento1,horarioEvento1,diaEvento2,horarioEvento2):
    # Verifica qual o evento ocorre primeiro pelo dia
    if menor_dia(diaEvento1,diaEvento2) == 1:
        return 1
    if menor_dia(diaEvento1,diaEvento2) == 2:
        return 2

    # Se os eventos ocorrem no mesmo dia entao busca pelo horario
    if menor_horario(horarioEvento1,horarioEvento2) == 1:
        return 1
    if menor_horario(horarioEvento1,horarioEvento2) == 2:
        return 2

    return 0

# Gerar dados aleatorios para testes
def gerador_aleatorio_de_eventos():
    query = "insert into evento(nome,horario,domingo,segunda,terca,quarta,quinta,sexta,sabado,somTocar,somTempoDuracao,somVolume) values "
    
    values = ""
    for c in range(0,5000):
        if c != 0:
            values += ","

        nome = c+10
        horario1 = (c*3) % 24
        horario2 = (c*7) % 60
        horario  = str(horario1)+":"+str(horario2)
        domingo  =  ((c*4) % 11) % 2
        segunda  =  ((c*5) % 10) % 2
        terca    =  ((c*6) % 9) % 2
        quarta   =  ((c*7) % 8) % 2
        quinta   =  ((c*8) % 7) % 2
        sexta    =  ((c*3) % 6) % 2
        sabado   =  ((c*4) % 9) % 2
        somTocar =  ((c*5) % 4) % 2
        values  += "(\"evento %s\",\"%s\",%s,%s,%s,%s,%s,%s,%s,%s,5,50)" %(nome,horario,domingo,segunda,terca,quarta,quinta,sexta,sabado,somTocar)

    query += values+";"
    #print(query)
    banco(query)

def banco_proximo_evento():
    diaNumericoDaSemana = date.today().weekday()
    horarioAtual = datetime.now().strftime("%H:%M")

    for c in range (0,7):
        diaNumericoDaSemanaASerBuscado = (diaNumericoDaSemana + c) % 7
        diaStringDaSemana = listaDiaDaSemana[diaNumericoDaSemanaASerBuscado]
        query = "select idEvento,horario,somTocar,somVolume,somTempoDuracao,nome from evento where %s=1 and horario > \"%s\" order by horario asc limit 1;" %(diaStringDaSemana, horarioAtual)
    
        tuplas = banco(query)

        possuiTupla = False

        for tupla in tuplas:
            possuiTupla = True
            idProximoEvento = tupla[0]
            diaProximoEvento = diaStringDaSemana
            horarioProximoEvento = tupla[1]
            tocarSom = tupla[2]
            volumeSom = tupla[3]
            somTempoDuracaoSom = tupla[4]
        if possuiTupla:
            break
        
        horarioAtual = "00:00"

    print(idProximoEvento)
    print(diaProximoEvento)
    print(horarioProximoEvento)
    print(tocarSom)
    print(volumeSom)
    print(somTempoDuracaoSom)

def bd_evento_remove(conexao):
    numeroDeIds = int( ler_conteudo_conexao(conexao,3) );

    subQuery = ""
    for c in range(numeroDeIds):
        idEvento = ler_conteudo_conexao(conexao,10)
        
        if c > 0:
            subQuery += ","
        subQuery += idEvento

    query = "DELETE FROM evento WHERE idEvento in ("+subQuery+");"
    
    banco(query)

    return "1"

# Atualiza as informacoes de um evento de acordo
# com os dados recebidos em uma conexao socket
def bd_evento_update(conexao):
    idEvento = ler_conteudo_conexao(conexao,10)
    domingo  = ler_conteudo_conexao(conexao,1)
    segunda  = ler_conteudo_conexao(conexao,1)
    terca    = ler_conteudo_conexao(conexao,1)
    quarta   = ler_conteudo_conexao(conexao,1)
    quinta   = ler_conteudo_conexao(conexao,1)
    sexta    = ler_conteudo_conexao(conexao,1)
    sabado   = ler_conteudo_conexao(conexao,1)
    
    somHabilitado = ler_conteudo_conexao(conexao,1)
    
    if somHabilitado == "1":
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
    query += "somTocar=%s," %(somHabilitado)
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

    return "1"

def bd_evento_insert(conexao):
    domingo = ler_conteudo_conexao(conexao,1)
    segunda = ler_conteudo_conexao(conexao,1)
    terca   = ler_conteudo_conexao(conexao,1)
    quarta  = ler_conteudo_conexao(conexao,1)
    quinta  = ler_conteudo_conexao(conexao,1)
    sexta   = ler_conteudo_conexao(conexao,1)
    sabado  = ler_conteudo_conexao(conexao,1)
    
    somHabilitado = ler_conteudo_conexao(conexao,1)

    if somHabilitado == "1":
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
    query += "%s," %(somHabilitado)
    query += "%s," %(somVolume)
    query += "%s);" %(somTempoDuracao)
    
    banco(query)

    return "1"

def bd_evento_select_all():
    query = "SELECT domingo,segunda,terca,quarta,quinta,sexta,sabado,horario,idEvento,nome FROM evento;"
    data = banco(query)
    
    retorno = ""

    for tupla in data:
        domingo  = str(tupla[0])
        segunda  = str(tupla[1])
        terca    = str(tupla[2])
        quarta   = str(tupla[3])
        quinta   = str(tupla[4])
        sexta    = str(tupla[5])
        sabado   = str(tupla[6])

        horario = formatar_horario(tupla[7])
        idEvento = formatar_id(tupla[8])
        nome = formatar_nome(str(tupla[9])) # nao pode ter ascento

        retorno += idEvento
        retorno += domingo
        retorno += segunda
        retorno += terca
        retorno += quarta
        retorno += quinta
        retorno += sexta
        retorno += sabado
        retorno += horario
        retorno += nome
        
    return retorno

def bd_evento_select(conexao):
    idEvento = ler_conteudo_conexao(conexao,10)

    query = "SELECT domingo,segunda,terca,quarta,quinta,sexta,sabado,horario,somTocar,somVolume,somTempoDuracao,nome "
    query += "FROM evento where idEvento="+idEvento+";"
    data = banco(query)
    
    retorno = ""

    for tupla in data:
        domingo = str(tupla[0])
        segunda = str(tupla[1])
        terca   = str(tupla[2])
        quarta  = str(tupla[3])
        quinta  = str(tupla[4])
        sexta   = str(tupla[5])
        sabado  = str(tupla[6])

        horario = formatar_horario(tupla[7])
        som = formatar_som(tupla[8],tupla[9],tupla[10])
        nome = formatar_nome(str(tupla[11])) # nao pode ter ascento

        retorno += domingo
        retorno += segunda
        retorno += terca
        retorno += quarta
        retorno += quinta
        retorno += sexta
        retorno += sabado
        retorno += horario
        retorno += som
        retorno += nome
    
    return retorno

def formatar_horario(horario):
    horario = str(horario).split(":")

    hora = formatar_digitos(horario[0],2)
    minuto = formatar_digitos(horario[1],2)

    return hora+minuto

def formatar_som(somHabilitado,somVolume,somTempoDuracao):
    somHabilitado = str(somHabilitado)
    somVolume = formatar_digitos(somVolume,3)
    somTempoDuracao = formatar_digitos(somTempoDuracao,2)

    if somHabilitado == "1":
        return somHabilitado+somVolume+somTempoDuracao
    return somHabilitado

def formatar_nome(nome):
    lengthNome = str(len(nome))
    lengthNome = formatar_digitos(lengthNome, 2)

    return lengthNome+nome

def formatar_id(id):
    return formatar_digitos(id, 10)