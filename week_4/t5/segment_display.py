from lib_sensor import SensorLIB

class SegmentDisplay(SensorLIB):
    def __init__(self, pin_out=-1, pin_in=-1, freq=-1):
        super().__init__(pin_out, pin_in, freq)

    def __segment(self, value):
        """
        This method returns a binary representation of a value on the 7-segment display.
        """
        return self._SEG_CHAR.get(str(value), self._SEG_CHAR['empty'])

    def display_number(self, number):
        """
        This method displays a number on a 7-segment display.
        """
        if not isinstance(number, int):
            raise ValueError("Invalid input type. The input should be an integer.")
        if number > 9999 or number < -999:
            raise ValueError("Invalid input value. The input should be between -999 and 9999.")
        if self.pin_signal_out < 0:
            raise Exception("Assign the pins first.")
        if self.__freq < 0:
            raise Exception("Assign the frequency first.")

        # Convert the number to a 4-digit string
        number_str = str(number).zfill(4)

        # Convert each digit to its binary representation
        segments = [self.__segment(digit) for digit in number_str]

        # Combine the binary representations into one string
        data_packet = "".join(segments)

        # Add the parity bit
        data_packet += str(data_packet.count('1') % 2)

        # Send the packet over the serial bus
        self._writeSerial(data_packet)

