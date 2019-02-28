#ifndef ANTENA_HPP
#define ANTENA_HPP

#include "nRF24L01.h"
#include "RF24.h"
#include "RF24_config.h"
#include <SPI.h>

class Antena {
private:
	uint64_t endereco;
	bool estaLigado;
	
	RF24 *antena;

public:
	Antena(uint8_t pinCE, uint8_t pinCSN);
	~Antena();

	bool iniciar_modo_escrita();
	void escrever(byte* dado);
	
	void set_endereco(uint64_t endereco);
	void ligar();

};

#endif