import time
import astropy
import serial

#create a serial object
arduinoData = serial.Serial('COM6', 115200)
#wait one millisecond for the serial object to finish instantiating
time.sleep(1)

#create an infinite loop where we will put our code to check the serial port
while True:
    command = input("Arduino command: ")
    arduinoData.write(command.encode('utf-8'))

    if command == 'exit':
        exit()
    # #reads when there is no actual data in the serial
    while(arduinoData.inWaiting()==0):
        pass

    #arduino reads the serial line
    dataPacket = arduinoData.readline()
    #convert that byte data to a utf-8 string
    dataPacket = str(dataPacket, 'utf-8')
    #strip off the extra lines from \r\n at end of string
    dataPacket = dataPacket.strip('\r\n')
    #print to terminal
    print(dataPacket)


