from multi_sensor import MultiSensor
from segment_display import SegmentDisplay

# create a multi-sensor instance
sensor1 = MultiSensor(1, "Lahti")
sensor2 = MultiSensor(2, "Lappeenranta")

# create two segment display instances
display1 = SegmentDisplay()
display2 = SegmentDisplay()

# connect the multi-sensor and segment displays
sensor1.connect_display(display1)
sensor1.connect_display(display2)

# boot up message
print("Vending machine booting...")

# group of components with one multi-sensor and two segment displays
component_group = [sensor1, display1, display2]

# print out component group information
print("Component group: 1")
print("Location: internal")

# read the humidity value from the sensor and display it twice
humidity = sensor1.readRaw()
print("Measurements - Temp: {:.2f} C, {:.2f} %".format(sensor1.readRaw(), humidity))
display1.show_value(humidity)
display2.show_value(humidity)

# shutdown message
print("Vending machine shutting down.")
