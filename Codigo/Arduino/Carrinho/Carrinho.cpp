#ifndef CARRINHO_CPP
#define CARRINHO_CPP

#include "Carrinho.hpp"

Carrinho::Carrinho() {}
Carrinho::Carrinho(int pinA1, int pinA2, int pinB1, int pinB2) {
	this->motorA = new Motor(pinA1, pinA2);
	this->motorB = new Motor(pinB1, pinB2);
}
Carrinho::~Carrinho() {}

void Carrinho::andar_sentido_norte() {
	this->motorA->ligar_sentido_horario();
	this->motorB->ligar_sentido_horario();
}
void Carrinho::andar_sentido_sul() {
	this->motorA->ligar_sentido_anti_horario();
	this->motorB->ligar_sentido_anti_horario();
}
void Carrinho::parar() {
	this->motorA->desligar();
	this->motorB->desligar();
}

#endif