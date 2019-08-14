// Arduino code to control the wheelchair 
//#include <SoftwareSerial.h>
//SoftwareSerial Bluetooth(3,2);  // RX | TX

const int leftForward = 8;
const int leftBackward = 9;
const int rightForward = 10;
const int rightBackward = 11;


void setup() {
  pinMode(leftForward , OUTPUT);
  pinMode(leftBackward , OUTPUT);
  pinMode(rightForward , OUTPUT);
  pinMode(rightBackward , OUTPUT);
  pinMode(12, OUTPUT);
  Serial.begin(9600);
  //Bluetooth.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(12, HIGH);
  while (Serial.available())
  {

    char ch = Serial.read();

    if (ch == 'a')  //back
    {
      //Serial.println("hello world");
      digitalWrite(leftForward, LOW); //turn left
      digitalWrite(leftBackward, HIGH);
      digitalWrite(rightForward, HIGH);
      digitalWrite(rightBackward, LOW);

    }
    else if (ch == 'l') //left
    {
      digitalWrite(leftForward, LOW);
      digitalWrite(leftBackward, HIGH);
      digitalWrite(rightForward, LOW);
      digitalWrite(rightBackward, HIGH);

      delay(520);

      digitalWrite(leftForward, HIGH);
      digitalWrite(leftBackward, LOW);
      digitalWrite(rightForward, LOW);
      digitalWrite(rightBackward, HIGH);

    }
    else if (ch == 'r') //right
    {
      digitalWrite(leftForward, HIGH);
      digitalWrite(leftBackward, LOW);
      digitalWrite(rightForward, HIGH);
      digitalWrite(rightBackward, LOW);

      delay(520);

      digitalWrite(leftForward, HIGH);
      digitalWrite(leftBackward, LOW);
      digitalWrite(rightForward, LOW);
      digitalWrite(rightBackward, HIGH);
    }
    else if (ch == 'f') //front
    {
      digitalWrite(leftForward, HIGH);
      digitalWrite(leftBackward, LOW);
      digitalWrite(rightForward, LOW);
      digitalWrite(rightBackward, HIGH);
    }
    else if (ch == 's' || ch == 'S')
    {
      digitalWrite(leftForward, LOW);
      digitalWrite(leftBackward, LOW);
      digitalWrite(rightForward, LOW);
      digitalWrite(rightBackward, LOW);
    }
  }
}
