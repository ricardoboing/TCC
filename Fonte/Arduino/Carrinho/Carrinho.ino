#include "Carrinho.hpp"
#include <SoftwareSerial.h>
#include <Ultrasonic.h>
SoftwareSerial antennaEsp(2, 3);
Carrinho carrinho(6, 7, 8, 9, 10, 11, 12, 13);
Ultrasonic ultrasonic(4, 5);

int estado = 0;
unsigned long tempoInicial = 0;
unsigned long tempoFinal = 0;
unsigned long intervaloEntreTempos = 0;
unsigned long tempoVoltaEsperado = 0;

float dist = 0;

void setup() {
	Serial.begin(115200);
    antennaEsp.begin(115200);
    esp_configure();
}
void esp_configure() {
    // Configuracoes iniciais
    esp_data_send("RST");
    esp_data_send("CWMODE=1");
    esp_data_send("CWJAP=\"GVT-DFDC\",\"S1F7586408\"");
    
    // Mostra ip do "no" dentro da rede
    esp_data_send("CIFSR");

    while(!antennaEsp.find("OK"));

    // Registra "no" iot no servidor
    esp_data_send("CIPSTART=\"TCP\",\"192.168.25.32\",8081");
    delay(2000);

    // Fecha conexao com o servidor
    esp_data_send("CIPCLOSE");
    delay(2000);

    // Cria servidor socket na porta 8080
    esp_data_send("CIPMUX=1");
    esp_data_send("CIPSERVER=1,8080");
    delay(2000);
}
void esp_data_send(String comando) {
    // Todo comando deve iniciar com "AT+" e terminar com "\r\n"
    comando = "AT+"+comando+"\r\n";
  
    String resposta;
    antennaEsp.print(comando);
  
    delay(2000);

    while(antennaEsp.available()) {
        char data = antennaEsp.read();
        resposta += data;
    }
  
    Serial.print(resposta);
}
float get_sensor_distancia() {
    long microsec = ultrasonic.timing();
    
    return ultrasonic.convert(microsec, Ultrasonic::CM);
}

void loop() {
    // Carrinho parado: verifica comando recebido (antena)
	if (estado == 0) {
		if (antennaEsp.available()) {
            delay(2000);
            while (antennaEsp.available()) antennaEsp.read();
            
            dist = get_sensor_distancia();

            carrinho.andar_sentido_sul();
			carrinho.abrir_reservatorio();

			estado = 1;
            tempoInicial = millis();
        }
	// Carrinho andando (sentido 1 - ida)
    } else if (estado == 1) {
        float distancia = get_sensor_distancia();
        
        if (distancia < 10 && distancia > 0) {
            carrinho.andar_sentido_norte();
            tempoFinal = millis();
            estado = 2;

            tempoVoltaEsperado = 2*tempoFinal - tempoInicial;

            
            delay(intervaloEntreTempos);
        }
	// Carrinho andando (sentido 2 - volta)
	} else {
        float distancia = get_sensor_distancia();
		//unsigned long tempoAtual = millis();
        //if (tempoVoltaEsperado <= tempoAtual) {
        if (dist <= distancia) {
            estado = 0;

            carrinho.parar();
            carrinho.fechar_reservatorio();
        }
    }
}
