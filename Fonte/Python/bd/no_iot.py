from bd.sql import *
from util import *

# 
def bd_no_iot_select_configuracoes():
	queryCampos = "velocidade, tempoDeAtividade, capacidadeDaBateria"
	queryTabela = "no_iot"
	queryAdicional = ""

	data = sql_select_all(queryCampos, queryTabela, queryAdicional)

	retorno = ""

	# Deve possuir apenas uma tupla na tabela
	for tupla in data:
		velocidade          = formatar_digitos(tupla[0],3)
		tempoDeAtividade    = formatar_digitos(tupla[1],3)
		capacidadeDaBateria = formatar_digitos(tupla[2],4)

		retorno += velocidade
		retorno += tempoDeAtividade
		retorno += capacidadeDaBateria

		break

	return retorno

#
def bd_no_iot_select_estimativa_de_consumo():
	print("")

	return "012345678901234567890123"

# 
def bd_no_iot_reset_estimativa_da_bateria():
	queryCampos = "reposicaoDaBateria=now()"

	queryTabela = "no_iot"
	queryCondicao = ""

	sql_update(queryTabela, queryCampos, queryCondicao)

	return "1"

def bd_no_iot_update_configuracoes(conexao):
	velocidade = ler_conteudo_conexao(conexao,3)
	tempoDeAtividade = ler_conteudo_conexao(conexao,3)
	capacidadeDaBateria = ler_conteudo_conexao(conexao,4)

	queryCampos = "velocidade=%s," %(velocidade)
	queryCampos += "tempoDeAtividade=%s," %(tempoDeAtividade)
	queryCampos += "capacidadeDaBateria=%s" %(capacidadeDaBateria)

	queryTabela = "no_iot"
	queryCondicao = ""

	sql_update(queryTabela, queryCampos, queryCondicao)

	return "1"


# update no_iot set velocidade=100, tempoDeAtividade=1, reposicaoDaBateria=now(), capacidadeDaBateria=100;
# select velocidade, tempoDeAtividade, reposicaoDaBateria, capacidadeDaBateria from no_iot;
# insert into no_iot(velocidade,tempoDeAtividade,reposicaoDaBateria,capacidadeDaBateria) values (100,60,now(),100);