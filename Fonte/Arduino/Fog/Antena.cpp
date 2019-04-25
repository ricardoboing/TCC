#ifndef ANTENA_CPP
#define ANTENA_CPP

#include "Antena.hpp"

Antena::Antena(uint8_t pinCE, uint8_t pinCSN) {
	SPI.begin();

	this->antena = new RF24(pinCE, pinCSN);
	this->endereco = 0x0;
}
Antena::~Antena() {}

bool Antena::iniciar_modo_escrita() {
	if (this->endereco == 0x0 || this->estaLigado) {
		return false;
	}

	this->antena->openWritingPipe(this->endereco);
	this->antena->printDetails();

	this->estaLigado = true;

	return true;
}
bool Antena::escrever(byte* dado) {
	if (!this->estaLigado) {
		if (!this->iniciar_modo_escrita()) {
			return false;
		}
	}

	this->antena->write(&dado, sizeof(dado));

	return true;
}

void Antena::set_endereco(uint64_t endereco) {
	this->endereco = endereco;
}
void Antena::ligar() {
	this->antena->begin();
}

#endif