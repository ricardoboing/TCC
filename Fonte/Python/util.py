# Acrescenta zeros ao lado esquerdo do valor numerico informado
def formatar_digitos(valor, numeroDeDigitosEsperado):
    numeroDeDigitosEsperado = int(numeroDeDigitosEsperado)
    valorStr = str(valor)
    lenghtValor = len(valorStr)

    # Se o valor for maior que o numeroDeDigitosEsperado entao corta o
    # valor e retorna. O corte acontece do valor mais a esquerda para
    # o mais a direita
    if lenghtValor > numeroDeDigitosEsperado:
        valorStr = valorStr[0:numeroDeDigitosEsperado]
        return valorStr

    numeroDeDigitosEmFalta = numeroDeDigitosEsperado - lenghtValor

    # Se o valor numerico for menor que o requisitado entao preenche o
    # lado esquerdo com zeros (0)
    for c in range(numeroDeDigitosEmFalta):
        valorStr = "0"+valorStr

    return valorStr

listaDiaDaSemana = ["segunda","terca","quarta","quinta","sexta","sabado","domingo"]

def menor_dia(dia1,dia2):
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

def menor_horario(horario1,horario2):
    if horario1 < horario2:
        return 1
    if horario1 > horario2:
        return 2
    return 0