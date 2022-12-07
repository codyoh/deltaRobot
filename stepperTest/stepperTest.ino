#include <AccelStepper.h>
#include <MultiStepper.h>

//define pin connections
const int directionPin1 = 2;
const int stepPin1 = 3;

const int directionPin2 = 4;
const int stepPin2 = 5;

// define motor interface type
#define motorInterfaceType 1

// create an instance
AccelStepper stepper1(motorInterfaceType, stepPin1, directionPin1);

//create second instance
AccelStepper stepper2(motorInterfaceType, stepPin2, directionPin2);

int convertAngleToSteps(int angle) {
  int steps = angle / 1.8;
  return steps;
}

void setup() {

  //serial port
   Serial.begin(115200);
  
  // set the maximum speed, acceleration factor,
  // initial speed, and the target position
 stepper1.setMaxSpeed(1000);
 stepper1.setSpeed(100);
 stepper1.setAcceleration(50);
//  stepper1.moveTo(200);


}

void loop() {
// stepper1.setSpeed(100);
// stepper1.runSpeed();
//  stepper1.run();
//  delay(500);

 if (Serial.available() > 0) {
   String msg = Serial.readString();
   
   int number = msg.toInt();
   int steps = convertAngleToSteps(number);
   Serial.println(steps);
  // Serial.print("message received");
  // Serial.println(msg);

  // if (number == 0) {
  //   stepper1.setSpeed(0);
  // }

  // else {
   stepper1.moveTo(steps);
  //  stepper1.run();
  // }

 }
    // // Move the motor one step
//    stepper1.moveTo(steps);
   stepper1.run();
  

}
