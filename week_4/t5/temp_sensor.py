from sensor import Sensor
from lib_sensor import SensorLIB


class TempSensor(Sensor):
    __unit: str = 'C'
    R_MIN: int = -50
    R_MAX: int = 50

    def __init__(self, id: str, location: str) -> None:
        super().__init__(id, location)

    def readRaw(self) -> int:
        sensor_lib = SensorLIB(10, 20)
        raw_value = sensor_lib.readAnalog()
        converted_value = self.convertToRange(self.R_MIN, self.R_MAX, raw_value)
        return converted_value

    def displayTemp(self):
        raw_value = self.readRaw(); 
        print(f"Temperature: {raw_value:.2f} {self.__unit}")