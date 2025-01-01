// Define motor pins
#define motor1Pin1  2
#define motor1Pin2  3
#define motor2Pin1  4
#define motor2Pin2  5

void setup() {
  // Set motor pins as outputs
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);
  pinMode(motor2Pin1, OUTPUT);
  pinMode(motor2Pin2, OUTPUT);

  // Start serial communication with HC-06 module
  Serial.begin(9600); // Ensure this matches the baud rate of your HC-06 module
}

void loop() {
  // Check if data is available from Bluetooth
  if (Serial.available()) {
    int data = Serial.read();
    Serial.println(data); // Optional: For debugging via the Serial Monitor

    // If data is 1, stop rotating and move forward
    if (data == '1') { // Compare with character '1'
      stopMotors();
      moveForward();
    } else {
      // Rotate continuously
      rotate();
    }
  } else {
    // Rotate continuously
    rotate();
  }
}

void rotate() {
  // Rotate the robot by running motors in opposite directions
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, HIGH);
}

void moveForward() {
  // Move the robot forward by running both motors in the same direction
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, LOW);
}

void stopMotors() {
  // Stop the motors
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);
}
