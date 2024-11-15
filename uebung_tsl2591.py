import time
import csv
import board
import busio
import adafruit_tsl2591

# I2C-Schnittstelle initialisieren
i2c = busio.I2C(board.SCL, board.SDA)

# TSL2591-Sensor initialisieren
sensor = adafruit_tsl2591.TSL2591(i2c)

# CSV-Datei erstellen oder öffnen
csv_filename = "tsl2591_data.csv"
with open(csv_filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Spaltenüberschriften hinzufügen
    writer.writerow(["Timestamp", "Gesamthelligkeit (Lux)", "Infrarotlicht", "Sichtbares Licht", "Gesamtspektrum"])
    print(f"CSV-Datei '{csv_filename}' wurde erstellt.")

    while True:
        try:
            # Sensordaten auslesen
            lux = sensor.lux
            infrared = sensor.infrared
            visible = sensor.visible
            full_spectrum = sensor.full_spectrum

            # Werte validieren (z. B. Lux darf nicht None sein)
            if lux is not None and 0 <= lux <= 100000:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                
                # Formatierten Eintrag erstellen
                formatted_entry = [
                    f"Zeit: {timestamp}",
                    f"Gesamthelligkeit: {lux:.2f} Lux",
                    f"Infrarotlicht: {infrared}",
                    f"Sichtbares Licht: {visible}",
                    f"Gesamtspektrum (IR + sichtbares Licht): {full_spectrum}"
                ]
                
                # Werte in die CSV-Datei schreiben
                writer.writerow(formatted_entry)
                csvfile.flush()  # Puffer leeren und Daten sofort schreiben
                print(f"Gespeichert: {formatted_entry}")
            else:
                print("Ungültige Werte, Eintrag übersprungen.")

        except Exception as e:
            print(f"Fehler: {e}")

        # 1 Sekunde warten, bevor der nächste Eintrag gemacht wird
        time.sleep(1)