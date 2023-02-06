#include <AccelStepper.h>
#include <MultiStepper.h>

//define pin connections
const int directionPin1 = 2;
const int stepPin1 = 3;

const int directionPin2 = 4;
const int stepPin2 = 5;

const int directionPin3 = 6;
const int stepPin3 = 7;

// define motor interface type
#define motorInterfaceType 1

// create an instance
AccelStepper stepper1(motorInterfaceType, stepPin1, directionPin1);

//create second instance
AccelStepper stepper2(motorInterfaceType, stepPin2, directionPin2);

AccelStepper stepper3(motorInterfaceType, stepPin3, directionPin3);

int convertAngleToSteps(int angle) {
  int gearRatioedAngle = angle * 5/2;
  int steps = gearRatioedAngle / 1.8;
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

 stepper2.setMaxSpeed(1000);
 stepper2.setSpeed(100);
 stepper2.setAcceleration(50);

 stepper3.setMaxSpeed(1000);
 stepper3.setSpeed(100);
 stepper3.setAcceleration(50);

}

void loop() {
 if (Serial.available() > 0) {
   String msg = Serial.readString();
   
   if(msg == "stop"){
     stepper1.setSpeed(0);
     stepper2.setSpeed(0);
     stepper3.setSpeed(0);
   }
   else if (msg == "currentPosition"){
     Serial.print(String(stepper1.currentPosition()));
     Serial.print(' ');
      Serial.print(String(stepper2.currentPosition()));
      Serial.print(' ');
      Serial.println(String(stepper2.currentPosition()));
   }

   else if (msg == "zero1"){
     stepper1.setCurrentPosition(0);
     Serial.println("stepper1 position set to 0");
   }
   else if (msg == "zero2"){
      stepper2.setCurrentPosition(0);
     Serial.println("stepper2 position set to 0");
   }

    else if (msg == "zero3"){
     stepper3.setCurrentPosition(0);
     Serial.println("stepper3 position set to 0");
  }

   else {
     int rotationAngles[3];
     int StringCount = 0;

     while (msg.length() > 0) {
       int index = msg.indexOf(' ');
       if (index == -1) {  // no space found
        rotationAngles[StringCount++] = msg.toInt();
        break;
       }
       else {
         rotationAngles[StringCount++] = msg.substring(0, index).toInt();
         msg = msg.substring(index + 1);
       }
     }


      // int number = msg.toInt();
      // int steps = convertAngleToSteps(number);
      // Serial.print("stepper1 to ");
      Serial.println();
      stepper1.setSpeed(100);
      stepper1.moveTo(convertAngleToSteps(rotationAngles[0]));
      stepper2.setSpeed(100);
      stepper2.moveTo(convertAngleToSteps(rotationAngles[1]));
      stepper3.setSpeed(100);
      stepper3.moveTo(convertAngleToSteps(rotationAngles[2]));
   }
  }

  stepper1.run();
  stepper2.run();
  stepper3.run();

}
