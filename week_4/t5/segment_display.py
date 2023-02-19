from lib_sensor import SensorLIB

class SegmentDisplay(SensorLIB):
    _SEG_CHAR = {
        "0": 0b11111100,
        "1": 0b01100000,
        "2": 0b11011010,
        "3": 0b11110010,
        "4": 0b01100110,
        "5": 0b10110110,
        "6": 0b10111110,
        "7": 0b11100000,
        "8": 0b11111110,
        "9": 0b11110110
    }

    def __init__(self, pin_out: int, pin_in: int, freq: int) -> None:
        super().__init__(pin_out, pin_in, freq)

    def showOnDisplay(self, symbol: str) -> None:
        if symbol in self._SEG_CHAR:
            self._writeSerial(self._SEG_CHAR[symbol],True)