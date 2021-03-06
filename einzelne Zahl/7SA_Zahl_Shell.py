# Initialisierung
import time
import sys
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

# schieben
def doSchieben():
    GPIO.output(schieben,1)
    time.sleep(0.001)
    GPIO.output(schieben,0)

# Eine Zahl ins Schieberegister
def n_to_s(n_p):
    for i in range(8):
        GPIO.output(levelinput,int(n_p[i]))
        GPIO.output(shift,1)
        time.sleep(0.001)
        GPIO.output(shift,0)

    doSchieben()

# Prgrammstart (Eine 7-Segment-Anzeige)

# ausschalten
n_to_s(n_a[10])
n_to_s(n_a[10])

zahl = str(sys.argv[1])

if zahl == "p":
    zahl = "11"
elif zahl == "a":
    zahl = "10"

zahl = int(zahl)

if zahl in range(0, 12):
    n_to_s(n_a[int(zahl)])

time.sleep(5)

GPIO.cleanup()
