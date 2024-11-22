#include <AccelStepper.h>
 
#define dirPin 2
#define stepPin 3
#define motorInterfaceType 1
//Program assumes 16 microstepping
 
// Create a new instance of the AccelStepper class:
AccelStepper stepper = AccelStepper(motorInterfaceType, stepPin, dirPin);


const int led1 = 6;
const int led2 = 5;
const int led3 = 4;
const int motled = 8;
const int motsw = 7;

 
void setup() 
{
  // Set the maximum speed and acceleration:
  stepper.setMaxSpeed(2000); //
  stepper.setAcceleration(200); //

  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(motled, OUTPUT);
  pinMode(motsw, INPUT_PULLUP);
}
 
void loop() {
  int motorenable = digitalRead(motsw);
  if(motorenable==HIGH){
    digitalWrite(motled, HIGH);
    // Set the target position:
    digitalWrite(led1, HIGH);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
    stepper.moveTo(26000);
    // Run to target position with set speed and acceleration/deceleration:
    stepper.runToPosition();
    
    //finished so rest
    digitalWrite(led1, LOW);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, LOW);
    delay(4000);
    
    // Move back to zero:
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, HIGH);
    stepper.moveTo(0);
    stepper.runToPosition();
    
    //finished so rest
    digitalWrite(led1, LOW);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, LOW);
    delay(4000);
  }else{
    digitalWrite(motled, LOW);
  }
};
