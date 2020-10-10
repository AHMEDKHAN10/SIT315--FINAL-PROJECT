from flask import Flask, jsonify, render_template, request
# import paho.mqtt.publish as publish
from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import time as t
import json

ENDPOINT = "ak42bv2i7c4lr-ats.iot.eu-central-1.amazonaws.com"
CLIENT_ID = "MQTT"
PATH_TO_CERT = "certificates/41148337e5-certificate.pem.crt"
PATH_TO_KEY = "certificates/41148337e5-private.pem.key"
PATH_TO_ROOT = "certificates/root.pem"
#MESSAGE = "Hello World"

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

#connect_future = mqtt_connection.connect()

# MQTT_SERVER = "127.0.0.1"
# MQTT_PATH = "test_channel"

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('pro.html')

@app.route('/room')
def index():
    return render_template('project.html')

@app.route('/LEDon')
def LEDon():
    MESSAGE = 'LED ON'
    #data = "{} [{}]".format(MESSAGE)
    #message = {"message" : data}
    mqtt_connection.publish(topic="/test_channel/room1/lights", payload=json.dumps(MESSAGE), qos=mqtt.QoS.AT_LEAST_ONCE)
    # publish.single(MQTT_PATH+"/room1", "1", hostname=MQTT_SERVER) #send data continuously every 3 seconds
    # time.sleep(5)
    print('LED ON')
    return "Nothing"

@app.route('/LEDoff')
def LEDoff():
    MESSAGE = 'LED OFF'
    #data = "{} [{}]".format(MESSAGE)
    #message = {"message" : data}
    mqtt_connection.publish(topic="/test_channel/room1/lights", payload=json.dumps(MESSAGE), qos=mqtt.QoS.AT_LEAST_ONCE)
    # publish.single(MQTT_PATH, "1", hostname=MQTT_SERVER) #send data continuously every 3 seconds
    # time.sleep(5)
    print('LED OFF')
    return "Nothing"

@app.route('/Fanon')
def Fanon():
    MESSAGE = '1'
    data = "{} [{}]".format(MESSAGE)
    message = {"message" : data}
    mqtt_connection.publish(topic="/test_channel/room1/fan", payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    # publish.single(MQTT_PATH, "1", hostname=MQTT_SERVER) #send data continuously every 3 seconds
    # time.sleep(5)
    print('Fan ON')
    return "Nothing"

@app.route('/Fanoff')
def fanoff():
    MESSAGE = '2'
    data = "{} [{}]".format(MESSAGE)
    message = {"message" : data}
    mqtt_connection.publish(topic="/test_channel/room1/fan", payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    # publish.single(MQTT_PATH, "1", hostname=MQTT_SERVER) #send data continuously every 3 seconds
    # time.sleep(5)
    print('Fan OFF')
    return "Nothing"

@app.route('/AllLEDon')
def AllLEDon():
    MESSAGE = '1'
    data = "{} [{}]".format(MESSAGE)
    message = {"message" : data}
    mqtt_connection.publish(topic="/test_channel/room1/lights", payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    mqtt_connection.publish(topic="/test_channel/room2/lights", payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    mqtt_connection.publish(topic="/test_channel/room3/lights", payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    # publish.single(MQTT_PATH, "1", hostname=MQTT_SERVER) #send data continuously every 3 seconds
    # time.sleep(5)
    print('All LED ON')
    return "Nothing"

@app.route('/AllLEDoff')
def AllLEDoff():
    MESSAGE = '2'
    data = "{} [{}]".format(MESSAGE)
    message = {"message" : data}
    mqtt_connection.publish(topic="/test_channel/room1/lights", payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    mqtt_connection.publish(topic="/test_channel/room2/lights", payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    mqtt_connection.publish(topic="/test_channel/room3/lights", payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    # publish.single(MQTT_PATH, "1", hostname=MQTT_SERVER) #send data continuously every 3 seconds
    # time.sleep(5)
    print('All LED OFF')
    return "Nothing"

@app.route('/AllFanon')
def AllFanon():
    MESSAGE = '1'
    data = "{} [{}]".format(MESSAGE)
    message = {"message" : data}
    mqtt_connection.publish(topic="/test_channel/room1/fan", payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    mqtt_connection.publish(topic="/test_channel/room2/fan", payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    mqtt_connection.publish(topic="/test_channel/room3/fan", payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    # publish.single(MQTT_PATH, "1", hostname=MQTT_SERVER) #send data continuously every 3 seconds
    # time.sleep(5)
    print('All Fans ON')
    return "Nothing"

@app.route('/AllFanoff')
def AllFanoff():
    MESSAGE = '2'
    data = "{} [{}]".format(MESSAGE)
    message = {"message" : data}
    mqtt_connection.publish(topic="/test_channel/room1/fan", payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    mqtt_connection.publish(topic="/test_channel/room2/fan", payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    mqtt_connection.publish(topic="/test_channel/room3/fan", payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    # publish.single(MQTT_PATH, "1", hostname=MQTT_SERVER) #send data continuously every 3 seconds
    # time.sleep(5)
    print('All Fans OFF')
    return "Nothing"



if __name__ == '__main__':
   app.run()
