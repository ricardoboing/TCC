# Le o conteudo recebido em uma conexao socket
def ler_conteudo_conexao(conexao, numeroBytes):
    return str(conexao.recv(numeroBytes).decode('utf-8'))

def decodificar_id(conexao):
    valorCodificado = ler_conteudo_conexao(conexao,5)

    byte1EmBits = decodificar_asc2_para_binario(valorCodificado[0:1])
    byte2EmBits = decodificar_asc2_para_binario(valorCodificado[1:2])
    byte3EmBits = decodificar_asc2_para_binario(valorCodificado[2:3])
    byte4EmBits = decodificar_asc2_para_binario(valorCodificado[3:4])
    byte5EmBits = decodificar_asc2_para_binario(valorCodificado[4:5])

    idEmBytes = byte1EmBits+byte2EmBits+byte3EmBits+byte4EmBits+byte5EmBits
    return decodificar_binario_para_inteiro(idEmBytes)

def decodificar_horario(conexao):
    valorCodificado = ler_conteudo_conexao(conexao,3)

    byte1EmBits = decodificar_asc2_para_binario(valorCodificado[0:1])
    byte2EmBits = decodificar_asc2_para_binario(valorCodificado[1:2])
    byte3EmBits = decodificar_asc2_para_binario(valorCodificado[2:3])

    horarioEmBits = byte1EmBits+byte2EmBits+byte3EmBits
    horarioEmInteiro = decodificar_binario_para_inteiro(horarioEmBits)
    
    horaEmInteiro = int(horarioEmInteiro/60)
    minutoEmInteiro = int(horarioEmInteiro % 60)

    hora = str(horaEmInteiro)
    minuto = str(minutoEmInteiro)
    
    horario = hora+":"+minuto

    return horario

def decodificar_dias_da_semana(conexao):
    valorCodificado = ler_conteudo_conexao(conexao,2)

    byte1EmBits = decodificar_asc2_para_binario(valorCodificado[0:1])
    byte2EmBits = decodificar_asc2_para_binario(valorCodificado[1:2])

    retorno = []
    retorno.append(byte1EmBits[0:1])
    retorno.append(byte1EmBits[1:2])
    retorno.append(byte1EmBits[2:3])
    retorno.append(byte1EmBits[3:4])
    retorno.append(byte1EmBits[4:5])

    retorno.append(byte2EmBits[3:4])
    retorno.append(byte2EmBits[4:5])

    return retorno

def decodificar_som(conexao):
    valorCodificado = ler_conteudo_conexao(conexao,4)

    byte1EmBits = decodificar_asc2_para_binario(valorCodificado[0:1])
    byte2EmBits = decodificar_asc2_para_binario(valorCodificado[1:2])[3:5]
    byte3EmBits = decodificar_asc2_para_binario(valorCodificado[2:3])
    byte4EmBits = decodificar_asc2_para_binario(valorCodificado[3:4])[4:5]

    volumeEmBits = byte1EmBits+byte2EmBits
    duracaoEmBits = byte3EmBits+byte4EmBits

    volumeEmInteiro = decodificar_binario_para_inteiro(volumeEmBits)
    duracaoEmInteiro = decodificar_binario_para_inteiro(duracaoEmBits)

    return [volumeEmInteiro,duracaoEmInteiro]
def decodificar_nome(conexao):
    lenghtNome = ler_conteudo_conexao(conexao,1)

    lengthByte1EmBits = decodificar_asc2_para_binario(lenghtNome)
    lengthEmInteiro = decodificar_binario_para_inteiro(lengthByte1EmBits)

    nome = ler_conteudo_conexao(conexao,lengthEmInteiro)

    return nome
def decodificar_inteiro(conexao,numeroBytes):
    byte1 = ler_conteudo_conexao(conexao,1)

    byte1EmBits = decodificar_asc2_para_binario(byte1)
    inteiro = decodificar_binario_para_inteiro(byte1EmBits)

    return inteiro

def decodificar_asc2_para_binario(valorCodificado):
    '''
        O valorCodificado esta no formato 0bABXXXXX, onde:
        0b: representa o bit que nao se usa em asc
        A: Sempre 0 pra garantir que o valor seja < 0b111 1111
        B: Sempre 1 para garantir que o valor seja imprimivel em ASCII
        XXXXX: Do bit 4 ao 8 sao os bits utilizados
    '''
    inteiro = int(ord(valorCodificado))
    return bin(inteiro)[4:]
def decodificar_binario_para_inteiro(valorCodificado):
    return int(valorCodificado,2)