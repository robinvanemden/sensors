"""
    JADS 2020 Data-Driven Food Value Chain course
    Introduction to Sensors

    Minimal MQTT client demo - demonstrates ease of use.
    Makes use of the open http://www.mqtt-dashboard.com/index.html
    And yes, globals are evil ;)

"""


import threading
import paho.mqtt.client as mqtt
import os


def on_connect(client, userdata, flags, rc):
    global topic
    global publisher_name
    print("Welcome " + publisher_name + ", you're connected to " + topic + "\n")
    print("Type 'q' to exit the chat.\n")
    client.subscribe(topic)


def on_message(client, userdata, msg):
    global publisher_name
    incoming_message = msg.payload.decode()
    splitted_msg = [x.strip() for x in incoming_message.split(',', 1)]
    sender_name = splitted_msg[0]
    if sender_name != publisher_name:
        print(sender_name + ":" + splitted_msg[1])


def publish():
    global publisher_name
    global topic
    new_msg = input()
    if new_msg == "quit" or new_msg == "q" or new_msg == "exit" or new_msg == "quit()":
        os._exit(1)
    client.publish(topic, publisher_name + "," + new_msg)
    return publish()


def receive():
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()


def config():
    global publisher_name
    global topic
    while True:
        publisher_name = input("Enter your username: ")
        if publisher_name.isalpha():
            break
        print("Please enter characters A-Z only")
    return "Loading chat (" + topic + ")..."


topic = "jads/intro-to-sensors"
print(config())

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)

publish_thread = threading.Thread(target=publish)
receive_thread = threading.Thread(target=receive)

publish_thread.start()
receive_thread.start()
