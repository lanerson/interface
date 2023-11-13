from Arduino import Arduino
import pyvisa
import numpy as np
import time

class PowerSupply():
    def __init__(self): # curr_lim, volt_lim talvez voltem mas por enquanto não
        self.rm = pyvisa.ResourceManager()
        self.power_supply = self.rm.open_resource("USB0::0x0957::0xCD18::MY51144612::0::INSTR")
        self.power_supply.write_termination = "\n"
        self.power_supply.read_termination = "\n"
        self.power_supply.write("*RST")
        # self.power_supply.write(f"CURR:LIM {curr_lim}")
        # self.power_supply.write(f"VOLT:LIM {volt_lim}")

    def powerSupplyOpen(self, curr, volt):
        self.power_supply.write(f"SOUR:CURR {curr}")
        self.power_supply.write(f"SOUR:VOLT {volt}")
        self.power_supply.write("OUTP ON")

    def powerSupplyClose(self):
        self.power_supply.write("OUTP OFF")
        self.power_supply.close()

class Multimeter():
    def __init__(self, serial = Arduino) -> None:
        self.rm = pyvisa.ResourceManager("C:/Windows/System32/visa64.dll")
        self.multimeter = self.rm.open_resource("GPIB0::22::INSTR")
        self.multimeter.read_termination = "\n"
        self.multimeter.write_termination = "\n"
        self.multimeter.query_delay = 0.1
        self.ser = serial

    def readValues(self, file, type):
        sensor = 3
        collum = 3
        movements = 2
        measures = np.zeros((collum, movements * sensor))
        self.ser.serialOpen()
        self.multimeter.write("*RST")
        for i in range(movements):
            # self.multimeter.write("*RST")
            # self.multimeter.write("TRIG:SOUR BUS") 
            # self.multimeter.write("INIT")
            # self.multimeter.write(f"TRIG:COUN {collum * sensor}")       
            # for j in range(collum * sensor):                
            #     self.ser.serialWrite(b"M")    
                            
            #     if self.ser.serialRead() == "F":
            #         self.multimeter.write("*TRG")
                    
            # response = self.multimeter.query("FETC?")
            # response = response[:-2]            
            self.multimeter.write("*RST")
            for i in range(movements):
                response = []
                for j in range(collum * sensor):
                    self.ser.serialWrite(b"M")
                    if self.ser.serialRead() == "F":
                        med = self.multimeter.query("MEAS?")
                        response.append(abs(float(med)))

                readings = np.array(response, dtype = np.float64).reshape((collum, sensor))    
                measures[:, i::movements] = readings
                while self.ser.serialRead() != "N":
                    continue
                print('arrocha menino')

        measures.tofile(f"{file}.{type}", sep = ",")
        
    def multimeterClose(self):
        self.multimeter.close()
        self.ser.serialClose()