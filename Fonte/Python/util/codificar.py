from util.util import formatar_digitos

def codificar_id(idEmDecimal):
	idEmDecimal = min(idEmDecimal, 33554432)

	idEmBits = bin(idEmDecimal)[2:]
	idEmBits = formatar_digitos(idEmBits, 25)

	byte1EmBits = idEmBits[0:5]
	byte2EmBits = idEmBits[5:10]
	byte3EmBits = idEmBits[10:15]
	byte4EmBits = idEmBits[15:20]
	byte5EmBits = idEmBits[20:25]

	byte1 = codificar_asc2(byte1EmBits)
	byte2 = codificar_asc2(byte2EmBits)
	byte3 = codificar_asc2(byte3EmBits)
	byte4 = codificar_asc2(byte4EmBits)
	byte5 = codificar_asc2(byte5EmBits)

	return byte1+byte2+byte3+byte4+byte5
def codificar_horario(hora,minuto):
	minuto += hora*60

	bits = bin(minuto)[2:]
	bytesEmBits = formatar_digitos(bits, 15)

	byte1EmBits = bytesEmBits[0:5]
	byte2EmBits = bytesEmBits[5:10]
	byte3EmBits = bytesEmBits[10:15]

	byte1 = codificar_asc2(byte1EmBits)
	byte2 = codificar_asc2(byte2EmBits)
	byte3 = codificar_asc2(byte3EmBits)

	return byte1+byte2+byte3
def codificar_dias_da_semana(domingo,segunda,terca,quarta,quinta,sexta,sabado):
	byte1EmBits = str(domingo)
	byte1EmBits += str(segunda)
	byte1EmBits += str(terca)
	byte1EmBits += str(quarta)
	byte1EmBits += str(quinta)

	byte2EmBits = "000"
	byte2EmBits += str(sexta)
	byte2EmBits += str(sabado)

	byte1 = codificar_asc2(byte1EmBits)
	byte2 = codificar_asc2(byte2EmBits)

	return byte1+byte2
def codificar_som(volume,duracaoEmSegundos):
	volumeEmBits = bin(volume)[2:]
	volumeEmBits = formatar_digitos(volumeEmBits, 7)

	duracaoEmBits = bin(duracaoEmSegundos)[2:]
	duracaoEmBits = formatar_digitos(duracaoEmBits, 6)

	byte1EmBits = volumeEmBits[0:5]
	byte2EmBits = "000"+volumeEmBits[5:7]
	byte3EmBits = duracaoEmBits[0:5]
	byte4EmBits = "0000"+duracaoEmBits[5:6]

	byte1 = codificar_asc2(byte1EmBits)
	byte2 = codificar_asc2(byte2EmBits)
	byte3 = codificar_asc2(byte3EmBits)
	byte4 = codificar_asc2(byte4EmBits)

	return byte1+byte2+byte3+byte4
def codificar_nome(nome):
	lengthEmDecimal = len(nome)

	lengthEmDecimal = min(lengthEmDecimal, 30)
	lengthEmBinario = bin(lengthEmDecimal)[2:]
	lengthEmBinario = formatar_digitos(lengthEmBinario, 5)

	byte1 = codificar_asc2(lengthEmBinario)

	return byte1+nome

def codificar_asc2(valorBinario):
	inteiro = int("10"+valorBinario, 2)
	return chr(inteiro)


'''
bitsInString = "111"
print(bitsInString)
k = int(bitsInString,2)
g = str(k).encode()
v = g.decode()
z = int(v)
print(g)
print(bin(z)[2:])
'''
'''
k = int("1111111", 2)
asc = chr(k)
inteiro = int(ord(asc))
print(asc)
print(inteiro)
bit = bin(inteiro)
'''