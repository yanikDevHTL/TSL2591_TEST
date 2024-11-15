import time
import board
import busio
import adafruit_tsl2591

# I2C-Schnittstelle initialisieren
i2c = busio.I2C(board.SCL, board.SDA)

# TSL2591-Sensor initialisieren
sensor = adafruit_tsl2591.TSL2591(i2c)

# Sensordaten auslesen
while True:
    try:
        print("Gesamthelligkeit: {:.2f} Lux".format(sensor.lux))
        print("Infrarotlicht: {}".format(sensor.infrared))
        print("Sichtbares Licht: {}".format(sensor.visible))
        print("Gesamtspektrum (IR + Sichtbares Licht): {}".format(sensor.full_spectrum))
        print("-" * 30)
    except Exception as e:
        print(f"Fehler: {e}")
    time.sleep(1)