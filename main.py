import time
import serial
import deltaReverseKinematics
import math

#constants defining our delta robot setup
r_b = 100
r_e = 35
l_b = 100
l_f = 150

#desired end effector position
E_x = 0
E_y = 0
E_z = -150 

#calculate distance between two points
def calculateDistance(x0, y0, z0, x1, y1, z1):
    distance = math.sqrt((x0 - x1)**2 + (y0 - y1)**2 + (z0 - z1)**2)
    return distance

#subdivide a parametrized path
#input is a function and the number of steps to subdivide it
#output is an array of pts
def subdividePath(pathEquation, subdivisionSteps, start, end):
    pathPoints = []
    for i in range(start, end, (end - start)/subdivisionSteps):
        pathPoints.append(pathEquation(i))
    return pathPoints




#initialize a serial object
arduinoData = serial.Serial('COM6', 115200)
time.sleep(1) #sleep briefly to allow time for initializing the serial object


#testing deltaReverseKinematics
deltaReverseKinematics.findReverseKinematicAngles(E_x, E_y, E_z)

#create an infinite loop that will house our code for reading serial inputs
while True:
    # sending data through serial connection
    i = input("Desired position: ").strip()
    if i == "currentPosition":
        print(E_x, E_y, E_z)
        arduinoData.write(i.encode())
    elif i.startswith("rot"):
        i = i[4:]
        arduinoData.write(i.encode())
    elif i[0].isdigit():
        i = i.split(" ")
        E_x = float(i[0])
        E_y = float(i[1])
        E_z = float(i[2])
        angles = deltaReverseKinematics.findReverseKinematicAngles(E_x, E_y , E_z)
        msg = f'{angles[0]} {angles[1]} {angles[2]}'
        print("int detected")
        # print(msg)
        arduinoData.write(msg.encode())
    else:
        arduinoData.write(i.encode())
        # print(i)

    # receiving data90
    while(arduinoData.inWaiting() == 0):
        pass
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket, 'utf-8')
    dataPacket = dataPacket.strip('\r\n')

    print(dataPacket)