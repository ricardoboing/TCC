from bd.sql import *
from util import *

def bd_agendamento_remove(conexao):
    numeroDeIds = int( ler_conteudo_conexao(conexao,3) );

    queryCondicaoValoresIn = ""
    for c in range(numeroDeIds):
        idEvento = ler_conteudo_conexao(conexao,10)

        if c > 0:
            queryCondicaoValoresIn += ","
        queryCondicaoValoresIn += idEvento

    queryTabela = "evento_agendamento"
    queryCondicaoCampo = "idAgendamento"

    sql_delete_where_in(queryTabela, queryCondicaoCampo, queryCondicaoValoresIn)

    return "1"

# Atualiza as informacoes de um evento de acordo
# com os dados recebidos em uma conexao socket
def bd_agendamento_update(conexao):
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

    queryCampos = "somTempoDuracao=%s," %(somTempoDuracao)
    queryCampos += "somVolume=%s," %(somVolume)
    queryCampos += "somTocar=%s," %(somHabilitado)
    queryCampos += "horario='%s'," %(horario)
    queryCampos += "nome='%s'," %(nome)
    queryCampos += "domingo=%s," %(domingo)
    queryCampos += "segunda=%s," %(segunda)
    queryCampos += "terca=%s," %(terca)
    queryCampos += "quarta=%s," %(quarta)
    queryCampos += "quinta=%s," %(quinta)
    queryCampos += "sexta=%s," %(sexta)
    queryCampos += "sabado=%s " %(sabado)

    queryTabela = "evento_agendamento"
    queryCondicao = "idAgendamento=%s" %(idEvento)

    sql_update(queryTabela, queryCampos, queryCondicao)

    return "1"

def bd_agendamento_insert(conexao):
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
    
    queryCampos = "nome,horario,domingo,segunda,terca,quarta,quinta,sexta,sabado,somTocar,somVolume,somTempoDuracao"
    queryTabela = "evento_agendamento"
    queryDados = "'%s'," %(nome)
    queryDados += "'%s'," %(horario)
    queryDados += "%s," %(domingo)
    queryDados += "%s," %(segunda)
    queryDados += "%s," %(terca)
    queryDados += "%s," %(quarta)
    queryDados += "%s," %(quinta)
    queryDados += "%s," %(sexta)
    queryDados += "%s," %(sabado)
    queryDados += "%s," %(somHabilitado)
    queryDados += "%s," %(somVolume)
    queryDados += "%s" %(somTempoDuracao)

    sql_insert(queryCampos, queryTabela, queryDados)

    return "1"

def bd_agendamento_select_all():
    queryCampos = "domingo,segunda,terca,quarta,quinta,sexta,sabado,horario,idAgendamento,nome"
    queryTabela = "evento_agendamento"
    queryAdicional = "ORDER BY horario ASC"

    data = sql_select_all(queryCampos, queryTabela, queryAdicional)

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
        nome = formatar_nome(str(tupla[9]))

        retorno += idEvento
        retorno += domingo
        retorno += segunda
        retorno += terca
        retorno += quarta
        retorno += quinta
        retorno += sexta
        retorno += sabado
        retorno += horario
        retorno += "%s" %(nome)

    return retorno

def bd_agendamento_select(conexao):
    idEvento = ler_conteudo_conexao(conexao,10)

    queryCampos = "domingo,segunda,terca,quarta,quinta,sexta,sabado,horario,somTocar,somVolume,somTempoDuracao,nome"
    queryTabela = "evento_agendamento"
    queryCondicao = "idAgendamento=%s" %(idEvento)
    queryAdicional = ""
    
    data = sql_select(queryCampos, queryTabela, queryCondicao, queryAdicional)

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
    nomeEncode = nome.encode("utf8")
    lengthNome = str(len(nomeEncode))
    lengthNome = formatar_digitos(lengthNome, 2)

    return lengthNome+nome

def formatar_id(id):
    return formatar_digitos(id, 10)