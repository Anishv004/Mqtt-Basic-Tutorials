import paho.mqtt.client as mqtt
import time

def on_message(client,userdata,message):
    print("Recieved message", str(message.payload.decode("utf-8"))) # 


mqttBroker="192.168.187.230"
client=mqtt.Client("mobile")
client.connect(mqttBroker)


client.loop_start()
client.subscribe("new_topic")
client.on_message=on_message

time.sleep(30)
client.loop_stop()
