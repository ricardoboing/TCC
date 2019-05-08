#ifndef CARRINHO_HPP
#define CARRINHO_HPP

#include "Roda.hpp"
#include "Reservatorio.hpp"

class Carrinho {
private:
	Roda *rodaA, *rodaB;
	Reservatorio *reservatorio;

public:
	Carrinho();
	Carrinho(int pinA1, int pinA2, int pinB1, int pinB2, int pinC1, int pinC2, int pinC3, int pinC4);
	~Carrinho();

	void andar_sentido_norte();
	void andar_sentido_sul();
	void parar();
	void abrir_reservatorio();
	void fechar_reservatorio();

};

#endif