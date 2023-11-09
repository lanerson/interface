from Serial import Serial
import time
import pyvisa
import numpy as np

class PowerSupply():
    def __init__(self, curr_lim, volt_lim):
        self.rm = pyvisa.ResourceManager("C:\\Windows\\System32\\visa64.dll")
        self.power_supply = self.rm.open_resource("USB0::0x0957::0xCD18::MY51144612::0::INSTR")
        self.power_supply.write("*RST")
        self.power_supply.write(f"CURR:LIM {curr_lim}")
        self.power_supply.write(f"VOLT:LIM {volt_lim}")

    def powerSupplyOpen(self, curr, volt):
        self.power_supply.write(f"CURR {curr}")
        self.power_supply.write(f"VOLT {volt}")
        self.power_supply.write("OUTP ON")

    def powerSupplyClose(self):
        self.power_supply.write("OUTP OFF")
        self.power_supply.close()

class Multimeter():
    def __init__(self, serial = Serial) -> None:
        self.rm = pyvisa.ResourceManager("C:\\Windows\\System32\\visa64.dll")
        self.multimeter = self.rm.open_resource("USB0::0x0957::0xCD18::MY51144612::0::INSTR")
        self.ser = serial

    def readValues(self) -> np.array:
        measures = np.zeros((5, 99))
        self.ser.serialOpen()
        self.multimeter.write("*RST")
        self.multimeter.write("INIT")
        self.multimeter.write("TRIG:COUN ")
        for i in range(33):
            self.multimeter.write("*RST")
            self.multimeter.write("INIT")
            self.multimeter.write("TRIG:COUN 15")
            self.multimeter.write("TRIG:SOUR BUS")
            for j in range(15):
                self.ser.serialWrite("a")
                time.sleep(90)
                if self.ser.serialRead() == "p":
                    self.multimeter.write("*TRG")
            
            response = self.multimeter.query("FETC?")
            readings = np.array([float(read) for read in response.split(", ")], dtype = np.float128).reshape((5, 3))
            measures[:, i::33] = readings

        measures.tofile("dados.csv", sep = ",")

    def multimeterClose(self) -> None:
        self.multimeter.close()
        self.ser.serialClose()