'''
VR Dashboard V 1.0
last update 21/3/22                
Obejctive : GUI only                
'''
#////////////////////////////////////////////////////////////
#importing Libraries and KV file

import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
import screen_brightness_control as sbc

#from kivy.uix.label import Label
#from kivy.lang import Builder

#////////////////////////////////////////////////////////////
#Setting Resolution and Background Colour
from kivy.core.window import Window
#Set it to a tuple with the (width, height) in Pixels
Window.size = (800, 480)
Window.show_cursor = False
Window.borderless = True
Window.fullscreen = True

#!/usr/bin/env python3
import serial

#Window.clearcolor = (255, 255, 255, 1) #to make background white

#////////////////////////////////////////////////////////////
#Global Parameters

#General
brightness = sbc.get_brightness()

#About Page
version_info = "v1.0"
last_update = "19/03/22" #ddmmyy

#Main Page
engine_rpm = 0
battery_voltage = 0
throttle = 95 #in percentage
wheel_speed = 0
gear_position = 0
engine_temp = 0
brake_pressure = 95 #in percentage

#////////////////////////////////////////////////////////////
##GUI
from unicodedata import name
import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

#from kivy.uix.label import Label
#from kivy.lang import Builder

#////////////////////////////////////////////////////////////
#Setting Resolution and Background Colour
from kivy.core.window import Window
#Set it to a tuple with the (width, height) in Pixels
Window.size = (800, 480)
#Window.show_cursor = False
Window.borderless = True
#Window.fullscreen = True

#Window.clearcolor = (255, 255, 255, 1) #to make background white

#////////////////////////////////////////////////////////////
#Global Parameters

#General

#About Page
version_info = "v1.0"
last_update = "19/03/22" #ddmmyy

#Main Page
engine_rpm = 0
battery_voltage = 0
throttle = 0 #in percentage
wheel_speed = 0
gear_position = 0
engine_temp = 0
brake_pressure = 0 #in percentage

#////////////////////////////////////////////////////////////
##GUI
#Main Page
class Main_Screen(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        global engine_rpm,throttle,brake_pressure, gear_position, wheel_speed       

        #RPM__________________________________________
        self.RPM = Button(
            disabled = True,
            #text settings
            text = str(engine_rpm),
            font_size = "44sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.0, "y":.9},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )

        self.add_widget(self.RPM)

        #Battery Voltage______________________________
        self.Battery_Voltage = Button(
            disabled = True,
            #text settings
            text = "14.4V",
            font_size = "26sp",
            bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.10, "y":.0},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )

        self.add_widget(self.Battery_Voltage)

        #Throttle_____________________________________
        self.Throttle = Button(
            disabled = True,
            #text settings
            text = str(throttle),
            font_size = "36sp",
            bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.9, "y":.9},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )

        self.add_widget(self.Throttle)

        #Brake Pressure______________________________
        self.Brake_Pressure = Button(
            disabled = True,
            #text settings
            text = str(brake_pressure),
            font_size = "36sp",
            bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.9, "y":.0},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )

        self.add_widget(self.Brake_Pressure)

        #Wheel Speed___________________________________
        self.Wheel_Speed = Button(
            disabled = True,
            #text settings
            text = str(wheel_speed),
            font_size = "192sp",
            bold = True,
            #size and position
            size_hint = (.50,.80),
            pos_hint = {"x":.0, "y":.1},
            #color settings
            color = (1,1,1,1),
            background_color = (0,0,0,255),
            opacity = (1)
        )

        self.add_widget(self.Wheel_Speed)

        #Gear Position____________________________________
        self.Gear_Position = Button(
            disabled = True,
            #text settings
            text = str(gear_position),
            font_size = "384sp",
            bold = True,
            #size and position
            size_hint = (.50,.80),
            pos_hint = {"x":.5, "y":.1},
            #color settings
            color = (1,1,1,1),
            background_color = (0,0,0,255),
            opacity = (1)
        )
        self.add_widget(self.Gear_Position)

        #Engine Temperature______________________________
        self.Engine_Temp = Button(
            disabled = True,
            #text settings
            text = "500C",
            font_size = "26sp",
            bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.0, "y":.0},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )

        self.add_widget(self.Engine_Temp)

        #Line Seperator______________________________
        self.LS = Button(
            #size and position
            size_hint = (0.05,.60),
            pos_hint = {"x":.5, "y":.2},
            #color settings
            color = (0,0,0,1),
            background_color = (255,255,0,255),
            opacity = (1)
        )

        self.add_widget(self.LS)

        #KMPH______________________________
        self.KMPH = Button(
            disabled = True,
            #text settings
            text = "kmph",
            font_size = "48sp", 
            bold = True,
            #size and position
            size_hint = (.15,.15),
            pos_hint = {"x":.2, "y":.2},
            #color settings
            color = (1,1,1,1),
            background_color = (0,0,0,255),
            opacity = (1)
        )

        self.add_widget(self.KMPH)

        #Throttle Percentage Bars_____________________
        self.Throttle1 = Button(
            disabled = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.2, "y":.9},
            #color settings
            background_color = (0,255,0,255)
        )
        self.add_widget(self.Throttle1)

        self.Throttle2 = Button(
            disabled = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.3, "y":.9},
            #color settings
            background_color = (0,255,0,255)
        )
        self.add_widget(self.Throttle2)

        self.Throttle3 = Button(
            disabled = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.4, "y":.9},
            #color settings
            background_color = (0,255,0,255)
        )
        self.add_widget(self.Throttle3)

        self.Throttle4 = Button(
            disabled = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.5, "y":.9},
            #color settings
            background_color = (0,255,0,255)
        )
        self.add_widget(self.Throttle4)

        self.Throttle5 = Button(
            disabled = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.6, "y":.9},
            #color settings
            background_color = (0,255,0,255)
        )
        self.add_widget(self.Throttle5)

        self.Throttle6 = Button(
            disabled = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.7, "y":.9},
            #color settings
            background_color = (0,255,0,255)
        )
        self.add_widget(self.Throttle6)

        self.Throttle7 = Button(
            disabled = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.8, "y":.9},
            #color settings
            background_color = (0,255,0,255)
        )
        self.add_widget(self.Throttle7)

        #Brake Percentage Bars____________________
        self.Brake1 = Button(
            disabled = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.2, "y":.0},
            #color settings
            background_color = (0,0,255,255)
        )
        self.add_widget(self.Brake1)

        self.Brake2 = Button(
            disabled = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.3, "y":.0},
            #color settings
            background_color = (0,0,255,255)
        )
        self.add_widget(self.Brake2)

        self.Brake3 = Button(
            disabled = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.4, "y":.0},
            #color settings
            background_color = (0,0,255,255)
        )
        self.add_widget(self.Brake3)

        self.Brake4 = Button(
            disabled = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.5, "y":.0},
            #color settings
            background_color = (0,0,255,255)
        )
        self.add_widget(self.Brake4)

        self.Brake5 = Button(
            disabled = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.6, "y":.0},
            #color settings
            background_color = (0,0,255,255)
        )
        self.add_widget(self.Brake5)

        self.Brake6 = Button(
            disabled = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.7, "y":.0},
            #color settings
            background_color = (0,0,255,255)
        )
        self.add_widget(self.Brake6)

        self.Brake7 = Button(
            disabled = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.8, "y":.0},
            #color settings
            background_color = (0,0,255,255)
        )
        self.add_widget(self.Brake7)

        self.Lets_Go = Button(
            disabled = True,
            #text settings
            text ="Let's Go",
            font_size = "150sp",
            bold = True,
            #size and position
            size_hint = (.5,.5),
            pos_hint = {"x":0.25, "y":0.25},
            #color settings
            color = (1,1,1,1),
            background_color = (0,0,0,255),
            italic = True,
            opacity = (1)
        )

        #self.add_widget(self.Lets_Go)

        #Throttle Percentage Bar Logic____________________
        if throttle < 5:
            self.Throttle1.background_color=(0,0,0,255)
            self.Throttle2.background_color=(0,0,0,255)
            self.Throttle3.background_color=(0,0,0,255)
            self.Throttle4.background_color=(0,0,0,255)
            self.Throttle5.background_color=(0,0,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 5 and throttle < 15:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,0,0,255)
            self.Throttle3.background_color=(0,0,0,255)
            self.Throttle4.background_color=(0,0,0,255)
            self.Throttle5.background_color=(0,0,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 15 and throttle < 30:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,0,0,255)
            self.Throttle4.background_color=(0,0,0,255)
            self.Throttle5.background_color=(0,0,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 30 and throttle < 45:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,255,0,255)
            self.Throttle4.background_color=(0,0,0,255)
            self.Throttle5.background_color=(0,0,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 45 and throttle < 60:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,255,0,255)
            self.Throttle4.background_color=(0,255,0,255)
            self.Throttle5.background_color=(0,0,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 60 and throttle < 75:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,255,0,255)
            self.Throttle4.background_color=(0,255,0,255)
            self.Throttle5.background_color=(0,255,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 75 and throttle < 90:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,255,0,255)
            self.Throttle4.background_color=(0,255,0,255)
            self.Throttle5.background_color=(0,255,0,255)
            self.Throttle6.background_color=(0,255,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 90:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,255,0,255)
            self.Throttle4.background_color=(0,255,0,255)
            self.Throttle5.background_color=(0,255,0,255)
            self.Throttle6.background_color=(0,255,0,255)
            self.Throttle7.background_color=(0,255,0,255)

        #Brake Percentage Bar Logic____________________
        if brake_pressure < 5:
            self.Brake1.background_color=(0,0,0,255)
            self.Brake2.background_color=(0,0,0,255)
            self.Brake3.background_color=(0,0,0,255)
            self.Brake4.background_color=(0,0,0,255)
            self.Brake5.background_color=(0,0,0,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 5 and brake_pressure < 15:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,0,255)
            self.Brake3.background_color=(0,0,0,255)
            self.Brake4.background_color=(0,0,0,255)
            self.Brake5.background_color=(0,0,0,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 15 and brake_pressure < 30:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,0,255)
            self.Brake4.background_color=(0,0,0,255)
            self.Brake5.background_color=(0,0,0,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 30 and brake_pressure < 45:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,255,255)
            self.Brake4.background_color=(0,0,0,255)
            self.Brake5.background_color=(0,0,0,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 45 and brake_pressure < 60:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,255,255)
            self.Brake4.background_color=(0,0,255,255)
            self.Brake5.background_color=(0,0,0,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 60 and brake_pressure < 75:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,255,255)
            self.Brake4.background_color=(0,0,255,255)
            self.Brake5.background_color=(0,0,255,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 75 and brake_pressure < 90:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,255,255)
            self.Brake4.background_color=(0,0,255,255)
            self.Brake5.background_color=(0,0,255,255)
            self.Brake6.background_color=(0,0,255,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 90:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,255,255)
            self.Brake4.background_color=(0,0,255,255)
            self.Brake5.background_color=(0,0,255,255)
            self.Brake6.background_color=(0,0,255,255)
            self.Brake7.background_color=(0,0,255,255)

        Clock.schedule_once(self.on_start_ani,8) #Change delay to change animation start time


#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    def on_start_ani(self,*a):
        global throttle, brake_pressure,engine_rpm, gear_position, wheel_speed
        wheel_speed+=10
        self.Wheel_Speed.text = str(wheel_speed)
        throttle+=10
        self.Throttle.text = str(throttle)
        brake_pressure+=10
        self.Brake_Pressure.text = str(brake_pressure)
        engine_rpm+=1000
        self.RPM.text = str(engine_rpm)
        if throttle%20==0:
            gear_position+=1
            self.Gear_Position.text = str(gear_position)
        if throttle < 5:
            self.Throttle1.background_color=(0,0,0,255)
            self.Throttle2.background_color=(0,0,0,255)
            self.Throttle3.background_color=(0,0,0,255)
            self.Throttle4.background_color=(0,0,0,255)
            self.Throttle5.background_color=(0,0,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 5 and throttle < 15:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,0,0,255)
            self.Throttle3.background_color=(0,0,0,255)
            self.Throttle4.background_color=(0,0,0,255)
            self.Throttle5.background_color=(0,0,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 15 and throttle < 30:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,0,0,255)
            self.Throttle4.background_color=(0,0,0,255)
            self.Throttle5.background_color=(0,0,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 30 and throttle < 45:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,255,0,255)
            self.Throttle4.background_color=(0,0,0,255)
            self.Throttle5.background_color=(0,0,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 45 and throttle < 60:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,255,0,255)
            self.Throttle4.background_color=(0,255,0,255)
            self.Throttle5.background_color=(0,0,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 60 and throttle < 75:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,255,0,255)
            self.Throttle4.background_color=(0,255,0,255)
            self.Throttle5.background_color=(0,255,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 75 and throttle < 90:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,255,0,255)
            self.Throttle4.background_color=(0,255,0,255)
            self.Throttle5.background_color=(0,255,0,255)
            self.Throttle6.background_color=(0,255,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 90:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,255,0,255)
            self.Throttle4.background_color=(0,255,0,255)
            self.Throttle5.background_color=(0,255,0,255)
            self.Throttle6.background_color=(0,255,0,255)
            self.Throttle7.background_color=(0,255,0,255)

        #Brake Percentage Bar Logic____________________
        if brake_pressure < 5:
            self.Brake1.background_color=(0,0,0,255)
            self.Brake2.background_color=(0,0,0,255)
            self.Brake3.background_color=(0,0,0,255)
            self.Brake4.background_color=(0,0,0,255)
            self.Brake5.background_color=(0,0,0,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 5 and brake_pressure < 15:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,0,255)
            self.Brake3.background_color=(0,0,0,255)
            self.Brake4.background_color=(0,0,0,255)
            self.Brake5.background_color=(0,0,0,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 15 and brake_pressure < 30:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,0,255)
            self.Brake4.background_color=(0,0,0,255)
            self.Brake5.background_color=(0,0,0,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 30 and brake_pressure < 45:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,255,255)
            self.Brake4.background_color=(0,0,0,255)
            self.Brake5.background_color=(0,0,0,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 45 and brake_pressure < 60:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,255,255)
            self.Brake4.background_color=(0,0,255,255)
            self.Brake5.background_color=(0,0,0,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 60 and brake_pressure < 75:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,255,255)
            self.Brake4.background_color=(0,0,255,255)
            self.Brake5.background_color=(0,0,255,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 75 and brake_pressure < 90:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,255,255)
            self.Brake4.background_color=(0,0,255,255)
            self.Brake5.background_color=(0,0,255,255)
            self.Brake6.background_color=(0,0,255,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 90:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,255,255)
            self.Brake4.background_color=(0,0,255,255)
            self.Brake5.background_color=(0,0,255,255)
            self.Brake6.background_color=(0,0,255,255)
            self.Brake7.background_color=(0,0,255,255)

        if throttle<100:
            Clock.schedule_once(self.on_start_ani,0.035)
        else:
            gear_position = 5
            self.Gear_Position.text = str(gear_position)
            Clock.schedule_once(self.on_start_ani2,0)

    def on_start_ani2(self,*a):
        global throttle, brake_pressure,engine_rpm, gear_position, wheel_speed
        wheel_speed-=10
        self.Wheel_Speed.text = str(wheel_speed)
        throttle-=10
        self.Throttle.text = str(throttle)
        brake_pressure-=10
        self.Brake_Pressure.text = str(brake_pressure)
        engine_rpm-=1000
        self.RPM.text = str(engine_rpm)
        if throttle%20==0:
            gear_position-=1
            self.Gear_Position.text = str(gear_position)

        if throttle < 5:
            self.Throttle1.background_color=(0,0,0,255)
            self.Throttle2.background_color=(0,0,0,255)
            self.Throttle3.background_color=(0,0,0,255)
            self.Throttle4.background_color=(0,0,0,255)
            self.Throttle5.background_color=(0,0,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 5 and throttle < 15:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,0,0,255)
            self.Throttle3.background_color=(0,0,0,255)
            self.Throttle4.background_color=(0,0,0,255)
            self.Throttle5.background_color=(0,0,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 15 and throttle < 30:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,0,0,255)
            self.Throttle4.background_color=(0,0,0,255)
            self.Throttle5.background_color=(0,0,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 30 and throttle < 45:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,255,0,255)
            self.Throttle4.background_color=(0,0,0,255)
            self.Throttle5.background_color=(0,0,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 45 and throttle < 60:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,255,0,255)
            self.Throttle4.background_color=(0,255,0,255)
            self.Throttle5.background_color=(0,0,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 60 and throttle < 75:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,255,0,255)
            self.Throttle4.background_color=(0,255,0,255)
            self.Throttle5.background_color=(0,255,0,255)
            self.Throttle6.background_color=(0,0,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 75 and throttle < 90:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,255,0,255)
            self.Throttle4.background_color=(0,255,0,255)
            self.Throttle5.background_color=(0,255,0,255)
            self.Throttle6.background_color=(0,255,0,255)
            self.Throttle7.background_color=(0,0,0,255)

        elif throttle > 90:
            self.Throttle1.background_color=(0,255,0,255)
            self.Throttle2.background_color=(0,255,0,255)
            self.Throttle3.background_color=(0,255,0,255)
            self.Throttle4.background_color=(0,255,0,255)
            self.Throttle5.background_color=(0,255,0,255)
            self.Throttle6.background_color=(0,255,0,255)
            self.Throttle7.background_color=(0,255,0,255)

        #Brake Percentage Bar Logic____________________
        if brake_pressure < 5:
            self.Brake1.background_color=(0,0,0,255)
            self.Brake2.background_color=(0,0,0,255)
            self.Brake3.background_color=(0,0,0,255)
            self.Brake4.background_color=(0,0,0,255)
            self.Brake5.background_color=(0,0,0,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 5 and brake_pressure < 15:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,0,255)
            self.Brake3.background_color=(0,0,0,255)
            self.Brake4.background_color=(0,0,0,255)
            self.Brake5.background_color=(0,0,0,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 15 and brake_pressure < 30:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,0,255)
            self.Brake4.background_color=(0,0,0,255)
            self.Brake5.background_color=(0,0,0,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 30 and brake_pressure < 45:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,255,255)
            self.Brake4.background_color=(0,0,0,255)
            self.Brake5.background_color=(0,0,0,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 45 and brake_pressure < 60:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,255,255)
            self.Brake4.background_color=(0,0,255,255)
            self.Brake5.background_color=(0,0,0,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 60 and brake_pressure < 75:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,255,255)
            self.Brake4.background_color=(0,0,255,255)
            self.Brake5.background_color=(0,0,255,255)
            self.Brake6.background_color=(0,0,0,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 75 and brake_pressure < 90:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,255,255)
            self.Brake4.background_color=(0,0,255,255)
            self.Brake5.background_color=(0,0,255,255)
            self.Brake6.background_color=(0,0,255,255)
            self.Brake7.background_color=(0,0,0,255)

        elif brake_pressure > 90:
            self.Brake1.background_color=(0,0,255,255)
            self.Brake2.background_color=(0,0,255,255)
            self.Brake3.background_color=(0,0,255,255)
            self.Brake4.background_color=(0,0,255,255)
            self.Brake5.background_color=(0,0,255,255)
            self.Brake6.background_color=(0,0,255,255)
            self.Brake7.background_color=(0,0,255,255)

        if throttle>0:
            Clock.schedule_once(self.on_start_ani2,0.035)
        else:
            self.Gear_Position.opacity = (1)
            self.Wheel_Speed.opacity = (1)
            self.LS.opacity= (1)
            self.KMPH.opacity = (1)
            self.remove_widget(self.Lets_Go)
            
        
    #Swipe gesture
    #Swipe to change screen
    def on_touch_move(self, touch):
        if touch.x > touch.ox and touch.x - touch.ox > 250 :
            Main_App.get_running_app().change_screen(screen_name="FocusMain", screen_direction = "right")

        if touch.ox > touch.x and touch.ox - touch.x > 250:
            Main_App.get_running_app().change_screen(screen_name="IMU", screen_direction = "left")


#----------------------------------------------------------------------------------------------
#IMU page

class IMU_Screen(Screen,FloatLayout):
    
    def MPU_data(self,*a):
        #if ser.in_waiting > 0:
        if __name__ == '__main__':
            ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
            ser.reset_input_buffer()
            
        if ser.in_waiting > 0:
            a = ser.readline().decode('utf-8').rstrip()
            
        self.Left_Front.text=f"{str(a)}"

        Clock.schedule_once(self.MPU_data, 0.01)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Background Image__________________________________
        self.background_img = Image(
            source = "IMU.png"    #PNG Only
        )
        self.add_widget(self.background_img)

        #Front Left Tyre____________________________________
        self.Left_Front = Button(
            disabled = True,
            #text settings
            text = "48  58\n58  55\n22  32",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.20,.20),
            pos_hint = {"x":.10, "y":.55},
            #color settings
            color = (1,1,1,1),
            background_color = (255,255,255,0)
        )

        self.add_widget(self.Left_Front)

        #Front Right Tyre___________________________________
        self.Right_Front = Button(
            disabled = True,
            #text settings
            text = "48  58\n58  55\n22  32",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.20,.20),
            pos_hint = {"x":.68, "y":.55},
            #color settings
            color = (1,1,1,1),
            background_color = (255,255,255,0)
        )

        self.add_widget(self.Right_Front)

        #Rear Left Tyre_____________________________________
        self.Left_Rear = Button(
            disabled = True,
            #text settings
            text = "48  58\n58  55\n22  32",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.20,.20),
            pos_hint = {"x":.03, "y":.2},
            #color settings
            color = (1,1,1,1),
            background_color = (255,255,255,0)
        )

        self.add_widget(self.Left_Rear)

        #Rear Right Tyre____________________________________
        self.Rear_Right = Button(
            disabled = True,
            #text settings
            text = "48  58\n58  55\n22  32",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.20,.20),
            pos_hint = {"x":.76, "y":.2},
            #color settings
            color = (1,1,1,1),
            background_color = (255,255,255,0)
        )

        self.add_widget(self.Rear_Right)

        #Title____________________________________
        self.Title = Button(
            disabled = True,
            #text settings
            text = "IMU",
            font_size = "36sp",
            bold = True,
            #size and position
            size_hint = (.30,.30),
            pos_hint = {"x":.35, "y":.78 },
            #color settings
            color = (1,1,1,1),
            background_color = (255,255,255,0)
        )

        self.add_widget(self.Title)
        self.MPU_data()

        #Calibrate____________________________________
        # self.Calibrate_Button = Button(
        #     #text settings
        #     text = "Calibrate",
        #     font_size = "24sp",
        #     bold = True,
        #     #size and position
        #     size_hint = (.20,.10),
        #     pos_hint = {"x":.40, "y":.05},
        #     #color settings
        #     color = (0,0,0,1),
        #     background_color = (255,255,255,1)

        #     #########LOGIC!!!!!!##########
        # )

        # self.add_widget(self.Calibrate_Button)

    #Swipe to change screen
    def on_touch_move(self, touch):
        if touch.x > touch.ox and touch.x - touch.ox > 250 :
            Main_App.get_running_app().change_screen(screen_name="Main", screen_direction = "right")

        if touch.ox > touch.x and touch.ox - touch.x > 250:
            Main_App.get_running_app().change_screen(screen_name="Raw", screen_direction = "left")

#----------------------------------------------------------------------------------------------
#Warnings page

class Warnings_Screen(Screen, FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Float for Title
        #Title__________________________________________
        self.Title = Button(
            disabled = True,
            #text settings
            text = "Warnings",
            font_size = "44sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.4, "y":.87},
            #color settings
            color = (1,1,1,1),
            background_color = (0,0,0,0)
        )

        self.add_widget(self.Title)

        self.layout()
        self.scroll=ScrollView(size=(Window.width,Window.height))
        self.scroll.do_scroll_y=True
        self.scroll.do_scroll_x=False
        self.scroll.add_widget(self.layout)
        self.add_widget(self.scroll)

    def layout(self):
        self.layout=GridLayout()
        self.layout.cols=2
        #self.layout.bind(minimum_height=self.layout.setter("height"))
        self.layout.size_hint_x=None
        self.layout.size_hint_y=5
        #self.layout.height=self.minimum_height
        self.layout.row_default_height=150
        self.layout.col_default_width=325
        self.layout.padding=75
        self.layout.row_force_default=True

        #PDB_Disconnected_________________________________________________
        self.PDB_Disconnected = Button(
            disabled = True,
            #text settings
            text = "         PDB \n Disconnected",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #PDB_Temperature_Warning_________________________________________________
        self.PDB_Temperature_Warning = Button(
            disabled = True,
            #text settings
            text = "PDB Temperature\n            High",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Main_Path_break______________________________
        self.Main_path_break = Button(
            disabled = True,
            #text settings
            text = "Main path \n    Break",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Gearbox_sensor_error_______________________________________________
        self.Gearbox_sensor = Button(
            disabled = True,
            #text settings
            text = "Gearbox Sensor\n          Error",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Battery_Voltage______________________________________________________
        self.Battery_Voltage = Button(
            disabled = True,
            #text settings
            text = "Battery Voltage\n          Low",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Battery_Disconnected________________________________________________
        self.Battery_Disconnected = Button(
            disabled = True,
            #text settings
            text = "Battery Sensor\n Disconnected",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Engine_Temperature_Disconnected_________________________________________________
        self.Engine_Temperature_Warning = Button(
            disabled = True,
            #text settings
            text = "Engine Temperature\n             Sensor \n      Disconnected",
            font_size = "34sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Engine_Temperature_High_________________________________________________
        self.Engine_Temperature_High = Button(
            disabled = True,
            #text settings
            text = "Engine Temperature\n              High",
            font_size = "34sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse1_____________________________________________________________
        self.Fuse1 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 1",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current____________________________________________________
        self.Over_current = Button(
            disabled = True,
            #text settings
            text = "Over current - 1",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse2_____________________________________________________________
        self.Fuse2 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 2",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current2____________________________________________________
        self.Over_current2 = Button(
            disabled = True,
            #text settings
            text = "Over current - 2",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse3_____________________________________________________________
        self.Fuse3 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 3",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_curren3____________________________________________________
        self.Over_current3 = Button(
            disabled = True,
            #text settings
            text = "Over current - 3",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse4_____________________________________________________________
        self.Fuse4 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 4",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current4____________________________________________________
        self.Over_current4 = Button(
            disabled = True,
            #text settings
            text = "Over current - 4",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse5_____________________________________________________________
        self.Fuse5 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 5",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current5____________________________________________________
        self.Over_current5 = Button(
            disabled = True,
            #text settings
            text = "Over current - 5",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse6_____________________________________________________________
        self.Fuse6 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 6",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current6____________________________________________________
        self.Over_current6 = Button(
            disabled = True,
            #text settings
            text = "Over current - 6",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse7_____________________________________________________________
        self.Fuse7 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 7",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current7____________________________________________________
        self.Over_current7 = Button(
            disabled = True,
            #text settings
            text = "Over current - 7",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse8_____________________________________________________________
        self.Fuse8 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 8",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current8____________________________________________________
        self.Over_current8 = Button(
            disabled = True,
            #text settings
            text = "Over current - 8",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse9_____________________________________________________________
        self.Fuse9 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 9",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current9____________________________________________________
        self.Over_current9 = Button(
            disabled = True,
            #text settings
            text = "Over current - 9",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse10_____________________________________________________________
        self.Fuse10 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 10",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current10____________________________________________________
        self.Over_current10 = Button(
            disabled = True,
            #text settings
            text = "Over current - 10",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        self.layout.add_widget(self.PDB_Disconnected)
        self.layout.add_widget(self.Main_path_break)
        self.layout.add_widget(self.PDB_Temperature_Warning)
        self.layout.add_widget(self.Gearbox_sensor)
        self.layout.add_widget(self.Battery_Voltage)
        self.layout.add_widget(self.Battery_Disconnected)
        self.layout.add_widget(self.Engine_Temperature_Warning)
        self.layout.add_widget(self.Engine_Temperature_High)

        self.layout.add_widget(self.Fuse1)
        self.layout.add_widget(self.Over_current)
        self.layout.add_widget(self.Fuse2)
        self.layout.add_widget(self.Over_current2)
        self.layout.add_widget(self.Fuse3)
        self.layout.add_widget(self.Over_current3)
        self.layout.add_widget(self.Fuse4)
        self.layout.add_widget(self.Over_current4)
        self.layout.add_widget(self.Fuse5)
        self.layout.add_widget(self.Over_current5)
        self.layout.add_widget(self.Fuse6)
        self.layout.add_widget(self.Over_current6)
        self.layout.add_widget(self.Fuse7)
        self.layout.add_widget(self.Over_current7)
        self.layout.add_widget(self.Fuse8)
        self.layout.add_widget(self.Over_current8)
        self.layout.add_widget(self.Fuse9)
        self.layout.add_widget(self.Over_current9)
        self.layout.add_widget(self.Fuse10)
        self.layout.add_widget(self.Over_current10)

    #Swipe to change screen
    def on_touch_move(self, touch):
        if touch.x > touch.ox and touch.x - touch.ox > 250 :
            Main_App.get_running_app().change_screen(screen_name="About", screen_direction = "right")

        if touch.ox > touch.x and touch.ox - touch.x > 250:
            Main_App.get_running_app().change_screen(screen_name="FocusMain", screen_direction = "left")


#----------------------------------------------------------------------------------------------
#Settings page

#----------------------------------------------------------------------------------------------
#Raw Data page

class Raw_Data_Screen(Screen, FloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

        #Title__________________________________________
        self.Title = Button(
            disabled = True,
            #text settings
            text = "Raw Data",
            font_size = "44sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.4, "y":.85},
            #color settings
            color = (1,1,1,1),
            background_color = (0,0,0,0)
        )
        self.add_widget(self.Title)

        self.layout1()
        self.scroll=ScrollView(size=(Window.width,Window.height))
        self.scroll.do_scroll_y=True
        self.scroll.do_scroll_x=False
        self.scroll.add_widget(self.layout1)
        self.add_widget(self.scroll)

    def layout1(self):
        self.layout1=GridLayout()
        self.layout1.cols=2
        self.layout1.size_hint_x=None
        self.layout1.size_hint_y=5
        #self.layout.height=self.minimum_height
        self.layout1.row_default_height=150
        self.layout1.col_default_width=325
        self.layout1.padding=75
        self.layout1.row_force_default=True

        #Battery Raw__________________________________________
        self.Battery_Raw = Button(
            disabled = True,
            #text settings
            text = "Battery\nRaw : ",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.05, "y":.7},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.Battery_Raw)

        #Battery Raw__________________________________________
        self.Battery_Raw = Button(
            disabled = True,
            #text settings
            text = "Battery\nRaw : ",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.05, "y":.7},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.Battery_Raw)

        #Battery Raw__________________________________________
        self.Battery_Raw = Button(
            disabled = True,
            #text settings
            text = "Battery\nRaw : ",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.05, "y":.7},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.Battery_Raw)

        #Battery Raw__________________________________________
        self.Battery_Raw = Button(
            disabled = True,
            #text settings
            text = "Battery\nRaw : ",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.05, "y":.7},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.Battery_Raw)


    def on_touch_move(self, touch):
        if touch.x > touch.ox and touch.x - touch.ox > 250 :
            Main_App.get_running_app().change_screen(screen_name="IMU", screen_direction = "right")

        if touch.ox > touch.x and touch.ox - touch.x > 250 :
            Main_App.get_running_app().change_screen(screen_name="About", screen_direction = "left")


#----------------------------------------------------------------------------------------------
#Focus Mode 

#Focus Mode Main Screen------------------------------------------------------------------------
class Focus_Main(Screen, FloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

    #Title__________________________________________
        self.Title = Button(
            disabled = True,
            #text settings
            text = "Focus Mode",
            font_size = "54sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.4, "y":.85},
            #color settings
            color = (1,1,1,1),
            background_color = (0,0,0,0)
        )
        self.add_widget(self.Title)

        #-------------------------------------------
        self.toGear = Button(
            #text settings
            text = "    Gear\nIndicator",
            font_size = "44sp",
            bold = True,
            #size and position
            size_hint = (.40,.30),
            pos_hint = {"x":.05, "y":.10},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.toGear)
        self.toGear.bind(on_press=self.gotoFocusGear)

        #-------------------------------------------
        self.toRPM = Button(
            #text settings
            text = "RPM",
            font_size = "44sp",
            bold = True,
            #size and position
            size_hint = (.40,.30),
            pos_hint = {"x":.55, "y":.10},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.toRPM)
        self.toRPM.bind(on_press=self.gotoFocusRPM)

        #-------------------------------------------
        self.toSpeed = Button(
            #text settings
            text = "Speed",
            font_size = "44sp",
            bold = True,
            #size and position
            size_hint = (.40,.30),
            pos_hint = {"x":.05, "y":.47},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.toSpeed)
        self.toSpeed.bind(on_press=self.gotoFocusSpeed)

        #-------------------------------------------
        self.toTB = Button(
            #text settings
            text = "Throttle &\n   Brake",
            font_size = "44sp",
            bold = True,
            #size and position
            size_hint = (.40,.30),
            pos_hint = {"x":.55, "y":.47},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.toTB)
        self.toTB.bind(on_press=self.gotoFocusTB)

    #define functions to bind the buttons
    def gotoFocusGear(instance, value):
         Main_App.get_running_app().change_screen(screen_name="FocusGear", screen_direction = "up")

    def gotoFocusRPM(instance, value):
         Main_App.get_running_app().change_screen(screen_name="FocusRPM", screen_direction = "up")

    def gotoFocusSpeed(instance, value):
         Main_App.get_running_app().change_screen(screen_name="FocusSpeed", screen_direction = "up")

    def gotoFocusTB(instance, value):
         Main_App.get_running_app().change_screen(screen_name="FocusTB", screen_direction = "up")

    #Touch Movement function
    def on_touch_move(self, touch):
        if touch.x > touch.ox and touch.x - touch.ox > 250 :
            Main_App.get_running_app().change_screen(screen_name="Warning", screen_direction = "right")

        if touch.ox > touch.x and touch.ox - touch.x > 250 :
            Main_App.get_running_app().change_screen(screen_name="Main", screen_direction = "left")


#Focus Mode Speed------------------------------------------------------------------------
class Focus_Speed(Screen, FloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

    #Speed__________________________________________
        self.Speed = Button(
            disabled = True,
            #text settings
            text = "Speed",
            font_size = "200sp",
            bold = True,
            #size and position
            size_hint = (1, 1),
            pos_hint = {"x":.0, "y":.0},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.Speed)

    #Switch to main screen
    def on_touch_move(self, touch):
        if touch.oy > touch.y and touch.oy - touch.y > 250 :
            Main_App.get_running_app().change_screen(screen_name="FocusMain", screen_direction = "down")


#Focus Mode Gear------------------------------------------------------------------------
class Focus_Gear(Screen, FloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

    #Gear__________________________________________
        self.Gear = Button(
            disabled = True,
            #text settings
            text = "Gear",
            font_size = "200sp",
            bold = True,
            #size and position
            size_hint = (1, 1),
            pos_hint = {"x":.0, "y":.0},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.Gear)

    #Switch to main screen
    def on_touch_move(self, touch):
        if touch.oy > touch.y and touch.oy - touch.y > 250 :
            Main_App.get_running_app().change_screen(screen_name="FocusMain", screen_direction = "down")


#Focus Mode RPM------------------------------------------------------------------------
class Focus_RPM(Screen, FloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

    #RPM__________________________________________
        self.RPM = Button(
            disabled = True,
            #text settings
            text = "RPM",
            font_size = "200sp",
            bold = True,
            #size and position
            size_hint = (1, 1),
            pos_hint = {"x":.0, "y":.0},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.RPM)

    #Switch to main screen
    def on_touch_move(self, touch):
        if touch.oy > touch.y and touch.oy - touch.y > 250 :
            Main_App.get_running_app().change_screen(screen_name="FocusMain", screen_direction = "down")


#Focus Mode ThrottleBrake------------------------------------------------------------------------
class Focus_ThrottleBrake(Screen, FloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

    #RPM__________________________________________
        self.RPM = Button(
            disabled = True,
            #text settings
            text = "T  |  B",
            font_size = "200sp",
            bold = True,
            #size and position
            size_hint = (1, 1),
            pos_hint = {"x":.0, "y":.0},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.RPM)

    #Switch to main screen
    def on_touch_move(self, touch):
        if touch.oy > touch.y and touch.oy - touch.y > 250 :
            Main_App.get_running_app().change_screen(screen_name="FocusMain", screen_direction = "down")


#----------------------------------------------------------------------------------------------
#Welcome page

class Welcome_Screen(Screen,FloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.welcome_gif = Image(
            source = "entry.gif",
            anim_delay = 0.03
        )

        self.add_widget(self.welcome_gif)

        Clock.schedule_once(self.switch_to_main, 2)

    #Switch to main screen
    def switch_to_main(self, *args):
        Main_App.get_running_app().change_screen(screen_name = "Main", screen_direction = "up")



#----------------------------------------------------------------------------------------------
#About page

class About_Screen(Screen, FloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

        #Background Image__________________________________
        self.background_img = Image(
            source = "vr_logo.png",   #PNG Only
            #size and position
            size_hint = (1,.80),
            pos_hint = {"x":.0, "y":.2},
        )
        self.add_widget(self.background_img)

        #About__________________________________________
        self.About = Button(
            disabled = True,
            #text settings
            text = f"VR 10.0\n2022-23\nversion : {version_info}\n last update : {last_update}",
            font_size = "18sp",
            bold = True,
            #size and position
            size_hint = (1,.50),
            pos_hint = {"x":.0, "y":.0},
            #color settings
            color = (1,1,1,1),
            background_color = (0,0,0,0)
        )
        self.add_widget(self.About)

    def on_touch_move(self, touch):
        if touch.x > touch.ox and touch.x - touch.ox > 250 :
            Main_App.get_running_app().change_screen(screen_name="Raw", screen_direction = "right")

        if touch.ox > touch.x and touch.ox - touch.x > 250 :
            Main_App.get_running_app().change_screen(screen_name="Warning", screen_direction = "left")


#////////////////////////////////////////////////////////////
## Main Class
class Main_App(App):

    def build(self):

        #Creating Screen manager and declaring screens
        self.Screen_Manager = ScreenManager(transition = SlideTransition())
        self.Screen_Manager.add_widget(Welcome_Screen(name = 'Welcome'))
        self.Screen_Manager.add_widget(Main_Screen(name = 'Main'))
        self.Screen_Manager.add_widget(IMU_Screen(name = 'IMU'))
        self.Screen_Manager.add_widget(Raw_Data_Screen(name = 'Raw'))
        self.Screen_Manager.add_widget(About_Screen(name = 'About'))
        self.Screen_Manager.add_widget(Focus_Main(name = 'FocusMain'))
        self.Screen_Manager.add_widget(Focus_Gear(name = 'FocusGear'))
        self.Screen_Manager.add_widget(Focus_RPM(name = 'FocusRPM'))
        self.Screen_Manager.add_widget(Focus_Speed(name = 'FocusSpeed'))
        self.Screen_Manager.add_widget(Focus_ThrottleBrake(name = 'FocusTB'))
        self.Screen_Manager.add_widget(Warnings_Screen(name = 'Warning'))
        return self.Screen_Manager

    #Function to change screen, call in classes
    def change_screen(self, screen_name, screen_direction):
        self.Screen_Manager.current = screen_name
        self.Screen_Manager.transition.direction = screen_direction

    #Swipe gesture
    #Swipe to change screen
    def on_touch_move(self, touch):
        if touch.x > touch.ox and touch.x - touch.ox > 250 :
            Main_App.get_running_app().change_screen(screen_name="FocusMain", screen_direction = "right")

        if touch.ox > touch.x and touch.ox - touch.x > 250:
            Main_App.get_running_app().change_screen(screen_name="IMU", screen_direction = "left")


#----------------------------------------------------------------------------------------------
#IMU page

class IMU_Screen(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Background Image__________________________________
        self.background_img = Image(
            source = "IMU.png"    #PNG Only
        )
        self.add_widget(self.background_img)

        #Front Left Tyre____________________________________
        self.Left_Front = Button(
            disabled = True,
            #text settings
            text = "48  58\n58  55\n22  32",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.20,.20),
            pos_hint = {"x":.10, "y":.55},
            #color settings
            color = (1,1,1,1),
            background_color = (255,255,255,0)
        )

        self.add_widget(self.Left_Front)

        #Front Right Tyre___________________________________
        self.Right_Front = Button(
            disabled = True,
            #text settings
            text = "48  58\n58  55\n22  32",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.20,.20),
            pos_hint = {"x":.68, "y":.55},
            #color settings
            color = (1,1,1,1),
            background_color = (255,255,255,0)
        )

        self.add_widget(self.Right_Front)

        #Rear Left Tyre_____________________________________
        self.Left_Rear = Button(
            disabled = True,
            #text settings
            text = "48  58\n58  55\n22  32",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.20,.20),
            pos_hint = {"x":.03, "y":.2},
            #color settings
            color = (1,1,1,1),
            background_color = (255,255,255,0)
        )

        self.add_widget(self.Left_Rear)

        #Rear Right Tyre____________________________________
        self.Rear_Right = Button(
            disabled = True,
            #text settings
            text = "48  58\n58  55\n22  32",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.20,.20),
            pos_hint = {"x":.76, "y":.2},
            #color settings
            color = (1,1,1,1),
            background_color = (255,255,255,0)
        )

        self.add_widget(self.Rear_Right)

        #Title____________________________________
        self.Title = Button(
            disabled = True,
            #text settings
            text = "IMU",
            font_size = "36sp",
            bold = True,
            #size and position
            size_hint = (.30,.30),
            pos_hint = {"x":.35, "y":.78 },
            #color settings
            color = (1,1,1,1),
            background_color = (255,255,255,0)
        )

        self.add_widget(self.Title)

        #Calibrate____________________________________
        # self.Calibrate_Button = Button(
        #     #text settings
        #     text = "Calibrate",
        #     font_size = "24sp",
        #     bold = True,
        #     #size and position
        #     size_hint = (.20,.10),
        #     pos_hint = {"x":.40, "y":.05},
        #     #color settings
        #     color = (0,0,0,1),
        #     background_color = (255,255,255,1)

        #     #########LOGIC!!!!!!##########
        # )

        # self.add_widget(self.Calibrate_Button)

    #Swipe to change screen
    def on_touch_move(self, touch):
        if touch.x > touch.ox and touch.x - touch.ox > 250 :
            Main_App.get_running_app().change_screen(screen_name="Main", screen_direction = "right")

        if touch.ox > touch.x and touch.ox - touch.x > 250:
            Main_App.get_running_app().change_screen(screen_name="Raw", screen_direction = "left")

#----------------------------------------------------------------------------------------------
#Warnings page

class Warnings_Screen(Screen, FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Float for Title
        #Title__________________________________________
        self.Title = Button(
            disabled = True,
            #text settings
            text = "Warnings",
            font_size = "44sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.4, "y":.87},
            #color settings
            color = (1,1,1,1),
            background_color = (0,0,0,0)
        )

        self.add_widget(self.Title)

        self.layout()
        self.scroll=ScrollView(size=(Window.width,Window.height))
        self.scroll.do_scroll_y=True
        self.scroll.do_scroll_x=False
        self.scroll.add_widget(self.layout)
        self.add_widget(self.scroll)

    def layout(self):
        self.layout=GridLayout()
        self.layout.cols=2
        #self.layout.bind(minimum_height=self.layout.setter("height"))
        self.layout.size_hint_x=None
        self.layout.size_hint_y=5
        #self.layout.height=self.minimum_height
        self.layout.row_default_height=125
        self.layout.col_default_width=325
        self.layout.padding=75
        self.layout.row_force_default=True

        #PDB_Disconnected_________________________________________________
        self.PDB_Disconnected = Button(
            disabled = True,
            #text settings
            text = "         PDB \n Disconnected",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #PDB_Temperature_Warning_________________________________________________
        self.PDB_Temperature_Warning = Button(
            disabled = True,
            #text settings
            text = "PDB Temperature\n            High",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Main_Path_break______________________________
        self.Main_path_break = Button(
            disabled = True,
            #text settings
            text = "Main path \n    Break",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Gearbox_sensor_error_______________________________________________
        self.Gearbox_sensor = Button(
            disabled = True,
            #text settings
            text = "Gearbox Sensor\n          Error",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Battery_Voltage______________________________________________________
        self.Battery_Voltage = Button(
            disabled = True,
            #text settings
            text = "Battery Voltage\n          Low",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Battery_Disconnected________________________________________________
        self.Battery_Disconnected = Button(
            disabled = True,
            #text settings
            text = "Battery Sensor\n Disconnected",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Engine_Temperature_Disconnected_________________________________________________
        self.Engine_Temperature_Warning = Button(
            disabled = True,
            #text settings
            text = "Engine Temperature\n             Sensor \n      Disconnected",
            font_size = "34sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Engine_Temperature_High_________________________________________________
        self.Engine_Temperature_High = Button(
            disabled = True,
            #text settings
            text = "Engine Temperature\n              High",
            font_size = "34sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse1_____________________________________________________________
        self.Fuse1 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 1",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current____________________________________________________
        self.Over_current = Button(
            disabled = True,
            #text settings
            text = "Over current - 1",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse2_____________________________________________________________
        self.Fuse2 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 2",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current2____________________________________________________
        self.Over_current2 = Button(
            disabled = True,
            #text settings
            text = "Over current - 2",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse3_____________________________________________________________
        self.Fuse3 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 3",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_curren3____________________________________________________
        self.Over_current3 = Button(
            disabled = True,
            #text settings
            text = "Over current - 3",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse4_____________________________________________________________
        self.Fuse4 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 4",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current4____________________________________________________
        self.Over_current4 = Button(
            disabled = True,
            #text settings
            text = "Over current - 4",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse5_____________________________________________________________
        self.Fuse5 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 5",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current5____________________________________________________
        self.Over_current5 = Button(
            disabled = True,
            #text settings
            text = "Over current - 5",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse6_____________________________________________________________
        self.Fuse6 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 6",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current6____________________________________________________
        self.Over_current6 = Button(
            disabled = True,
            #text settings
            text = "Over current - 6",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse7_____________________________________________________________
        self.Fuse7 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 7",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current7____________________________________________________
        self.Over_current7 = Button(
            disabled = True,
            #text settings
            text = "Over current - 7",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse8_____________________________________________________________
        self.Fuse8 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 8",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current8____________________________________________________
        self.Over_current8 = Button(
            disabled = True,
            #text settings
            text = "Over current - 8",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse9_____________________________________________________________
        self.Fuse9 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 9",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current9____________________________________________________
        self.Over_current9 = Button(
            disabled = True,
            #text settings
            text = "Over current - 9",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Fuse10_____________________________________________________________
        self.Fuse10 = Button(
            disabled = True,
            #text settings
            text = "Fuse - 10",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        #Over_current10____________________________________________________
        self.Over_current10 = Button(
            disabled = True,
            #text settings
            text = "Over current - 10",
            font_size = "36sp",
            bold = True,
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )

        self.layout.add_widget(self.PDB_Disconnected)
        self.layout.add_widget(self.Main_path_break)
        self.layout.add_widget(self.PDB_Temperature_Warning)
        self.layout.add_widget(self.Gearbox_sensor)
        self.layout.add_widget(self.Battery_Voltage)
        self.layout.add_widget(self.Battery_Disconnected)
        self.layout.add_widget(self.Engine_Temperature_Warning)
        self.layout.add_widget(self.Engine_Temperature_High)

        self.layout.add_widget(self.Fuse1)
        self.layout.add_widget(self.Over_current)
        self.layout.add_widget(self.Fuse2)
        self.layout.add_widget(self.Over_current2)
        self.layout.add_widget(self.Fuse3)
        self.layout.add_widget(self.Over_current3)
        self.layout.add_widget(self.Fuse4)
        self.layout.add_widget(self.Over_current4)
        self.layout.add_widget(self.Fuse5)
        self.layout.add_widget(self.Over_current5)
        self.layout.add_widget(self.Fuse6)
        self.layout.add_widget(self.Over_current6)
        self.layout.add_widget(self.Fuse7)
        self.layout.add_widget(self.Over_current7)
        self.layout.add_widget(self.Fuse8)
        self.layout.add_widget(self.Over_current8)
        self.layout.add_widget(self.Fuse9)
        self.layout.add_widget(self.Over_current9)
        self.layout.add_widget(self.Fuse10)
        self.layout.add_widget(self.Over_current10)
    
    #Swipe to change screen
    def on_touch_move(self, touch):
        if touch.x > touch.ox and touch.x - touch.ox > 250 :
            Main_App.get_running_app().change_screen(screen_name="Settings", screen_direction = "right")

        if touch.ox > touch.x and touch.ox - touch.x > 250:
            Main_App.get_running_app().change_screen(screen_name="FocusMain", screen_direction = "left")


#----------------------------------------------------------------------------------------------
#Settings page 

class Settings_Screen(Screen, FloatLayout):
                                                                                                           
    def __init__(self, **kw):
        super().__init__(**kw)

        #Background__________________________________________
        self.Background = Button(
            disabled = True,
            #size and position
            size_hint = (1, 1),
            pos_hint = {"x":.0, "y":.0},
            #color settings
            color = (1,1,1,1),
            background_color = (255,255,255,255)
        )
        self.add_widget(self.Background)

        #Title__________________________________________
        self.Title = Button(
            disabled = True,
            #text settings 1
            text = "Settings",
            font_size = "44sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.4, "y":.87},
            #color settings
            color = (0,0,0,1),
            background_color = (0,0,0,0)
        )
        self.add_widget(self.Title)

        #SubTitle__________________________________________
        self.SubTitle = Button(
            disabled = True,
            #text settings 1
            text = ">> Shifter Leds",
            font_size = "30sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.08, "y":.72},
            #color settings
            color = (0,0,0,1),
            background_color = (0,0,0,0)
        )
        self.add_widget(self.SubTitle)

        #RPM Mode 1__________________________________________
        self.RPMM1 = Button(
            #disabled = True,
            #text settings
            text = "Linear Map",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.1, "y":.55},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.RPMM1)

        #RPM Mode 2__________________________________________
        self.RPMM2 = Button(
            #disabled = True,
            #text settings
            text = "Partial Map",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.4, "y":.55},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.RPMM2)

        #RPM Mode 3__________________________________________
        self.RPMM3 = Button(
            #disabled = True,
            #text settings
            text = "OFF",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.7, "y":.55},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.RPMM3)

        #LowerRPM__________________________________________
        self.LowerRPM = Button(
            disabled = True,
            #text settings 1
            text = "> Lower RPM",
            font_size = "26sp",
            bold = True,
            #size and position
            size_hint = (.20,.1),
            pos_hint = {"x":.15, "y":.35},
            #color settings
            color = (0,0,0,1),
            background_color = (0,0,0,0)
        )
        self.add_widget(self.LowerRPM)

        #Slider1________________________________________________
        self.Slider_1 = Slider(
            min=0, 
            max=10000, 
            step=500,
            value_track=True, 
            value_track_color=[1, 0, 0, 1],
            cursor_height = '64sp',
            cursor_width = '64sp',
            padding = '256sp',
            sensitivity = 'handle',
            pos_hint = {"x":-.25, "y":-.20} #from centre so use -ve
            )

        self.add_widget(self.Slider_1)
        self.Slider_1.bind(value = self.OnSlider1)

        #HigherRPM__________________________________________
        self.HigherRPM = Button(
            disabled = True,
            #text settings 1
            text = "> Higher RPM",
            font_size = "26sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.65, "y":.35},
            #color settings
            color = (0,0,0,1),
            background_color = (0,0,0,0)
        )
        self.add_widget(self.HigherRPM)

        #Slider2________________________________________________
        self.Slider_2 = Slider(
            min=0, 
            max=10000, 
            step=500,
            value_track=True, 
            value_track_color=[1, 0, 0, 1],
            cursor_height = '64sp',
            cursor_width = '64sp',
            padding = '256sp',
            sensitivity = 'handle',
            pos_hint = {"x":.25, "y":-.20} #from centre so use -ve
            )

        self.add_widget(self.Slider_2)
        self.Slider_2.bind(value = self.OnSlider2)

        #Brightness Control Button__________________________________________
        self.Brightness_Button = Button(
            #disabled = True,
            #text settings
            text = "Brightness",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.25, "y":.05},
            #color settings
            color = (0,0,0,1),
            background_color = (0,0,255,255)
        )
        self.add_widget(self.Brightness_Button)
        self.Brightness_Button.bind(on_press=self.gotoBrightness)

        #Exit Button__________________________________________
        self.Exit_Button = Button(
            #disabled = True,
            #text settings
            text = "Exit Dash",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.55, "y":.05},
            #color settings
            color = (0,0,0,1),
            background_color = (0,0,255,255)
        )
        self.add_widget(self.Exit_Button)
        self.Exit_Button.bind(on_press=self.gotoExit)

    #define functions to bind the buttons
    def gotoBrightness(instance, value):
         Main_App.get_running_app().change_screen(screen_name="Brightness", screen_direction = "up")

    def gotoExit(instance, value):
        Main_App().stop()

    def OnSlider1(self, instance, slider_value):
            # print("Slider value is ",int(slider_value))
            # print(self.Slider_1.value)
            # if self.Slider_1.value == 0:
            #     pass
            self.LowerRPM.text = f"> Lower RPM : {int(self.Slider_1.value)}"

    def OnSlider2(self, instance, slider_value):
            #print("Slider value is ",int(slider_value))
            #print(self.Slider_1.value)
            # if self.Slider_2.value == 0:
            #     pass
            self.HigherRPM.text = f"> Higher RPM : {int(self.Slider_2.value)}"

    #Swipe gesture
    #Swipe to change screen
    def on_touch_move(self, touch):
        if touch.x > touch.ox and touch.x - touch.ox > 500 :
            Main_App.get_running_app().change_screen(screen_name="About", screen_direction = "right")

        if touch.ox > touch.x and touch.ox - touch.x > 500:
            Main_App.get_running_app().change_screen(screen_name="Warning", screen_direction = "left")


#----------------------------------------------------------------------------------------------
#Brightness page 

class Brightness_Screen(Screen, FloatLayout):
                                                                                                           
    def __init__(self, **kw):
        super().__init__(**kw)

        #Background__________________________________________
        self.Background = Button(
            disabled = True,
            #size and position
            size_hint = (1, 1),
            pos_hint = {"x":.0, "y":.0},
            #color settings
            color = (1,1,1,1),
            background_color = (255,255,255,255)
        )
        self.add_widget(self.Background)

        #Title__________________________________________
        self.Title = Button(
            disabled = True,
            #text settings 1
            text = "Brightness",
            font_size = "44sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.4, "y":.87},
            #color settings
            color = (0,0,0,1),
            background_color = (0,0,0,0)
        )
        self.add_widget(self.Title)

        #Screen Brightness__________________________________________
        self.Screen = Button(
            disabled = True,
            #text settings 1
            text = "Screen",
            font_size = "26sp",
            bold = True,
            #size and position
            size_hint = (.20,.1),
            pos_hint = {"x":.15, "y":.55},
            #color settings
            color = (0,0,0,1),
            background_color = (0,0,0,0)
        )
        self.add_widget(self.Screen)

        #Slider1________________________________________________
        self.Slider_1 = Slider(
            min=0, 
            max=100, 
            step=10,
            value_track=True, 
            value_track_color=[1, 0, 0, 1],
            cursor_height = '64sp',
            cursor_width = '64sp',
            padding = '256sp',
            sensitivity = 'handle',
            pos_hint = {"x":-.25, "y":-.10} #from centre so use -ve
            )

        self.add_widget(self.Slider_1)
        self.Slider_1.bind(value = self.OnSlider1)

        #Led__________________________________________
        self.Led = Button(
            disabled = True,
            #text settings 1
            text = "Shifter Led",
            font_size = "26sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.65, "y":.55},
            #color settings
            color = (0,0,0,1),
            background_color = (0,0,0,0)
        )
        self.add_widget(self.Led)

        #Slider2________________________________________________
        self.Slider_2 = Slider(
            min=0, 
            max=100, 
            step=10,
            value_track=True, 
            value_track_color=[1, 0, 0, 1],
            cursor_height = '64sp',
            cursor_width = '64sp',
            padding = '256sp',
            sensitivity = 'handle',
            pos_hint = {"x":.25, "y":-.10} #from centre so use -ve
            )

        self.add_widget(self.Slider_2)
        self.Slider_2.bind(value = self.OnSlider2)

        #Save Button__________________________________________
        self.Save_Button = Button(
            #disabled = True,
            #text settings
            text = "Save",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.40, "y":.05},
            #color settings
            color = (0,0,0,1),
            background_color = (0,255,0,255)
        )
        self.add_widget(self.Save_Button)
        self.Save_Button.bind(on_press=self.gotoBack)

    def gotoBack(instance, value):
         Main_App.get_running_app().change_screen(screen_name="Settings", screen_direction = "down")

    def OnSlider1(self, instance, slider_value):
            # print("Slider value is ",int(slider_value))
            # print(self.Slider_1.value)
            # if self.Slider_1.value == 0:
            #     pass
            self.Screen.text = f"> Screen : {int(self.Slider_1.value)}"
            sbc.set_brightness(int(self.Slider_1.value))

    def OnSlider2(self, instance, slider_value):
            #print("Slider value is ",int(slider_value))
            #print(self.Slider_1.value)
            # if self.Slider_2.value == 0:
            #     pass
            self.Led.text = f"> Shifter Led : {int(self.Slider_2.value)}"

#----------------------------------------------------------------------------------------------
#Raw Data page

class Raw_Data_Screen(Screen, FloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

        #Title__________________________________________
        self.Title = Button(
            disabled = True,
            #text settings 1
            text = "Raw Data",
            font_size = "44sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.4, "y":.87},
            #color settings
            color = (1,1,1,1),
            background_color = (0,0,0,0)
        )
        self.add_widget(self.Title)

        self.layout1()
        self.scroll=ScrollView(size=(Window.width,Window.height))
        self.scroll.do_scroll_y=True
        self.scroll.do_scroll_x=False
        self.scroll.add_widget(self.layout1)
        self.add_widget(self.scroll)

    def layout1(self):
        self.layout1=GridLayout()
        self.layout1.cols=2
        self.layout1.size_hint_x=None
        self.layout1.size_hint_y=5
        #self.layout.height=self.minimum_height
        self.layout1.row_default_height=150
        self.layout1.col_default_width=325
        self.layout1.padding=75
        self.layout1.row_force_default=True

        #Battery Raw__________________________________________
        self.Battery = Button(
            disabled = True,
            #text settings
            text = "Battery : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.Battery)

        #Throttle__________________________________________
        self.Throttle = Button(
            disabled = True,
            #text settings
            text = "Throttle : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.Throttle)

        #WheelSpeed__________________________________________
        self.WheelSpeed = Button(
            disabled = True,
            #text settings
            text = "Wheel Speed : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.WheelSpeed)

        #RPM__________________________________________
        self.RPM = Button(
            disabled = True,
            #text settings
            text = "RPM : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.RPM)

        #Brake Presuure__________________________________________
        self.BrakePressure = Button(
            disabled = True,
            #text settings
            text = "Brake Pressure : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.BrakePressure)

        #Engine Temp__________________________________________
        self.EngineTemp = Button(
            disabled = True,
            #text settings
            text = "Engine Temp : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.EngineTemp)

        #Gear1__________________________________________
        self.Gear1 = Button(
            disabled = True,
            #text settings
            text = "Gear1 : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.Gear1)

        #Gear2__________________________________________
        self.Gear2 = Button(
            disabled = True,
            #text settings
            text = "Gear2 : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.Gear2)

        #Gear3__________________________________________
        self.Gear3 = Button(
            disabled = True,
            #text settings
            text = "Gear3 : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.Gear3)

        #Gear4__________________________________________
        self.Gear4 = Button(
            disabled = True,
            #text settings
            text = "Gear4 : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.Gear4)

        #Gear5__________________________________________
        self.Gear5 = Button(
            disabled = True,
            #text settings
            text = "Gear5 : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.Gear5)

        #GearN__________________________________________
        self.GearN = Button(
            disabled = True,
            #text settings
            text = "GearN : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.GearN)

        #IMU1__________________________________________
        self.IMU1 = Button(
            disabled = True,
            #text settings
            text = "IMU1 : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.IMU1)

        #IMU2__________________________________________
        self.IMU2 = Button(
            disabled = True,
            #text settings
            text = "IMU2 : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.IMU2)

        #IMU3__________________________________________
        self.IMU3 = Button(
            disabled = True,
            #text settings
            text = "IMU3 : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.IMU3)

        #IMU4__________________________________________
        self.IMU4 = Button(
            disabled = True,
            #text settings
            text = "IMU4 : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.IMU4)

        #Damper1__________________________________________
        self.Damper1 = Button(
            disabled = True,
            #text settings
            text = "Damper1 : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.Damper1)

        #Damper2__________________________________________
        self.Damper2 = Button(
            disabled = True,
            #text settings
            text = "Damper2 : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.Damper2)

        #Damper3__________________________________________
        self.Damper3 = Button(
            disabled = True,
            #text settings
            text = "Damper3 : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.Damper3)

        #Damper4__________________________________________
        self.Damper4 = Button(
            disabled = True,
            #text settings
            text = "Damper4 : ",
            font_size = "40sp",
            bold = True,
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.layout1.add_widget(self.Damper4)
        
    def on_touch_move(self, touch):
        if touch.x > touch.ox and touch.x - touch.ox > 250 :
            Main_App.get_running_app().change_screen(screen_name="IMU", screen_direction = "right")

        if touch.ox > touch.x and touch.ox - touch.x > 250 :
            Main_App.get_running_app().change_screen(screen_name="About", screen_direction = "left")


#----------------------------------------------------------------------------------------------
#Focus Mode 

#Focus Mode Main Screen------------------------------------------------------------------------
class Focus_Main(Screen, FloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

    #Title__________________________________________
        self.Title = Button(
            disabled = True,
            #text settings
            text = "Focus Mode",
            font_size = "54sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.4, "y":.85},
            #color settings
            color = (1,1,1,1),
            background_color = (0,0,0,0)
        )
        self.add_widget(self.Title)

        #-------------------------------------------
        self.toGear = Button(
            #text settings
            text = "    Gear\nIndicator",
            font_size = "38sp",
            bold = True,
            #size and position
            size_hint = (.30,.20),
            pos_hint = {"x":.10, "y":.10},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.toGear)
        self.toGear.bind(on_press=self.gotoFocusGear)

        #-------------------------------------------
        self.toRPM = Button(
            #text settings
            text = "RPM",
            font_size = "38sp",
            bold = True,
            #size and position
            size_hint = (.30,.20),
            pos_hint = {"x":.60, "y":.55},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.toRPM)
        self.toRPM.bind(on_press=self.gotoFocusRPM)

        #-------------------------------------------
        self.toSpeed = Button(
            #text settings
            text = "Speed",
            font_size = "38sp",
            bold = True,
            #size and position
            size_hint = (.30,.20),
            pos_hint = {"x":.10, "y":.55},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.toSpeed)
        self.toSpeed.bind(on_press=self.gotoFocusSpeed)

        #-------------------------------------------
        self.toTB = Button(
            #text settings
            text = "Throttle &\n   Brake",
            font_size = "38sp",
            bold = True,
            #size and position
            size_hint = (.30,.20),
            pos_hint = {"x":.60, "y":.10},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.toTB)
        self.toTB.bind(on_press=self.gotoFocusTB)

    #define functions to bind the buttons
    def gotoFocusGear(instance, value):
         Main_App.get_running_app().change_screen(screen_name="FocusGear", screen_direction = "up")

    def gotoFocusRPM(instance, value):
         Main_App.get_running_app().change_screen(screen_name="FocusRPM", screen_direction = "up")

    def gotoFocusSpeed(instance, value):
         Main_App.get_running_app().change_screen(screen_name="FocusSpeed", screen_direction = "up")

    def gotoFocusTB(instance, value):
         Main_App.get_running_app().change_screen(screen_name="FocusTB", screen_direction = "up")

    #Touch Movement function
    def on_touch_move(self, touch):
        if touch.x > touch.ox and touch.x - touch.ox > 250 :
            Main_App.get_running_app().change_screen(screen_name="Warning", screen_direction = "right")

        if touch.ox > touch.x and touch.ox - touch.x > 250 :
            Main_App.get_running_app().change_screen(screen_name="Main", screen_direction = "left")


#Focus Mode Speed------------------------------------------------------------------------
class Focus_Speed(Screen, FloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

    #Speed__________________________________________
        self.Speed = Button(
            disabled = True,
            #text settings
            text = "Speed",
            font_size = "200sp",
            bold = True,
            #size and position
            size_hint = (1, 1),
            pos_hint = {"x":.0, "y":.0},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.Speed)

    #Switch to main screen
    def on_touch_move(self, touch):
        if touch.oy > touch.y and touch.oy - touch.y > 250 :
            Main_App.get_running_app().change_screen(screen_name="FocusMain", screen_direction = "down")


#Focus Mode Gear------------------------------------------------------------------------
class Focus_Gear(Screen, FloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

    #Gear__________________________________________
        self.Gear = Button(
            disabled = True,
            #text settings
            text = "Gear",
            font_size = "200sp",
            bold = True,
            #size and position
            size_hint = (1, 1),
            pos_hint = {"x":.0, "y":.0},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.Gear)

    #Switch to main screen
    def on_touch_move(self, touch):
        if touch.oy > touch.y and touch.oy - touch.y > 250 :
            Main_App.get_running_app().change_screen(screen_name="FocusMain", screen_direction = "down")


#Focus Mode RPM------------------------------------------------------------------------
class Focus_RPM(Screen, FloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

    #RPM__________________________________________
        self.RPM = Button(
            disabled = True,
            #text settings
            text = "RPM",
            font_size = "200sp",
            bold = True,
            #size and position
            size_hint = (1, 1),
            pos_hint = {"x":.0, "y":.0},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.RPM)

    #Switch to main screen
    def on_touch_move(self, touch):
        if touch.oy > touch.y and touch.oy - touch.y > 250 :
            Main_App.get_running_app().change_screen(screen_name="FocusMain", screen_direction = "down")


#Focus Mode ThrottleBrake------------------------------------------------------------------------
class Focus_ThrottleBrake(Screen, FloatLayout):

    def __init__(self, **kw):
        super().__init__(**kw)

    #RPM__________________________________________
        self.RPM = Button(
            disabled = True,
            #text settings
            text = "T  |  B",
            font_size = "200sp",
            bold = True,
            #size and position
            size_hint = (1, 1),
            pos_hint = {"x":.0, "y":.0},
            #color settings
            color = (1,1,1,1),
            background_color = (255,0,0,255)
        )
        self.add_widget(self.RPM)

    #Switch to main screen
    def on_touch_move(self, touch):
        if touch.oy > touch.y and touch.oy - touch.y > 250 :
            Main_App.get_running_app().change_screen(screen_name="FocusMain", screen_direction = "down")


#----------------------------------------------------------------------------------------------
#Welcome page

class Welcome_Screen(Screen,FloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.welcome_gif = Image(
            source = "entry.gif",
            anim_delay = 0.03
        )

        self.add_widget(self.welcome_gif)

        Clock.schedule_once(self.switch_to_main, 7)
        
    #Switch to main screen
    def switch_to_main(self, *args):
        Main_App.get_running_app().change_screen(screen_name = "Main", screen_direction = "up")



#----------------------------------------------------------------------------------------------
#About page

class About_Screen(Screen, FloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

        #Background Image__________________________________
        self.background_img = Image(
            source = "vr_logo.png",   #PNG Only
            #size and position
            size_hint = (1,.80),
            pos_hint = {"x":.0, "y":.2},
        )
        self.add_widget(self.background_img)

        #About__________________________________________
        self.About = Button(
            disabled = True,
            #text settings
            text = f"                VR 10.0\n               2022-23\n         version : {version_info}\n last update : {last_update}",
            font_size = "18sp",
            bold = True,
            #size and position
            size_hint = (1,.50),
            pos_hint = {"x":.0, "y":.0},
            #color settings
            color = (1,1,1,1),
            background_color = (0,0,0,0)
        )
        self.add_widget(self.About)

    def on_touch_move(self, touch):
        if touch.x > touch.ox and touch.x - touch.ox > 250 :
            Main_App.get_running_app().change_screen(screen_name="Raw", screen_direction = "right")

        if touch.ox > touch.x and touch.ox - touch.x > 250 :
            Main_App.get_running_app().change_screen(screen_name="Settings", screen_direction = "left")


#////////////////////////////////////////////////////////////
## Main Class
class Main_App(App):

    def build(self):
        
        #Creating Screen manager and declaring screens
        self.Screen_Manager = ScreenManager(transition = SlideTransition())
        self.Screen_Manager.add_widget(Welcome_Screen(name = 'Welcome'))
        self.Screen_Manager.add_widget(Main_Screen(name = 'Main'))
        self.Screen_Manager.add_widget(IMU_Screen(name = 'IMU'))
        self.Screen_Manager.add_widget(Raw_Data_Screen(name = 'Raw'))
        self.Screen_Manager.add_widget(Settings_Screen(name= 'Settings'))
        self.Screen_Manager.add_widget(About_Screen(name = 'About'))
        self.Screen_Manager.add_widget(Focus_Main(name = 'FocusMain'))
        self.Screen_Manager.add_widget(Focus_Gear(name = 'FocusGear'))
        self.Screen_Manager.add_widget(Focus_RPM(name = 'FocusRPM'))
        self.Screen_Manager.add_widget(Focus_Speed(name = 'FocusSpeed'))
        self.Screen_Manager.add_widget(Focus_ThrottleBrake(name = 'FocusTB'))
        self.Screen_Manager.add_widget(Warnings_Screen(name = 'Warning'))
        self.Screen_Manager.add_widget(Brightness_Screen(name = 'Brightness'))
        return self.Screen_Manager

    #Function to change screen, call in classes
    def change_screen(self, screen_name, screen_direction):
        self.Screen_Manager.current = screen_name
        self.Screen_Manager.transition.direction = screen_direction

#Run the Main App
Main_App().run()

#////////////////////////////////////////////////////////////

