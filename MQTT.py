import time
import sys
import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
    print('conected with result code'+str(rc))
    client.subscribe([("nay/#", 0), ("a/#", 0),("b/#", 0)])
def on_message(client,userdata,msg):
    print(msg.topic,str(msg.payload),userdata,str(msg.qos))
def on_subscribe(client,userdata,mid,granted_qos):
    print("Subscribe",granted_qos)




client=mqtt.Client(client_id='subscribes', clean_session=False, protocol=mqtt.MQTTv31)

#client.user_data_set('12345')
user = "user"
password = "password"
client.username_pw_set(user, password)
client.on_connect=on_connect
client.on_message=on_message
client.on_subscribe=on_subscribe

client.connect("192.168.1.104")

client.loop_forever()






