#ifndef ANTENA_CPP
#define ANTENA_CPP

#include "Antena.hpp"

Antena::Antena(uint8_t pinCE, uint8_t pinCSN) {
	//SPI.begin();

	this->antena = new RF24(pinCE, pinCSN);
	this->endereco = 0x0;
}
Antena::~Antena() {}

bool Antena::iniciar_modo_escrita() {
	if (this->endereco == 0x0 || this->estaLigado) {
		Serial.println("iniciar_modo_escrita fail if");
		return false;
	}

	const byte address[6] = "00001";

	Serial.println("iniciar_modo_escrita...");
	this->antena->openWritingPipe(address);
	this->antena->setPALevel(RF24_PA_MIN);
	this->antena->printDetails();
	this->antena->stopListening();

	this->estaLigado = true;

	return true;
}
bool Antena::escrever(byte* dado) {
	if (!this->estaLigado) {
		if (!this->iniciar_modo_escrita()) {
			Serial.println("iniciar_modo_escrita fail");
			return false;
		}
	}

	Serial.println("RF24->write fail");
	const char t[] = "a";
	return this->antena->write(&t, sizeof(t));
}

void Antena::set_endereco(uint64_t endereco) {
	this->endereco = endereco;
}
void Antena::ligar() {
	this->antena->begin();
}

#endif