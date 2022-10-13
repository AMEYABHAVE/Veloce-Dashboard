import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.IN)
while(1):
	print(GPIO.input(5))

