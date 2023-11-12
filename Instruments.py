from Arduino import Arduino
import time
import pyvisa
import numpy as np
print('oi')
class PowerSupply():
    def __init__(self): # curr_lim, volt_lim talvez voltem mas por enquanto não
        self.rm = pyvisa.ResourceManager("C:\\Windows\\System32\\visa64.dll")
        self.power_supply = self.rm.open_resource("USB0::0x0957::0xCD18::MY51144612::0::INSTR")
        self.power_supply.write("*RST")
        # self.power_supply.write(f"CURR:LIM {curr_lim}")
        # self.power_supply.write(f"VOLT:LIM {volt_lim}")
        pass

    def powerSupplyOpen(self, curr, volt):
        self.power_supply.write(f"CURR {curr}")
        self.power_supply.write(f"VOLT {volt}")
        self.power_supply.write("OUTP ON")
        pass

    def powerSupplyClose(self):
        self.power_supply.write("OUTP OFF")
        self.power_supply.close()
        pass

class Multimeter():
    def __init__(self, serial = Arduino) -> None:
        self.rm = pyvisa.ResourceManager("C:\\Windows\\System32\\visa64.dll")
        self.multimeter = self.rm.open_resource("USB0::0x0957::0xCD18::MY51144612::0::INSTR")
        self.multimeter.read_termination = "\n"
        self.multimeter.write_termination = "\n"
        self.multimeter.query_delay = 0.1
        self.ser = serial

    def readValues(self, file, type):
        sensor = 3
        collum = 3
        movements = 3
        measures = np.zeros((collum, movements * sensor))
        self.ser.serialOpen()
        self.multimeter.write("*RST")
        for i in range(movements):
            self.multimeter.write("*RST")
            self.multimeter.write("TRIG:SOUR BUS") 
            self.multimeter.write("INIT")
            self.multimeter.write(f"TRIG:COUN {collum * sensor}") 
            # teste           
            for j in range(sensor):                
                self.ser.serialWrite(b"M")    
                            
                if self.ser.serialRead() == "F":
                    self.multimeter.write("*TRG")
                    
            response = self.multimeter.query("FETC?")
            response = response[:-2]
            print(response)            
            readings = np.array([float(read) for read in response.split(",")], dtype = np.float64).reshape((collum, sensor))
            measures[:, i::movements] = readings
        
        measures.tofile(f"{file}.{type}", sep = ",")
        

    def multimeterClose(self):
        self.multimeter.close()
        self.ser.serialClose()