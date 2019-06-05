#ifndef RESERVATORIO_CPP
#define RESERVATORIO_CPP

#include "Reservatorio.hpp"
#include <Arduino.h>

Reservatorio::Reservatorio() {}
Reservatorio::Reservatorio(int pin1, int pin2, int pin3, int pin4) {
	this->motor = new Stepper(500, pin1, pin2, pin3, pin4);
	this->motor->setSpeed(60);

	this->isAberto = false;
}
Reservatorio::~Reservatorio() {}

void Reservatorio::abrir() {
	if (!this->isAberto) {
		this->motor->step(1024);
		this->isAberto = true;
	}
}
void Reservatorio::fechar() {
	if (this->isAberto) {
		this->motor->step(-1024);
		this->isAberto = false;
	}
}

#endif