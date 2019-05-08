#ifndef RODA_CPP
#define RODA_CPP

#include "Roda.hpp"
#include <Arduino.h>

Roda::Roda() {}
Roda::Roda(int pinA, int pinB) {
	pinMode(pinA, OUTPUT);
	pinMode(pinB, OUTPUT);

	this->pinA = pinA;
	this->pinB = pinB;
}
void Roda::parar() {
	digitalWrite(this->pinA, LOW);
	digitalWrite(this->pinB, LOW);
}
void Roda::girar_sentido_horario() {
	digitalWrite(this->pinA, HIGH);
	digitalWrite(this->pinB, LOW);
}
void Roda::girar_sentido_anti_horario() {
	digitalWrite(this->pinA, LOW);
	digitalWrite(this->pinB, HIGH);
}

#endif