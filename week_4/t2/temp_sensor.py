from sensor import Sensor

class TempSensor(Sensor):
    __unit = 'C'
    R_MIN = -50
    R_MAX = 50
    
    def __init__(self, id, location):
        super().__init__(id, location)
        
    def displayTemp(self):
        raw_value = self.printReading(); 
        converted_temp = self.convertToRange(self.R_MIN, self.R_MAX, raw_value)
        print(f"Temperature: {converted_temp:.2f} {self.__unit}")
    
    def convertToRange(self, minimum: int, maximum: int, raw_value: int) -> float:
        zero_to_one = float(raw_value) / 65535
        wanted_range = float(abs(maximum - minimum))
        converted_value = zero_to_one * wanted_range + minimum
        return converted_value