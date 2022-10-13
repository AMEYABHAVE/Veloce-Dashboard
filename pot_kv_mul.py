import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.clock import Clock

import  smbus

bus= smbus.SMBus(1)
add= 0x03

class Main_Class(FloatLayout):

    def Pot_data(self,*a):
        
        #0x00 for A0, 0x01 for A1, 0x02 for A2, 0x03 for A3
        bus.write_byte(0x48, 0x03) # first write the data to main bus
        pot1 = bus.read_byte(0x48) #read from main bus

        bus.write_byte(0x48, 0x01) # first write the data to main bus
        pot2 = bus.read_byte(0x48) #read from main bus

        self.Test1.text = str(int(pot1))
        self.Test2.text = str(int(pot2))
        Clock.schedule_once(self.Pot_data, 0.1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.Test1 = Button(
            disabled = True,
            #text settings
            text = "",
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

        self.Test2 = Button(
            disabled = True,
            #text settings
            text = "",
            font_size = "84sp",
            bold = True,
            #size and position
            size_hint = (.50,.50),
            pos_hint = {"x":.0, "y":.5},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.add_widget(self.Test2)

        self.Pot_data()
  
class Test_App(App):

    def build(self):
        return Main_Class()

test = Test_App()
test.run()