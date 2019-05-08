#ifndef RESERVATORIO_HPP
#define RESERVATORIO_HPP

#include "Reservatorio.hpp"

class Reservatorio {
private:
	bool isAberto;

public:
	Reservatorio();
	Reservatorio(int pin1, int pin2, int pin3, int pin4);
	~Reservatorio();

	void abrir();
	void fechar();

};

#endif