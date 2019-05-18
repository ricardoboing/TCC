from datetime import datetime, date
from bd.sql import *

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

class Evento:
    def __init__(self):
        self.idEvento = 0
        self.diaEvento = ""
        self.horarioEvento = ""
        self.tocarSom = False
        self.volumeSom = 0
        self.somTempoDuracaoSom = 0
        self.listaDiaDaSemana = ["domingo", "segunda", "terca", "quarta", "quinta", "sexta", "sabado"]

    def buscar_proximo_evento(self):
        diaNumericoDaSemana = date.today().weekday()
        horarioAtual = datetime.now().strftime("%H:%M")

        for c in range (0,7):
            diaNumericoDaSemanaASerBuscado = (diaNumericoDaSemana + c) % 7
            diaStringDaSemana = self.listaDiaDaSemana[diaNumericoDaSemanaASerBuscado]
            
            queryCampos = "idEvento,horario,somTocar,somVolume,somTempoDuracao"
            queryTabela = "evento"
            queryCondicao = "%s=1 AND horario > \"%s\"" %(diaStringDaSemana, horarioAtual)
            queryAdicional = "ORDER BY horario ASC LIMIT 1"
            
            tuplas = sql_select(queryCampos, queryTabela, queryCondicao, queryAdicional)

            possuiTupla = False
            for tupla in tuplas:
                possuiTupla = True
                self.idEvento = tupla[0]
                self.diaEvento = diaStringDaSemana
                self.horarioEvento = str(tupla[1])
                self.tocarSom = tupla[2]
                self.volumeSom = tupla[3]
                self.somTempoDuracaoSom = tupla[4]

            if possuiTupla:
                break
            
            horarioAtual = "00:00"

    def disparar_agora(self):
        horarioAtual = str(datetime.now().strftime("%H:%M:00"))
        print(horarioAtual)
        print(self.horarioEvento)

        # SE horarioEvento <= horarioAtual
        if horarioAtual >= self.horarioEvento:
            self.buscar_proximo_evento()
            return 1

        return 0

    def menor_dia(self,dia1,dia2):
        indiceDia1 = -1
        indiceDia2 = -1
        for c in range(0,6):
            if listaDiaDaSemana[c] == dia1:
                indiceDia1 = c
            if listaDiaDaSemana[c] == dia2:
                indiceDia2 = c

        if indiceDia1 < indiceDia2:
            return 1
        if indiceDia1 > indiceDia2:
            return 2
        return 0