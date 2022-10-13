import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.clock import Clock

from kivy.core.window import Window
Window.size = (800, 480)

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

bus= smbus.SMBus(1)
Device_Address = 0x68

class Main_Class(FloatLayout):

    def MPU_Init(self, *a):
        bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

        bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

        bus.write_byte_data(Device_Address, CONFIG , 0)

        bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

        bus.write_byte_data(Device_Address, INT_ENABLE, 1)

    def read_raw_data(self, addr):
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)

        value = ((high << 8) | low)

        if(value>32768):
            value = value - 65536
        return value

    def MPU_data(self,*a):
        acc_x = self.read_raw_data(ACCEL_XOUT_H)
        acc_y= self.read_raw_data(ACCEL_YOUT_H)
        acc_z = self.read_raw_data(ACCEL_ZOUT_H)
        gyro_x = self.read_raw_data(GYRO_XOUT_H)
        gyro_y = self.read_raw_data(GYRO_YOUT_H)
        gyro_z = self.read_raw_data(GYRO_ZOUT_H)
        Ax = acc_x/16384.0
        Ay = acc_y/16384.0
        Az = acc_z/16384.0
        Gx = gyro_x/131.0
        Gy = gyro_y/131.0
        Gz = gyro_z/131.0

        self.Test1.text= str(int(Ax))
        self.Test2.text= str(int(Ay))
        self.Test3.text= str(int(Az))
        self.Test4.text= str(int(Gx))
        self.Test5.text= str(int(Gy))
        self.Test6.text= str(int(Gz))

        Clock.schedule_once(self.MPU_data, 0.1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.Test1 = Button(
            disabled = True,
            #text settings
            text = "20*",
            font_size = "84sp",
            bold = True,
            #size and position
            size_hint = (.20,.20),
            pos_hint = {"x":.1, "y":.1},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.Test2 = Button(
            disabled = True,
            #text settings
            text = "20*",
            font_size = "84sp",
            bold = True,
            #size and position
            size_hint = (.20,.20),
            pos_hint = {"x":.3, "y":.1},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.Test3 = Button(
            disabled = True,
            #text settings
            text = "20*",
            font_size = "84sp",
            bold = True,
            #size and position
            size_hint = (.20,.20),
            pos_hint = {"x":.5, "y":.1},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.Test4 = Button(
            disabled = True,
            #text settings
            text = "20*",
            font_size = "84sp",
            bold = True,
            #size and position
            size_hint = (.20,.20),
            pos_hint = {"x":.1, "y":.5},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.Test5 = Button(
            disabled = True,
            #text settings
            text = "20*",
            font_size = "84sp",
            bold = True,
            #size and position
            size_hint = (.20,.20),
            pos_hint = {"x":.3, "y":.5},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.Test6 = Button(
            disabled = True,
            #text settings
            text = "20*",
            font_size = "84sp",
            bold = True,
            #size and position
            size_hint = (.20,.20),
            pos_hint = {"x":.5, "y":.5},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.add_widget(self.Test1)
        self.add_widget(self.Test2)
        self.add_widget(self.Test3)
        self.add_widget(self.Test4)
        self.add_widget(self.Test5)
        self.add_widget(self.Test6)

        self.MPU_Init()
        self.MPU_data()
           
class Test_App(App):

    def build(self):

        Window.borderless = True
        Window.fullscreen = True

        return Main_Class()

test = Test_App()
test.run()