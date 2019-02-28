import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)

while True:
	GPIO.output(21, GPIO.HIGH)
