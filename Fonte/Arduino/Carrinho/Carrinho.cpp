#ifndef CARRINHO_CPP
#define CARRINHO_CPP

#include "Carrinho.hpp"

Carrinho::Carrinho() {}
Carrinho::Carrinho(int pinA1, int pinA2, int pinB1, int pinB2, int pinC1, int pinC2, int pinC3, int pinC4) {
	this->rodaA = new Roda(pinA1, pinA2);
	this->rodaB = new Roda(pinB1, pinB2);
	
	this->reservatorio = new Reservatorio(pinC1, pinC2, pinC3, pinC4);	
}
Carrinho::~Carrinho() {}

void Carrinho::andar_sentido_norte() {
	this->rodaA->girar_sentido_horario();
	this->rodaB->girar_sentido_horario();
}
void Carrinho::andar_sentido_sul() {
	this->rodaA->girar_sentido_anti_horario();
	this->rodaB->girar_sentido_anti_horario();
}
void Carrinho::parar() {
	this->rodaA->parar();
	this->rodaB->parar();
}
void Carrinho::abrir_reservatorio() {
	this->reservatorio->abrir();
}
void Carrinho::fechar_reservatorio() {
	this->reservatorio->fechar();
}

#endif