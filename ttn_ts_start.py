# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 11:13:00 2019

Template file for sending data from The Things Network to ThingSpeak.

Replace this text with your own docstring documenting how this functions.

@author: Alla
"""

# Imports
import ttn # MQTT client for getting the CPU temperature from The Things Network (TTN)
import paho.mqtt.client as paho # MQTT client for publishing CPU temperature to ThingSpeak (TS)
import time
import base64

from dragino import Dragino
import logging
from time import sleep
import RPi.GPIO as GPIO

# TTN Parameters
app_id = ""# Write application ID of the device which is registered as your Raspberry Pi on TTN
access_key = "ttn-account-"# Write the access key of the application

# TS parameters
broker_url = "mqtt.thingspeak.com"# Write the URL of the MQTT server of ThingSpeak
broker_port = 1883 # Write the port number you wish to use
api_key = ""# Write the API key of the channel at TS you want to send to
channelID = "" # Write the channel ID here

# Create the topic string.
topic = "channels/" + channelID + "/publish/" + api_key

# Callback which receives messages "msg" from TTN using MQTT client "client"
def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  #print(msg)
  print("Data:", msg.payload_raw)
  data = msg.payload_raw
  temperature = base64.b64decode(data) # Decodes the raw payload data
  temperature_decoded = temperature.decode("ASCII") # Because it was encoded in ASCII, we decode it in ASCII
  print(temperature_decoded)
  

# Defines the handler which connects to TTN
handler = ttn.HandlerClient(app_id, access_key)

# Using mqtt client to fetch data from TTN
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
print("Starting MQTT client")
mqtt_client.connect()
time.sleep(60) # Script runs for one minute, waiting for data from TTN
print("Stopping MQTT client")
mqtt_client.close()
