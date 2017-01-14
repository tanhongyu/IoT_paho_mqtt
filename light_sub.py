#!/usr/bin/python
import sys
import socket
import paho.mqtt.client as mqtt

def on_connect(client, obj, flags, rc):
    print("rc: "+str(rc))

def on_message(client, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

#def on_publish(mqttc, obj, mid):
#   print("mid: "+str(mid))

def on_subscribe(client, obj, mid, granted_qos):
   print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

#if __name__ == '__main__':
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#mqttc.on_publish = on_publish
client.on_subscribe = on_subscribe
# Uncomment to enable debug messages
#mqttc.on_log = on_log

#host = ""

client.connect("m2m.eclipse.org", 1883, 60)
client.subscribe([("topic1",0),("topic2",0),("topic3",0),("topic4",0),("topic5",0)])
#TUE/Room-1/Sensor/+/State

client.loop_forever()
