
class Antena {
private:
	bool modoLeitura;

public:
	Antena(int pinCE, int pinCSN);
	~Antena();
	void set_modo_leitura();
	void set_modo_escrita();

	bool modo_leitura();
	bool modo_escrita();

	void ligar();
	void desligar();

};
