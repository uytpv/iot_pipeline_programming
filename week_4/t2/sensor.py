from lib_sensor import SensorLIB


class Sensor:
    __id: str
    __location: str

    def __init__(self, id: str, location: str) -> None:
        self.__id = id
        self.__location = location

    def getId(self) -> str:
        return self.__id

    def printLocation(self) -> None:
        print("Location: " + self.__location)

    def printReading(self) -> int:
        sensor_lib = SensorLIB(10, 10)
        # sensor_lib = SensorLIB(self.input_pin, self.output_pin)
        raw_value = sensor_lib.readAnalog()
        return raw_value