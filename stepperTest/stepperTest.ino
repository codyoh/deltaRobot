#include <AccelStepper.h>
#include <MultiStepper.h>

//define pin connections
const int directionPin1 = 4;
const int stepPin1 = 5;

const int directionPin2 = 2;
const int stepPin2 = 3;

// define motor interface type
#define motorInterfaceType 1

// create an instance
AccelStepper stepper1(motorInterfaceType, stepPin1, directionPin1);

//create second instance
AccelStepper stepper2(motorInterfaceType, stepPin2, directionPin2);

void setup() {
  // set the maximum speed, acceleration factor,
  // initial speed, and the target position
  stepper1.setMaxSpeed(1000);
  stepper1.setSpeed(100);
  stepper1.setAcceleration(50);
  stepper1.moveTo(200);
  
  stepper2.setMaxSpeed(1000);
  stepper2.setSpeed(100);
  stepper2.setAcceleration(50);
  stepper2.moveTo(200);

}

void loop() {

  // // Move the motor one step
  stepper1.run();
  stepper2.run();


}
