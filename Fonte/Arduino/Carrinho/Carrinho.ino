#include "Carrinho.hpp"
#include "Antena.hpp"

Antena antena(8,7);
Carrinho carrinho(3, 4, 6, 5, 1, 2, 9, 10);

int estado = 0;
int contador = 0;

void setup() {
	Serial.begin(9600);
}

void loop() {
	char valor[] = "a";

	// Carrinho parado: verifica comando recebido (antena)
	if (estado == 0) {
		Serial.println(contador);
		if (valor[0] == 'a') {
			carrinho.andar_sentido_sul();
			carrinho.abrir_reservatorio();

			estado = 1;
			contador = 0;
		}
	// Carrinho andando (sentido 1 - ida)
	} else if (estado == 1) {
		contador++;
		if (contador > 15) {
			estado = 2;
		}
	// Carrinho andando (sentido 2 - volta)
	} else {
		contador--;
		if (contador <= 0) {
			estado = 0;
		}
	}

	//Serial.print(estado);
	
}