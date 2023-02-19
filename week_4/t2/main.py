from temp_sensor import TempSensor

def main():
    print("Vending machine booting...")

    sensor1 = TempSensor(1, "Lahti")
    sensor2 = TempSensor(2, "Lappeenranta")

    sensor1.printLocation()
    sensor1.displayTemp()
    sensor2.printLocation()
    sensor2.displayTemp()
    print("Shutting down.")

if __name__ == "__main__":
    main()
