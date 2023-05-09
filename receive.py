import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
   global flag_connected
   flag_connected = 1
   client_subscriptions(client)
   print("Connected to MQTT server")

def on_disconnect(client, userdata, rc):
   global flag_connected
   flag_connected = 0
   print("Disconnected from MQTT server")
   
# a callback functions 
def callback_esp32_sensor1(client, userdata, msg):
    print('ESP sensor1 data: ', msg.payload.decode('utf-8'))

def on_log(client, userdata, level, buf):
    print("log: ",buf)

def client_subscriptions(client):
    client.subscribe('KRSTI/data')

def on_log(client, userdata, level, buf):
    print("log: ",buf)


client = mqtt.Client("rpi_client1") #this should be a unique name
flag_connected = 0

client.on_connect = on_connect
client.on_log=on_log
client.on_disconnect = on_disconnect
client.message_callback_add('KRSTI/data', callback_esp32_sensor1)
client.connect('127.0.0.1',1883)

client.loop_start()
client_subscriptions(client)
print("......client setup complete............")


while True:
    time.sleep(4)
    if (flag_connected != 1):
        print("trying to connect MQTT server..")
