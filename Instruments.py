from Arduino import Arduino
import time
import pyvisa
import numpy as np

class PowerSupply():
    def __init__(self): # curr_lim, volt_lim talvez voltem mas por enquanto não
        # self.rm = pyvisa.ResourceManager("C:\\Windows\\System32\\visa64.dll")
        # self.power_supply = self.rm.open_resource("USB0::0x0957::0xCD18::MY51144612::0::INSTR")
        # self.power_supply.write("*RST")
        # self.power_supply.write(f"CURR:LIM {curr_lim}")
        # self.power_supply.write(f"VOLT:LIM {volt_lim}")
        pass

    def powerSupplyOpen(self, curr, volt):
        # self.power_supply.write(f"CURR {curr}")
        # self.power_supply.write(f"VOLT {volt}")
        # self.power_supply.write("OUTP ON")
        pass

    def powerSupplyClose(self):
        # self.power_supply.write("OUTP OFF")
        # self.power_supply.close()
        pass

class Multimeter():
    def __init__(self, serial = Arduino) -> None:
        # self.rm = pyvisa.ResourceManager("C:\\Windows\\System32\\visa64.dll")
        # self.multimeter = self.rm.open_resource("USB0::0x0957::0xCD18::MY51144612::0::INSTR")
        self.ser = serial

    def readValues(self, file, type):
        sensor = 9
        collum = 3
        movements = sensor*2
        # measures = np.zeros((collum, movements))
        self.ser.serialOpen()
        # self.multimeter.write("*RST")
        # self.multimeter.write("INIT")
        # self.multimeter.write("TRIG:COUN ")
        for i in range(movements):
            # self.multimeter.write("*RST")
            # self.multimeter.write("INIT")
            # self.multimeter.write(f"TRIG:COUN {sensor}")
            # self.multimeter.write("TRIG:SOUR BUS")
            for j in range(1, sensor+1):
                self.ser.serialWrite("M" * j)
                time.sleep(5)
                if self.ser.serialRead() == "F":
                    # self.multimeter.write("*TRG")
                    pass
            # response = self.multimeter.query("FETC?")
            # readings = np.array([float(read) for read in response.split(", ")], dtype = np.float128).reshape((collum, 3))
            # measures[:, i::2] = readings

        # measures.tofile(f"{file}.{type}", sep = ",")

    # def multimeterClose(self):
    #     self.multimeter.close()
    #     self.ser.serialClose()