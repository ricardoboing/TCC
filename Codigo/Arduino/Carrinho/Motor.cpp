#ifndef MOTOR_CPP
#define MOTOR_CPP

#include "Motor.hpp"
#include <Arduino.h>

Motor::Motor() {}
Motor::Motor(int pinA, int pinB) {
	pinMode(pinA, OUTPUT);
	pinMode(pinB, OUTPUT);

	this->pinA = pinA;
	this->pinB = pinB;
}
void Motor::desligar() {
	digitalWrite(this->pinA, LOW);
	digitalWrite(this->pinB, LOW);
}
void Motor::ligar_sentido_horario() {
	digitalWrite(this->pinA, HIGH);
	digitalWrite(this->pinB, LOW);
}
void Motor::ligar_sentido_anti_horario() {
	digitalWrite(this->pinA, LOW);
	digitalWrite(this->pinB, HIGH);
}

#endif