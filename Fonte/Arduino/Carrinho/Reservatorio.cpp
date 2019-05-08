#ifndef RESERVATORIO_CPP
#define RESERVATORIO_CPP

#include "Reservatorio.hpp"
#include <Arduino.h>

Reservatorio::Reservatorio() {}
Reservatorio::Reservatorio(int pin1, int pin2, int pin3, int pin4) {
	pinMode(pin1, OUTPUT);
	pinMode(pin2, OUTPUT);
	pinMode(pin3, OUTPUT);
	pinMode(pin4, OUTPUT);
}
Reservatorio::~Reservatorio() {}

void Reservatorio::abrir() {
	if (!this->isAberto) {

	}
}
void Reservatorio::fechar() {
	if (this->isAberto) {

	}	
}

#endif