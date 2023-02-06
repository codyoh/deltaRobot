import time
import serial
import deltaReverseKinematics

#constants defining our delta robot setup
r_b = 100
r_e = 35
l_b = 100
l_f = 150

#desired end effector position
E_x = 0
E_y = 0
E_z = -150 



#initialize a serial object
# arduinoData = serial.Serial('COM6', 115200)
time.sleep(1) #sleep briefly to allow time for initializing the serial object


#testing deltaReverseKinematics
deltaReverseKinematics.findReverseKinematicAngles(E_x, E_y, E_z)

#create an infinite loop that will house our code for reading serial inputs
# while True:
#     # sending data through serial connection
#     i = input("Desired position: ").strip()
#     arduinoData.write(i.encode())


#     #receiving data90
#     while(arduinoData.inWaiting() == 0):
#         pass
#     dataPacket = arduinoData.readline()
#     dataPacket = str(dataPacket, 'utf-8')
#     dataPacket = dataPacket.strip('\r\n')

#     print(dataPacket)