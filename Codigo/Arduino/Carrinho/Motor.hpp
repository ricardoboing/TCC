#ifndef MOTOR_HPP
#define MOTOR_HPP

class Motor {
private:
	int pinA, pinB;

public:
	Motor();
	Motor(int pinA, int pinB);
	~Motor();

	void desligar();
	void ligar_sentido_horario();
	void ligar_sentido_anti_horario();

};

#endif