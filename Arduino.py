import serial
import serial.tools.list_ports
import time


def findArduino():
    def getPorts():
        ports = serial.tools.list_ports.comports()
        return ports
    portsFound = getPorts()
    commPort = "None"

    numConnnection = len(portsFound)

    for i in range(numConnnection):
        port = portsFound[i]
        strPort = str(port)

        if "Arduino" in strPort:
            splitPort = strPort.split(" ")
            commPort = splitPort[0]

    return commPort

class Arduino():
    def __init__(self, port, baudrate = 9600, size = 1, timeout = None):
        self.ser = serial.Serial(port = port, baudrate = baudrate, timeout = timeout)
        self.size = size
        time.sleep(0.1)
    
    def serialOpen(self):
        self.ser.open()

    def serialRead(self):
        if self.ser.in_waiting == self.size:
            readValue = self.ser.read(size = self.size)
            self.ser.reset_input_buffer()
            return str(readValue)
    
    def serialWrite(self, message):
        self.ser.reset_output_buffer()
        self.ser.write(message)

    def serialClose(self):
        self.ser.close()