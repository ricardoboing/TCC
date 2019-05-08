#ifndef RODA_HPP
#define RODA_HPP

class Roda {
private:
	int pinA, pinB;

public:
	Roda();
	Roda(int pinA, int pinB);
	~Roda();

	void parar();
	void girar_sentido_horario();
	void girar_sentido_anti_horario();

};

#endif