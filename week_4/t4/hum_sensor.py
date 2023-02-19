from sensor import Sensor
from lib_sensor import SensorLIB


class HumSensor(Sensor):
    __unit: str = '%'
    R_MIN: int = 0
    R_MAX: int = 100

    def __init__(self, id: str, location: str) -> None:
        super().__init__(id, location)

    def readRaw(self) -> int:
        sensor_lib = SensorLIB(30, 60)
        raw_value = sensor_lib.readAnalog()
        converted_value = self.convertToRange(self.R_MIN, self.R_MAX, raw_value)
        return converted_value

    def displayHum(self) -> None:
        hum = round(self.readRaw(), 1)
        print(f"Humidity: {hum} {self.__unit}")