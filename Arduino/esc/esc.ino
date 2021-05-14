#include <Servo.h>
byte servoPin = 9;
byte servoPin1 = 5;
Servo servo;
Servo servo1;

void setup() {
  // Initialize Serial communication to see printed values
  Serial.begin(9600);

  servo.attach(servoPin);
  servo1.attach(servoPin1);

  servo.writeMicroseconds(1500); // send "stop" signal to ESC (Electronic Speed Controller).
  servo1.writeMicroseconds(1500);

  delay(7000); // delay to allow the ESC to recognize the stopped signal
}


void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int servoVal = data[0] - 48;

    int pwmVal = 0;
    for (int i = 1; i < data.length(); i++) {
      if (data[i] == '.') {
        break;
      }
      pwmVal = pwmVal * 10 + (data.charAt(i) - 48); 
    }
    
    if (servoVal == 0) {
      servo.writeMicroseconds(pwmVal);
    } else {
      servo1.writeMicroseconds(pwmVal);
    }
   
    Serial.println("Port: " + String(servoVal) + " PWM: " + String(pwmVal));
    Serial.println(" ");

    // delay for 3 seconds to test
    //delay(3000);
    
  }
}
