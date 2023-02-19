from sensor import Sensor
from temp_sensor import TempSensor
from hum_sensor import HumSensor

class MultiSensor(Sensor):
    def __init__(self, id, location):
        super().__init__(id, location)
        self.t_sensor = TempSensor(id, location)
        self.h_sensor = HumSensor(id, location)

    def printReading(self):
        temp_value = self.t_sensor.readRaw()
        hum_value = self.h_sensor.readRaw()
        print(f"Measurements - Temp: {temp_value:.2f} C, Hum: {round(hum_value, 1)} %")

    def readRaw(self) -> int:
        return super().readRaw()
