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