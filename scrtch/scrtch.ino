#include <Servo.h>

Servo myServo;


void setup() {
  myServo.attach(8);
  
}

void loop() {
  myServo.write(90);
}
