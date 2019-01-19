from thermostat import thermostat
import RPi.GPIO as GPIO
import threading
import time
import paho.mqtt.client as mqtt
import argparse
import os

def thread2():
    global thermostat_obj



    while True:

        if thermostat_obj.valid_list():

            l = thermostat_obj.get_list()

            for a, b in l:
                GPIO.output(int(args.thermostat_pin_a), a)
                GPIO.output(int(args.thermostat_pin_b), b)

                time.sleep(float(args.thermostat_delay))


def thread1():
    global client

    while True:

        client.on_connect = on_connect
        client.on_message = on_message

        try_to_connect = True

        while try_to_connect:
            try:
                client.connect(args.mqtt_server_ip, int(args.mqtt_server_port), 60)
                try_to_connect = False
                break
            except Exception as e:
                print(e)



        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        client.loop_forever()



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):

    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(args.mqtt_topic_set_temperature)



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global thermostat_obj

    print(msg.topic + " "+ msg.payload.decode("utf-8"))

    if msg.topic == args.mqtt_topic_set_temperature:
        temperature = float(msg.payload.decode("utf-8"))
        thermostat_obj.set_temperature(temperature)

        hours = time.strftime("%H")
        minutes = time.strftime("%M")
        seconds = time.strftime("%S")
        client.publish(args.mqtt_topic_ack_temperature, hours + ":" + minutes + ":" + seconds, qos=0, retain=False)



# Argparse
parser = argparse.ArgumentParser()
parser.add_argument("--mqtt_server_ip", help="")
parser.add_argument("--mqtt_server_port", help="")
parser.add_argument("--mqtt_topic_set_temperature", help="")
parser.add_argument("--mqtt_topic_ack_temperature", help="")
parser.add_argument("--thermostat_pin_a", help="")
parser.add_argument("--thermostat_pin_b", help="")
parser.add_argument("--thermostat_delay", help="")
args = parser.parse_args()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(int(args.thermostat_pin_a), GPIO.OUT)
GPIO.setup(int(args.thermostat_pin_b), GPIO.OUT)

thermostat_obj = thermostat()

client = mqtt.Client()

t1= threading.Thread(target=thread1)
t2= threading.Thread(target=thread2)

t1.start()
time.sleep(1)
t2.start()
