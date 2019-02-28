#include "Motor.hpp"

class Carrinho {
private:
	Motor motorA, motorB;
	bool modoLigado;

public:
	Carrinho(int pinA1, int pinA2, int pinB1, int pinB2);
	~Carrinho();
	void andar_sentido_norte();
	void andar_sentido_sul();
	void desligar();

	bool ligado();
	bool desligado();

};
