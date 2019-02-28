#include "Antena.hpp"

Antena antena(8,7);

char dado[1];

void setup() {
	Serial.begin(9600);

	antena.ligar();
	antena.set_endereco(0xAABBCCDDEEFF);
	antena.iniciar_modo_escrita();
}

void loop() {
	int potenciometro;
	potenciometro = analogRead(A1);

	if (potenciometro < 200) {
		dado[0] = 'h';
	} else if (potenciometro < 400) {
		dado[0] = 'd';
	} else {
		dado[0] = 'a';
	}

	antena.escrever(dado);

	delay(1000);
}