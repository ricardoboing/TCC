
class Motor {
private:
	int pinA, pinB;
	bool ligado;

public:
	Motor(int pinA, int pinB);
	~Motor();
	void desligar();
	void ligar_sentido_horario();
	void ligar_sentido_anti_horario();

};
