import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.clock import Clock

import  smbus

bus= smbus.SMBus(1)

class Main_Class(FloatLayout):

    def Pot_data(self,*a):
        
        pot = bus.read_byte(0x48)

        self.Test1.text = str(int(pot))
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
            size_hint = (.50,.50),
            pos_hint = {"x":.5, "y":.5},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.add_widget(self.Test1)

        self.Pot_data()
  
class Test_App(App):

    def build(self):
        return Main_Class()

test = Test_App()
test.run()