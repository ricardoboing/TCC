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
  //carrinho.andar_sentido_norte();
  carrinho.andar_sentido_sul();
  //carrinho.parar();
  delay(3000);
  carrinho.andar_sentido_norte();
  delay(3000);
}