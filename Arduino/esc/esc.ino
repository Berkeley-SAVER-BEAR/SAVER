#include <Servo.h>

byte servoPin = 9;
Servo servo;

void setup() {
  // Initialize Serial communication to see printed values
  Serial.begin(9600);

  servo.attach(servoPin);

  servo.writeMicroseconds(1500); // send "stop" signal to ESC (Electronic Speed Controller).

  delay(7000); // delay to allow the ESC to recognize the stopped signal
}

void loop() {
  // test ESC
  // Set signal value, which should be between 1100 (max reverse) and 1900 (max forward)
  int signal = 1100;
  for (int i = signal; i <= 1900; i+= 100) {
    Serial.println("PWM Value" + signal)
    
    // Send signal to ESC.
    servo.writeMicroseconds(signal);
    
    // delay for 10 seconds to test
    delay(10000);
  }
}
