from datetime import datetime, date

from bd.sql import *
from util.util import *
from util.codificar import *
from util.decodificar import *

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
        horario = str(horario1)+":"+str(horario2)
        domingo =  ((c*4) % 11) % 2
        segunda =  ((c*5) % 10) % 2
        terca =  ((c*6) % 9) % 2
        quarta =  ((c*7) % 8) % 2
        quinta =  ((c*8) % 7) % 2
        sexta =  ((c*3) % 6) % 2
        sabado =  ((c*4) % 9) % 2
        somTocar =  ((c*5) % 4) % 2
        values += "(\"evento %s\",\"%s\",%s,%s,%s,%s,%s,%s,%s,%s,5,50)" %(nome,horario,domingo,segunda,terca,quarta,quinta,sexta,sabado,somTocar)

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

def bd_evento_delete(conexao):
    numeroDeIds = decodificar_inteiro(conexao,1)

    subQuery = ""
    for c in range(numeroDeIds):
        idEvento = str(decodificar_id(conexao))
        
        if c > 0:
            subQuery += ","
        subQuery += idEvento

    query = "DELETE FROM evento WHERE idEvento in ("+subQuery+");"
    
    banco(query)

    return "1"

# Atualiza as informacoes de um evento de acordo
# com os dados recebidos em uma conexao socket
def bd_evento_update(conexao, somHabilitado):
    idEvento = str(decodificar_id(conexao))
    diasDaSemana = decodificar_dias_da_semana(conexao)

    domingo = diasDaSemana[0]
    segunda = diasDaSemana[1]
    terca   = diasDaSemana[2]
    quarta  = diasDaSemana[3]
    quinta  = diasDaSemana[4]
    sexta   = diasDaSemana[5]
    sabado  = diasDaSemana[6]

    if somHabilitado:
        som = decodificar_som(conexao)

        somVolume = som[0]
        somTempoDuracao = som[1]
    else:
        somVolume = 0
        somTempoDuracao = 0

    horario = decodificar_horario(conexao)
    nome = decodificar_nome(conexao)

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

def bd_evento_insert(conexao, somHabilitado):
    diasDaSemana = decodificar_dias_da_semana(conexao)

    domingo = diasDaSemana[0]
    segunda = diasDaSemana[1]
    terca   = diasDaSemana[2]
    quarta  = diasDaSemana[3]
    quinta  = diasDaSemana[4]
    sexta   = diasDaSemana[5]
    sabado  = diasDaSemana[6]

    if somHabilitado:
        som = decodificar_som(conexao)

        somVolume = som[0]
        somTempoDuracao = som[1]
    else:
        somVolume = 0
        somTempoDuracao = 0

    horario = decodificar_horario(conexao)
    nome = decodificar_nome(conexao)

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

def bd_evento_select(idEvento):#conexao):
    #idEvento = str(decodificar_id(conexao))

    query = "SELECT nome,domingo,segunda,terca,quarta,quinta,sexta,sabado,horario,somTocar,somVolume,somTempoDuracao "
    query += "FROM evento where idEvento="+idEvento+";"
    data = banco(query)
    
    retorno = ""

    for tupla in data:
        nome = str(tupla[0]) # nao pode ter ascento
        
        diasDaSemana = codificar_dias_da_semana(tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],tupla[6],tupla[7])

        horario = str(tupla[8]).split(":")
        horario = codificar_horario(horario[0],horario[1])

        somHabilitado = str(tupla[9])
        som = codificar_som(linha[10],tupla[11])

        lengthNome = str(len(nome))
        lengthNome = formatar_digitos(lengthNome, 2)

        retorno += diasDaSemana
        retorno += horario
        
        if somHabilitado == "1":
            retorno += "1"
            retorno += som
        else:
            retorno += "0"

        retorno += codificar_nome(nome)
    
    return retorno