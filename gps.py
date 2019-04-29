# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 10:33:04 2019

@author: Alla
"""

from dragino import Dragino
import logging
from time import sleep
import RPi.GPIO as GPIO


while True:
  GPIO.setwarnings(False)
  D = Dragino("dragino.ini", logging_level=logging.DEBUG)
  D.get_gps()
  gpsMsg = D.get_gps()
  print(gpsMsg)
  
  
  gpsMsg = str(gpsMsg)
  
  print("gpsMsg type: ", type(gpsMsg))
  
  print("gpsMsg: ", gpsMsg)
  gpsList = gpsMsg.split(",")
  #print("GPS list: ", gpsList[2])
  if gpsList[0] == "$GPGGA":
      Latitude = (float(gpsList[2])/100)
      Longtitude = (float(gpsList[4])/100)
#          print("Latitude: %s" % (float(gpsList[2])/100))
#          print("Longtitude: %s" % (float(gpsList[4])/100))
  
  while not D.registered():
      print("waiting")
      sleep(2)
  
  D.send(str(float(gpsList[2])/100) + "," + str(float(gpsList[4])/100)) 
  sleep(30)