import paho.mqtt.client as mqtt
from random import randint, randrange,uniform
import time

mqttBroker="192.168.187.230"
client=mqtt.Client("test_client")
client.connect(mqttBroker)


while True:
    print("Note for string/char datatype, enter the data in single or double quotes")
    inp=eval(input("Enter the data to publish : "))
    client.publish("new_topic",inp)
    print("Published data : ",inp," of datatype ",type(inp))
    time.sleep(1)

