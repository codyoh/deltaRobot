import time
import serial

#initialize a serial object
arduinoData = serial.Serial('COM6', 115200)
time.sleep(1) #sleep briefly to allow time for initializing the serial object

#create an infinite loop that will house our code for reading serial inputs
while True:
    # sending data through serial connection
    i = input("Turn to X degrees: ").strip()
    arduinoData.write(i.encode())


    #receiving data90
    while(arduinoData.inWaiting() == 0):
        pass
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket, 'utf-8')
    dataPacket = dataPacket.strip('\r\n')

    print(dataPacket)