import serial
import serial.tools.list_ports
import time


def findArduino():
    vid = 0x2341
    pid = 0x0043
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if port.vid == vid and port.pid == pid:
            return port.device
    return None

class Arduino():
    def __init__(self, port, baudrate = 9600, size = 1, timeout = None):
        self.ser = serial.Serial(port = port, baudrate = baudrate, timeout = timeout)
        self.size = size
        time.sleep(0.1)
    
    def serialOpen(self):
        try:
            self.ser.open()
        except Exception as e:
            print('já tava aberta')

    def serialRead(self):
        time.sleep(2)
        if self.ser.in_waiting == self.size:
            readValue = self.ser.read(size = self.size)
            self.ser.reset_input_buffer()
            print(str(readValue)[2])
            return str(readValue)[2]
    
    def serialWrite(self, message):
        self.ser.reset_output_buffer()
        self.ser.write(message)

    def serialClose(self):
        self.ser.close()
        
# porta = findArduino()
# arduino = Arduino(porta)
# c = 20
# while True:
#     r = str(input('continua? '))    
#     arduino.serialWrite(b"M")        
#     time.sleep(2)
#     print(arduino.serialRead())
#     c+=1
#     if( c == 10):
#         arduino.serialClose()
#         break