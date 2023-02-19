from lib_sensor import SensorLIB
from abc import abstractmethod, ABC

class Sensor(ABC):
    @property
    def id(self) -> str:
        return self.__id

    @property
    def location(self) -> str:
        return self.__location

    @abstractmethod
    def readRaw(self) -> int:
        pass
    @abstractmethod
    def __init__(self, id: str, location: str) -> None:
        self.__id = id
        self.__location = location
        # self.__input_pin = input_pin
        # self.__output_pin = output_pin

    def printLocation(self) -> None:
        print("Location: " + self.__location)

    def convertToRange(self, minimum: int, maximum: int, raw_value: int) -> float:
        zero_to_one = float(raw_value) / 65535
        wanted_range = float(abs(maximum - minimum))
        converted_value = zero_to_one * wanted_range + minimum
        return converted_value