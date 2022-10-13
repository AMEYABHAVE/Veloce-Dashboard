from smbus import SMBus
import time
 
addr = 0x08 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
 
time.sleep(0.5)

while(True):
    var1 = bus.read_byte(addr)
    print(str(var1))
    var2 = bus.read_byte(addr)
    print(str(var2))
    var3 = bus.read_byte(addr)
    print(str(var3))
    time.sleep(0.5)

