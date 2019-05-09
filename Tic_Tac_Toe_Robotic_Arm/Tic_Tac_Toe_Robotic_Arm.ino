#include <Servo.h>

char receivedChar;
boolean newData = false;


Servo base;
Servo arm1;
Servo arm2;
Servo arm3;
Servo claw;

int clawClose = 6;
int clawOpen = 80;

int shortDelay = 500;
int longDelay = 1500;

void setup() {
  Serial.begin(9600);
  //Serial.flush();
  base.attach(9);
  arm1.attach(10);
  arm2.attach(11);
  arm3.attach(6);
  claw.attach(5);


  StartPosition();

} 

void StartPosition() {
 
  arm3.write(90);
  
  arm2.write(30);
  
  arm1.write(150);
  
   delay(shortDelay);
  claw.write(clawClose);
  
  delay(shortDelay);
    base.write(90);
  
}


void SquareOne() {
  base.write(125);
  delay(shortDelay);
  
  arm3.write(110);
  delay(shortDelay);
  
  arm2.write(50);
  delay(shortDelay);
  
  arm1.write(50);
  delay(longDelay);
  
  claw.write(clawOpen);
  delay(shortDelay);
}

void SquareTwo() {
  base.write(115);
  delay(shortDelay);
  
  arm3.write(100);
  delay(shortDelay);
  
  arm2.write(80);
  delay(shortDelay);
  
  arm1.write(35);
  delay(longDelay);
  
  claw.write(clawOpen);
  delay(shortDelay);
}

void SquareThree() {
  base.write(110);
  delay(shortDelay);
  
  arm3.write(150);
  delay(shortDelay);
  
  arm2.write(165);
  delay(shortDelay);
  
  arm1.write(0);
  delay(longDelay);
  
  claw.write(clawOpen);
  delay(shortDelay);
}

void SquareFour() {
  base.write(95);
  delay(shortDelay);
  
  arm3.write(130);
  delay(shortDelay);
  
  arm2.write(45);
  delay(shortDelay);
  
  arm1.write(50);
  delay(longDelay);
  
  claw.write(clawOpen);
  delay(shortDelay);
}

void SquareFive() {
  base.write(95);
  delay(shortDelay);
  
  arm3.write(100);
  delay(shortDelay);
  
  arm2.write(70);
  delay(shortDelay);
  
  arm1.write(40);
  delay(longDelay);
  
  claw.write(clawOpen);
  delay(shortDelay);
}

void SquareSix() {
  base.write(90);
  delay(shortDelay);
  
  arm3.write(150);
  delay(shortDelay);
  
  arm2.write(165);
  delay(shortDelay);
  
  arm1.write(0);
  delay(longDelay);
  
  claw.write(clawOpen);
  delay(shortDelay);
}

void SquareSeven() {
  base.write(60);
  delay(shortDelay);
  
  arm3.write(130);
  delay(shortDelay);
  
  arm2.write(45);
  delay(shortDelay);
  
  arm1.write(50);
  delay(longDelay);
  
  claw.write(clawOpen);
  delay(shortDelay);
}

void SquareEight() {
  base.write(70);
  delay(shortDelay);
  
  arm3.write(100);
  delay(shortDelay);
  
  arm2.write(70);
  delay(shortDelay);
  
  arm1.write(40);
  delay(longDelay);
  
  claw.write(clawOpen);
  delay(shortDelay);
}

void SquareNine() {
  base.write(75);
  delay(shortDelay);
  
  arm3.write(150);
  delay(shortDelay);
  
  arm2.write(165);
  delay(shortDelay);
  
  arm1.write(0);
  delay(longDelay);
  
  claw.write(clawOpen);
  delay(shortDelay);
}

void SquarePickup() {
  claw.write(clawOpen);
  delay(shortDelay);
  
  base.write(0);
  delay(shortDelay);
  
  arm3.write(120);
  delay(shortDelay);
  
  arm2.write(45);
  delay(shortDelay);
  
  arm1.write(50);
  delay(longDelay);
  
  claw.write(clawClose);
  delay(shortDelay);
}

void recvInfo() {
  if(Serial.available()>0){
    receivedChar = Serial.parseInt();
    Serial.print("received a char.... bitch");
  
  if (receivedChar == 1) {
      Serial.print("Placing in Tile 1");
      StartPosition();
      delay(longDelay);
      SquarePickup();
      delay(shortDelay);
      StartPosition();
      delay(shortDelay);
      SquareOne();
      delay(shortDelay);
      StartPosition();
    }
  
    if (receivedChar == 2) {
      Serial.print("Placing in Tile 2");
      StartPosition();
      SquarePickup();
      StartPosition();
      SquareTwo();
      StartPosition();
    }
      
    if (receivedChar == 3) {
      Serial.print("Placing in Tile 3");
      StartPosition();
      SquarePickup();
      StartPosition();
      SquareThree();
      StartPosition();
   
    }
  
    if (receivedChar == 4) {
      Serial.print("Placing in Tile 4");
      StartPosition();
      SquarePickup();
      StartPosition();
      SquareFour();
      StartPosition();
    }
  
    if (receivedChar == 5) {
      Serial.print("Placing in Tile 5");
      StartPosition();
      SquarePickup();
      StartPosition();
      SquareFive();
      StartPosition();
    }
    
  
    if (receivedChar == 6) {
      Serial.print("Placing in Tile 6");
      StartPosition();
      SquarePickup();
      StartPosition();
      SquareSix();
      StartPosition();
    }
  
    if (receivedChar == 7) {
      Serial.print("Placing in Tile 7");
      StartPosition();
      SquarePickup();
      StartPosition();
      SquareSeven();
      StartPosition();
    }
    
  
    if (receivedChar == 8) {
      Serial.print("Placing in Tile 8");
      StartPosition();
      SquarePickup();
      StartPosition();
      SquareEight();
      StartPosition();
    }
  
    if (receivedChar == 9) {
      Serial.print("Placing in Tile 9");
      StartPosition();
      SquarePickup();
      StartPosition();
      SquareNine();
      StartPosition();
    }
    
  }
}

void loop() {
 
  recvInfo();
  
  /*
  delay(1500);
  myservo.write(clawOpen);
  delay(1500);
  myservo.write(clawClose);
  */
 
  
}
