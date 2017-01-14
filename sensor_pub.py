#!/usr/bin/python
import sys
import socket
import time
from random import choice
import random
import paho.mqtt.client as mqtt

def on_connect(client, obj, flags, rc):
    print("rc: "+str(rc))

#def on_message(client, obj, msg):
#    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_publish(client, obj, mid):
    print("mid: "+str(mid))

#def on_subscribe(client, obj, mid, granted_qos):
#   print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

client = mqtt.Client()

client.on_connect = on_connect
#client.on_message = on_message
client.on_publish = on_publish

client.connect("m2m.eclipse.org", 1883, 60)

client.loop_start()
while(True):
    time.sleep(1)
    list = ['Occupied','Free']
    payload = random.choice(list)
    client.publish("topic1",payload,0,False)

#client.on_subscribe = on_subscribe
# Uncomment to enable debug messages
#client.on_log = on_log
