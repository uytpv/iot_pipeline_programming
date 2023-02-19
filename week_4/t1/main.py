from sensor import Sensor

def main():
    print("Vending machine booting...")

    sensor1 = Sensor(1, "Lahti")
    sensor2 = Sensor(2, "Lappeenranta")

    sensor1.printLocation()
    sensor1.printReading()

    sensor2.printLocation()
    sensor2.printReading()

    print("Shutting down.")

if __name__ == "__main__":
    main()
