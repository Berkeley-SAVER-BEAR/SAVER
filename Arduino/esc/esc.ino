#include <Servo.h>

// For ESC
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
  // int signal = 1100;
  // for (int i = signal; i <= 1900; i+= 100) {
  //   Serial.println("PWM Value" + signal)
    
  //   // Send signal to ESC.
  //   servo.writeMicroseconds(i);
    
  //   // delay for 10 seconds to test
  //   delay(10000);
  // }

  // Read data from Pi
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.print("Pi to arduino: ");
    Serial.println(data);
    
    // Handle message from Pi
    parseMessage(data);
  }
}

void parseMessage(String data) {
  if data.starts("ESC") {
    int index = data.indexOf("PWM");
    // Extract PWM value from message
    int PWM = data.substring(index + 5).toInt()
    // Send PWM to ESC
    Serial.print("PWM: ")
    Serial.println(PWM)
    servo.writeMicroseconds(PWM)
  }
}
