import os
import RPi.GPIO as GPIO
import time
import board
import adafruit_mpl3115a2

i2c = board.I2C()   # uses board.SCL and board.SDA
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)

stagerelay = 21
led = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(stagerelay,GPIO.OUT)
GPIO.output(led, GPIO.LOW)

launchaltitude = sensor.altitude
maxaltitude = -100
while True:
        altitude = sensor.altitude - launchaltitude
        print("altitude=" + str(altitude))
        print("max altitude=" + str(maxaltitude))

        if altitude > maxaltitude:
                maxaltitude = altitude
        if maxaltitude >= 3 and maxaltitude <= 4:
                print("2nd stage activated")
                time.sleep(1)
                GPIO.output(stagerelay, GPIO.HIGH) 
        if maxaltitude - altitude >= 3:
                GPIO.output(led,GPIO.HIGH)
                GPIO.output(stagerelay, GPIO.LOW)
                print("LED 1 is on")
                break
