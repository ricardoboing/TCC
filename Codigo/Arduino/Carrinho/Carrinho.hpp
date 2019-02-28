#ifndef CARRINHO_HPP
#define CARRINHO_HPP

#include "Motor.hpp"

class Carrinho {
private:
	Motor *motorA, *motorB;

public:
	Carrinho();
	Carrinho(int pinA1, int pinA2, int pinB1, int pinB2);
	~Carrinho();

	void andar_sentido_norte();
	void andar_sentido_sul();
	void parar();

};

#endif