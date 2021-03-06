# Initialisierung
import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

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

# Zahl anzeigen
def show_number(msg_zahl):

    # ausschalten
    n_to_s(n_a[10])
    n_to_s(n_a[10])

    doSchieben()

    # anzeigen
    zahl = str(msg_zahl)

    if zahl == "p":
        zahl = "11"
    elif zahl == "a":
        zahl = "10"

    zahl = int(zahl)
    
    if zahl in range(0, 12):
        n_to_s(n_a[int(zahl)])

    doSchieben()

# Countdown
def countdown(msg_zahl):

    # ausschalten
    n_to_s(n_a[10])
    n_to_s(n_a[10])

    doSchieben()

    start = str(msg_zahl)
    if int(start) > 99:
        start = "99"

    # Countdown starten
    for i in range(int(start)+1):

        zahl = int(start) - i

        if len(str(zahl)) == 1:
             zahl = "0" + str(zahl)

             n_to_s(n_a[int(zahl[1])])
             n_to_s(n_a[0])

        elif len(str(start)) == 2:
            zahl = str(zahl)

            n_to_s(n_a[int(zahl[1])])
            n_to_s(n_a[int(zahl[0])])

        doSchieben()

        time.sleep(0.99)

    # blinken
    for i in range(2):

        n_to_s(n_a[10])
        n_to_s(n_a[10])

        doSchieben()

        time.sleep(0.4)

        n_to_s(n_a[0])
        n_to_s(n_a[0])

        doSchieben()

        time.sleep(0.4)

    # ausschalten
    n_to_s(n_a[10])
    n_to_s(n_a[10])

    doSchieben()

# MQTT
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("7-SA/#")

def on_message(client, userdata, msg):

    msg_len = (len(str(msg.payload)))-3
    message = ""
    for i in range(msg_len):
        message = message + str(msg.payload)[2+i]

    if msg.topic == "7-SA/Zahl":
        show_number(message)
    elif msg.topic == "7-SA/Countdown":
        countdown(message)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.x.x", 1883, 60)

client.loop_forever()

GPIO.cleanup()
