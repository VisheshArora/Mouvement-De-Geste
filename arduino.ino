int rm1 = 5;    // pin the LED is connected to
int rm = 6;
int lm1 = 7;
int lm = 8;
int enbA = A0;
int enbB = A1;
int trigPinl = 9;
int echoPinl = 10;
int trigPinr = 32;
int echoPinr = 34;
int redl = 11;
int greenl = 12;
int redr = 46;
int greenr = 50;
char c = '1';  
long durationL, durationR;
int distanceL, distanceR;

void setup()
{
  Serial.begin(115200); // Initialize serial port to send and receive at 9600 baud
  pinMode(rm, OUTPUT);
  pinMode(rm1, OUTPUT);
  pinMode(lm, OUTPUT);
  pinMode(lm1, OUTPUT);
  pinMode(enbA, OUTPUT);
  pinMode(enbB, OUTPUT);
  pinMode(trigPinl, OUTPUT);
  pinMode(echoPinl, INPUT);
  pinMode(trigPinr, OUTPUT);
  pinMode(echoPinr, INPUT);
  pinMode(redl, OUTPUT);
  pinMode(greenl, OUTPUT);
  pinMode(redr, OUTPUT);
  pinMode(greenr, OUTPUT);
}

void loop()
{
  if ( Serial.available()) // Check to see if at least one character is available
  {
   c = Serial.read();
   //Serial.println(c);
   
   analogWrite(enbA, 150);
   analogWrite(enbB, 150);

   digitalWrite(trigPinl, LOW);
   delayMicroseconds(2);

   digitalWrite(trigPinl, HIGH);
   delayMicroseconds(10);
   digitalWrite(trigPinl, LOW);

   durationL = pulseIn(echoPinl, HIGH);
   distanceL = durationL*0.034/2;
   Serial.println(distanceL);

   digitalWrite(trigPinr, LOW);
   delayMicroseconds(2);

   digitalWrite(trigPinr, HIGH);
   delayMicroseconds(10);
   digitalWrite(trigPinr, LOW);

   durationR = pulseIn(echoPinr, HIGH);
   distanceR = durationR*0.034/2;
   Serial.println(distanceR);
   if(distanceL<=15 && distanceR<=15){
      digitalWrite(redl, HIGH);
      digitalWrite(redr, HIGH);
      delay(80);
      digitalWrite(redl, LOW);
      digitalWrite(redr, LOW);
    }
   else if(distanceL<=15 && distanceR>15){
      digitalWrite(redl, HIGH);
      digitalWrite(greenr, HIGH);
      delay(80);
      digitalWrite(greenr, LOW);
      digitalWrite(redl, LOW);
    }


   else if(distanceR<=15 && distanceL>15){
      digitalWrite(redr, HIGH);
      digitalWrite(greenl, HIGH);
      delay(80);
      digitalWrite(greenl, LOW);
      digitalWrite(redr, LOW);
    }
   else{
      digitalWrite(greenl, HIGH);
      digitalWrite(greenr, HIGH);
      delay(80);
      digitalWrite(greenr, LOW);
      digitalWrite(greenl, LOW);
    }
    
   
   switch (c) {
      case '0':
        
        digitalWrite(lm, HIGH);
        digitalWrite(lm1, LOW);
        digitalWrite(rm, HIGH);
        digitalWrite(rm1, LOW);
        delay(80);
        break;
      case '1':
        
        digitalWrite(lm, LOW);
        digitalWrite(lm1, LOW);
        digitalWrite(rm, LOW);
        digitalWrite(rm1, LOW);
        delay(80);
        break;
      case '2':
        
        digitalWrite(lm1, HIGH);
        digitalWrite(lm, LOW);
        digitalWrite(rm, HIGH);
        digitalWrite(rm1, LOW);
        delay(80);
        break;
      case '3':
        
        digitalWrite(lm, HIGH);
        digitalWrite(lm1, LOW);
        digitalWrite(rm1, HIGH);
        digitalWrite(rm, LOW);
        delay(80);
        break;
      default:
        
        digitalWrite(lm, LOW);
        digitalWrite(lm1, LOW);
        digitalWrite(rm, LOW);
        digitalWrite(rm1, LOW);
        delay(80);
        break;
      }
  }
}
