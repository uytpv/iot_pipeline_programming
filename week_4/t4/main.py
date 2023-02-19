from multi_sensor import MultiSensor
def main():
    print("Vending machine booting...")
    sensor1 = MultiSensor(1, "Lahti")
    sensor1.printLocation()
    sensor1.printReading()
    sensor2 = MultiSensor(2, "Lappeenranta")
    sensor2.printLocation()
    sensor2.printReading()
    print("Shutting down.")

if __name__ == "__main__":
    main()
