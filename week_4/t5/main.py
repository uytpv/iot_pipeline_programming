from multi_sensor import MultiSensor
from segment_display import SegmentDisplay

print("Vending machine booting...")

multiSensor = MultiSensor(1, "internal")
display1 = SegmentDisplay(1, 2, 9600)
display2 = SegmentDisplay(3, 4, 9600)

temp = multiSensor.t_sensor.readRaw()
hum = multiSensor.h_sensor.readRaw()
print()
print("Component group: 1")
multiSensor.printLocation()
print(f"Measurements - Temp: {temp:.2f} C, Hum: {hum:.2f} %")

display1.showOnDisplay(str(bin(int(temp))))
display2.showOnDisplay(str(bin(int(hum%10))))
print()
print("Vending machine shutting down.")
