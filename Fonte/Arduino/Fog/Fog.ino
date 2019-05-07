#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"

// Armazena caractere digitado na serial
char valor[1];

// Armazena os dados enviados
int dados[1];

// Inicializa o NRF24L01 nos pinos 9 (CE) e 10 (CS) do Arduino Uno
RF24 radio(9,10);

// Define o endereco para comunicacao entre os modulos
const uint64_t pipe = 0xE13CBAF433LL;

void setup()
{
  // Inicializa a serial
  Serial.begin(57600);
  Serial.println("Digite 1, 2 ou L e pressione ENVIAR...");
  
  // Inicializa a comunicacao do NRF24L01
  radio.begin();
  // Entra em modo de transmissao
  radio.openWritingPipe(pipe);
}

void loop() {
	dados[0] = 1;
	Serial.println(radio.write(dados, 1));
	delay(100);
}