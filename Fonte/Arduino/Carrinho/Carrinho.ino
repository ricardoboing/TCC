#include "Carrinho.hpp"
#include "Antena.hpp"

Antena antena(8,7);
Carrinho carrinho(3, 4, 6, 5);

byte dado[1];

void setup() {
	Serial.begin(57600);

	antena.ligar();
	antena.set_endereco(0xAABBCCDDEEFF);
	antena.iniciar_modo_leitura();
}

void loop() {
	antena.ler(dado);

	if (antena.disponiveis() > 0) {
		switch (dado[0]) {
			case 'h':
				carrinho.andar_sentido_norte();
				Serial.println("andar_norte");
				break;
			case 'a':
				carrinho.andar_sentido_sul();
				Serial.println("andar_sul");
				break;
			default:
				carrinho.parar();
				Serial.println("desligar");
				break;
		}
	}

	delay(1000);
}