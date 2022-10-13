import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

from kivy.core.window import Window
Window.size = (800, 480)
Window.show_cursor = False

import  smbus

PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG     = 0x1A
GYRO_CONFIG= 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47

def MPU_Init():
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

	bus.write_byte_data(Device_Address, CONFIG , 0)

	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
	high = bus.read_byte_data(Device_Address, addr)
	low = bus.read_byte_data(Device_Address, addr+1)

	value = ((high << 8) | low)

	if(value>32768):
		value = value - 65536
	return value

bus= smbus.SMBus(1)
Device_Address = 0x68

print("Reading Data of Gyroscope and Accelerometer")

#while True:

		

		#print (Gx, Gy, Gz, Ax, Ay, Az)

class Main_Screen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #RPM__________________________________________
        self.RPM = Button(
            disabled = True,
            #text settings
            text = Gx,
            font_size = "20sp",
            bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.5, "y":.5},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.add_widget(self.RPM)
        
class Main_App(App):

    def build(self):
        #To make window borderless and fullscreen
        Window.borderless = True
        Window.fullscreen = True
        
        MPU_Init()
        
        acc_x = read_raw_data(ACCEL_XOUT_H)
		acc_y = read_raw_data(ACCEL_YOUT_H)
		acc_z = read_raw_data(ACCEL_ZOUT_H)

		gyro_x = read_raw_data(GYRO_XOUT_H)
		gyro_y = read_raw_data(GYRO_YOUT_H)
		gyro_z = read_raw_data(GYRO_ZOUT_H)

		Ax = acc_x/16384.0
		Ay = acc_y/16384.0
		Az = acc_z/16384.0

		Gx = gyro_x/131.0
		Gy = gyro_y/131.0
		Gz = gyro_z/131.0
       
    return Main_Screen()
    
test = Main_App()
test.run()