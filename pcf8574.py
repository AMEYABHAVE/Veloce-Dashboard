import smbus
import time
 
pot1 = 0x01
bus = smbus.SMBus(1)
 
while True:
    print(bus.read_byte(0x48))
    time.sleep(0.5)