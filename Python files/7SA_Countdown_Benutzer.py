# Initialisierung
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# AusgangsPins
levelinput = 26
schieben = 19
shift = 16

GPIO.setup(levelinput,GPIO.OUT,initial=False)
GPIO.setup(schieben,GPIO.OUT,initial=False)
GPIO.setup(shift,GPIO.OUT,initial=False)

# Zahlen
n_0 = "01111110"
n_1 = "00010010"
n_2 = "10111100"
n_3 = "10110110"
n_4 = "11010010"
n_5 = "11100110"
n_6 = "11101110"
n_7 = "00110010"
n_8 = "11111110"
n_9 = "11110110"
aus = "00000000"
dot = "00000001"

n_a = [n_0,n_1,n_2,n_3,n_4,n_5,n_6,n_7,n_8,n_9,aus,dot]

# Eine Zahl ins Schieberegister
def n_to_s(n_p):
    for i in range(8):
        GPIO.output(levelinput,int(n_p[i]))
        GPIO.output(shift,1)
        time.sleep(0.001)
        GPIO.output(shift,0)

# schieben
def schieben():
    GPIO.output(schieben,1)
    time.sleep(0.001)
    GPIO.output(schieben,0)

# Prgrammstart (Zwei 7-Segment-Anzeigen)

# Anweisung für den Benutzer
print("Dieses Programm erzeugt einen Countdown auf zwei 7-Segment-Anzeigen! \n")

try:
    while True:
        start = input("Geben Sie die Startzahl ein! ")
        if int(start) > 99:
            start = "99"
            print("Startzahl zu hoch!")
            print("Start ab 99!")
            
        # Countdown starten
        for i in range(int(start)+1):

            zahl = int(start) - i

            if len(str(zahl)) == 1:
                # Null vorne
                zahl = "0" + str(zahl)

                n_to_s(n_a[int(zahl[1])])
                n_to_s(n_a[0])

            elif len(str(start)) == 2:
                # zweistellige Zahl
                zahl = str(zahl)

                n_to_s(n_a[int(zahl[1])])
                n_to_s(n_a[int(zahl[0])])

            schieben()

            # Terminal Ausgabe
            print(int(zahl))

            time.sleep(0.99)

        # blinken
        for i in range(2):
            
            n_to_s(n_a[10])
            n_to_s(n_a[10])
        
            schieben()

            time.sleep(0.4)
            
            n_to_s(n_a[0])
            n_to_s(n_a[0])
        
            schieben()

            time.sleep(0.4)

        print("Der Countdown ist abgelaufen! \n")    

        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
