import paho.mqtt.client as mqtt 
import time

broker_address="192.168.18.45"

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def on_log(client, userdata, level, buf):
    print("log: ",buf)


print("creating new instance")
client = mqtt.Client("KRI") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker

while True:
    print("Publishing message to topic")
    client.publish("KRSTI/data", "kontol")
    time.sleep(4) # wait