import time
import paho.mqtt.client as mqtt


def on_publish(client, userdata, mid):
    print("message published")


client = mqtt.Client("KRI") #this name should be unique
client.on_publish = on_publish
client.connect('127.0.0.1', 1883)
client.loop_start()

k=0

while True:
    k=k+1
    if(k>20):
        k=1 
        
    try:
        msg =str(k)
        pubMsg = client.publish(
            topic='KRSTI/data',
            payload=msg.encode('utf-8'),
            qos=0,
        )
        pubMsg.wait_for_publish()
        print(pubMsg.is_published())
    
    except Exception as e:
        print(e)
        
    time.sleep(2)