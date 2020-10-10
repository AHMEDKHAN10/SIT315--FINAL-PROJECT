# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import time as t
import json
import RPi.GPIO as GPIO

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
ENDPOINT = "ak42bv2i7c4lr-ats.iot.eu-central-1.amazonaws.com"
CLIENT_ID = "MQTT"
PATH_TO_CERT = "certificates/root-CA.pem"
PATH_TO_KEY = "certificates/MQTT.private.key"
PATH_TO_ROOT = "certificates/MQTT.cert.pem"

TOPIC1 = "/test_channel/#" #this is the name of topic, like temp
TOPIC2 = "/test_channel/room1/lights"  
TOPIC3 = "/test_channel/room1/fan"  
TOPIC4 = "/test_channel/room1/#" 
TOPIC5 = "/test_channel/#/lights"  
TOPIC6 = "/test_channel/#/fan"  
  

#RANGE = 20

# Spin up resources
event_loop_group = io.EventLoopGroup(1)
host_resolver = io.DefaultHostResolver(event_loop_group)
client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
mqtt_connection = mqtt_connection_builder.mtls_from_path(
            endpoint=ENDPOINT,
            cert_filepath=PATH_TO_CERT,
            pri_key_filepath=PATH_TO_KEY,
            client_bootstrap=client_bootstrap,
            ca_filepath=PATH_TO_ROOT,
            client_id=CLIENT_ID,
            clean_session=False,
            keep_alive_secs=6
            )
print("Connecting to {} with client ID '{}'...".format(
        ENDPOINT, CLIENT_ID))
# Make the connect() call

# Future.result() waits until a result is available
#connect_future.result()
print("Connected!")
# Publish message to server desired number of times.
# print('Begin Publish')

# for i in range (RANGE):
#     data = "{} [{}]".format(MESSAGE, i+1)
#     message = {"message" : data}
#     mqtt_connection.publish(topic=TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
#     print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
#     t.sleep(0.1)
# print('Publish End')
# disconnect_future = mqtt_connection.disconnect()
# disconnect_future.result()


def on_connect(client, userdata, flags, rc):
    print("Connected")
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    mqtt_connection.subscribe(TOPIC1)
    mqtt_connection.subscribe(TOPIC2)
    mqtt_connection.subscribe(TOPIC3)
    mqtt_connection.subscribe(TOPIC4)
    mqtt_connection.subscribe(TOPIC5)
    mqtt_connection.subscribe(TOPIC6)



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if(msg.payload == "1"):
        GPIO.output(16, True)
    else:
        GPIO.output(16, False)
    # more callbacks, etc

connect_future = mqtt_connection.connect()
connect_future.on_connect()
connect_future.on_message()