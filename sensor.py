#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

trigPin = 7
echoPin = 11
redLightPin = 15
blueLightPin = 16
warningLightPin = 22
 
while True:
      time.sleep(1) #ensures the yellow light isn't always on, this runs the loop once about every 4 seconds


      # sets the mode of the board
      GPIO.setmode(GPIO.BOARD)
      # sets up the pin orientation for the trigger pin and the echo pin on the  
      GPIO.setup(trigPin, GPIO.OUT)
      GPIO.setup(echoPin, GPIO.IN)
      # sets up the pin orientation for turning the blue and red light on
      GPIO.setup(redLightPin,GPIO.OUT)
      GPIO.setup(blueLightPin, GPIO.OUT)

      # GPIO setup for warning light
      GPIO.setup(warningLightPin, GPIO.OUT)

      GPIO.output(trigPin, GPIO.LOW) # makes it so the sensor isnt measuring anything

      print("Do not move the sensor while the yellow light is on!!!")
      GPIO.output(warningLightPin, GPIO.HIGH)
 
      time.sleep(2) # the sensor will measure almost exactly every 2 seconds
 
      GPIO.output(trigPin, GPIO.HIGH) # turns the sensor on so it will start measuring
 
      time.sleep(0.00001)
 
      GPIO.output(trigPin, GPIO.LOW) #turns the sensor back off
      GPIO.output(warningLightPin, GPIO.LOW)
 
      while GPIO.input(echoPin)==0: # this will keep updating the time 
            pulseStartTime = time.time()
      while GPIO.input(echoPin)==1: # this will end the time when the sound comes back to the sensor
            pulseEndTime = time.time()
 
      pulseDuration = pulseEndTime - pulseStartTime
      distance = round(pulseDuration * 17150, 2) # it multiplies the pulse duration by 17150, in order to convert the time into centimeters, then it rounds it to two decimal places
      print("Distance:",distance,"cm") # troubleshooting
      if distance < 10 :
          GPIO.output(redLightPin,GPIO.HIGH) # turns the red light on and the blue light off when the distance is less thatn 10
          GPIO.output(blueLightPin,GPIO.LOW)
      elif distance >= 10: # turns the red light off and the blue light on when the distance is greater than 10
          GPIO.output(redLightPin,GPIO.LOW)
          GPIO.output(blueLightPin,GPIO.HIGH)



