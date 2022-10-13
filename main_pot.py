'''
VR Dashboard V 1.0
last update 7/3/22                
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
#from kivy.uix.label import Label
#from kivy.lang import Builder

import  smbus
bus= smbus.SMBus(1)

#////////////////////////////////////////////////////////////
#Setting Resolution and Background Colour
from kivy.config import Config
from kivy.core.window import Window
#Config.set('graphics', 'resizable', '0')
#Config.set("graphics", "show_cursor", '0')
#Set it to a tuple with the (width, height) in Pixels
Window.size = (800, 480)


#Window.clearcolor = (255, 255, 255, 1)

#////////////////////////////////////////////////////////////
#Global Parameters

#General
page_number = 1

#About Page
version_info = 0
last_update = 0 #ddmmyy

#Main Page
engine_rpm = 0
battery_voltage = 0
throttle_raw = 0
throttle = 0 #in percentage
wheel_speed = 0
gear_position = 0
engine_temp = 0
brake_pressure = 95 #in percentage

#////////////////////////////////////////////////////////////
#Page Number code



#////////////////////////////////////////////////////////////
##GUI
#Main Page
class Main_Screen(Screen,FloatLayout):

    def Pot_data(self,*a):
        
        throttle_raw = bus.read_byte(0x48)
        throttle = throttle_raw * 0.392156
        self.Throttle.text = str(int(throttle))

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

        Clock.schedule_once(self.Pot_data, 0.1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #RPM__________________________________________
        self.RPM = Button(
            disabled = True,
            #text settings
            text = "RPM",
            font_size = "20sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.0, "y":.9},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.add_widget(self.RPM)

        #Battery Voltage______________________________
        self.Battery_Voltage = Button(
            disabled = True,
            #text settings
            text = "14.4V",
            font_size = "20sp",
            bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.10, "y":.0},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.add_widget(self.Battery_Voltage)

        #Throttle_____________________________________
        self.Throttle = Button(
            disabled = True,
            #text settings
            text = "Throttle",
            font_size = "20sp",
            bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.9, "y":.9},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.add_widget(self.Throttle)

        #Brake Pressure______________________________
        self.Brake_Pressure = Button(
            disabled = True,
            #text settings
            text = "Brake",
            font_size = "20sp",
            bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.9, "y":.0},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.add_widget(self.Brake_Pressure)

        #Wheel Speed___________________________________
        self.Wheel_Speed = Button(
            disabled = True,
            #text settings
            text = "123",
            font_size = "192sp",
            bold = True,
            #size and position
            size_hint = (.50,.80),
            pos_hint = {"x":.0, "y":.1},
            #color settings
            color = (1,1,1,1),
            background_color = (0,0,0,255)
        )

        self.add_widget(self.Wheel_Speed)

        #Gear Position____________________________________
        self.Gear_Position = Button(
            disabled = True,
            #text settings
            text = "5",
            font_size = "384sp",
            bold = True,
            #size and position
            size_hint = (.50,.80),
            pos_hint = {"x":.5, "y":.1},
            #color settings
            color = (1,1,1,1),
            background_color = (0,0,0,255)
        )

        self.add_widget(self.Gear_Position)

        #Engine Temperature______________________________
        self.Engine_Temp = Button(
            disabled = True,
            #text settings
            text = "500C",
            font_size = "20sp",
            bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.0, "y":.0},
            #color settings
            color = (0,0,0,1),
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
            background_color = (255,255,0,255)
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
            background_color = (0,0,0,255)
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

        self.Pot_data()

    #Swipe gesture
    def on_touch_move(self, touch):
        if touch.x < touch.ox: 
            Main_App.get_running_app().change_screen(screen_name = "IMU", screen_direction = "left")


#----------------------------------------------------------------------------------------------
#IMU page

class IMU_Screen(Screen,FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Background Image__________________________________
        self.background_img = Image(
            source = "Chasis.png"    #PNG Only
        )
        self.add_widget(self.background_img)

        #Front Left Tyre____________________________________
        self.Left_Front = Button(
            disabled = True,
            #text settings
            text = "20*",
            font_size = "84sp",
            bold = True,
            #size and position
            size_hint = (.30,.30),
            pos_hint = {"x":.05, "y":.6},
            #color settings
            color = (0,0,0,1),
            background_color = (255,255,255,1)
        )

        self.add_widget(self.Left_Front)

        #Front Right Tyre___________________________________
        self.Right_Front = Button(
            disabled = True,
            #text settings
            text = "20*",
            font_size = "84sp",
            bold = True,
            #size and position
            size_hint = (.30,.30),
            pos_hint = {"x":.65, "y":.6},
            #color settings
            color = (0,0,0,1),
            background_color = (255,255,255,1)
        )

        self.add_widget(self.Right_Front)

        #Rear Left Tyre_____________________________________
        self.Left_Rear = Button(
            disabled = True,
            #text settings
            text = "20*",
            font_size = "84sp",
            bold = True,
            #size and position
            size_hint = (.30,.30),
            pos_hint = {"x":.05, "y":.1},
            #color settings
            color = (0,0,0,1),
            background_color = (255,255,255,1)
        )

        self.add_widget(self.Left_Rear)

        #Rear Right Tyre____________________________________
        self.Rear_Right = Button(
            disabled = True,
            #text settings
            text = "20*",
            font_size = "84sp",
            bold = True,
            #size and position
            size_hint = (.30,.30),
            pos_hint = {"x":.65, "y":.1},
            #color settings
            color = (0,0,0,1),
            background_color = (255,255,255,1)
        )

        self.add_widget(self.Rear_Right)

        #Title____________________________________
        self.Title = Button(
            disabled = True,
            #text settings
            text = "Slip Angle",
            font_size = "48sp",
            bold = True,
            #size and position
            size_hint = (.30,.30),
            pos_hint = {"x":.35, "y":.75},
            #color settings
            color = (0,0,0,1),
            background_color = (255,255,255,1)
        )

        self.add_widget(self.Title)

        #Calibrate____________________________________
        self.Calibrate_Button = Button(
            #text settings
            text = "Calibrate",
            font_size = "24sp",
            bold = True,
            #size and position
            size_hint = (.20,.10),
            pos_hint = {"x":.40, "y":.05},
            #color settings
            color = (0,0,0,1),
            background_color = (255,255,255,1)

            #########LOGIC!!!!!!##########
        )

        self.add_widget(self.Calibrate_Button)

    def on_touch_move(self, touch):
        if touch.x > touch.ox:
            Main_App.get_running_app().change_screen(screen_name="Main", screen_direction = "right")

        if touch.ox > touch.x:
            Main_App.get_running_app().change_screen(screen_name="About", screen_direction = "left")

#----------------------------------------------------------------------------------------------
#Warnings page

#----------------------------------------------------------------------------------------------
#Settings page

#----------------------------------------------------------------------------------------------
#Raw Data page

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

        Clock.schedule_once(self.switch_to_main, 5)
        
    def switch_to_main(self, *args):
        Main_App.get_running_app().change_screen(screen_name = "Main", screen_direction = "up")



#----------------------------------------------------------------------------------------------
#About page

class About_Page(Screen,FloatLayout):
    def _init_(self, **kw):
        super()._init_(**kw)
        
        self.about_image = Image(
        source = "vr_logo.png", 
        size_hint = (0.1, 0.1), 
        pos_hint = {"x" : 0.1,"y": 0.1}
        )
        self.add_widget(self.about_image)

        self.about_text = Button(
            text = "Veloce Racing Team 2021-22 VIT PUNE.\nApp build version = (Unreleased)",
            disabled = True,
            size_hint=(0.1,0.1),
            pos_hint = {"x" : 0.5,"y" : 0.5},
            color = (1,1,1,1)
            )
        self.add_widget(self.about_text)

    def on_touch_move(self, touch):
        if touch.x > touch.ox:
            Main_App.get_running_app().change_screen(screen_name="IMU", screen_direction = "right")

#////////////////////////////////////////////////////////////
## Main Class
class Main_App(App):

    def build(self):
        #To make window borderless and fullscreen
        Window.borderless = True
        Window.fullscreen = True

        #Creating Screen manager and declaring screens
        self.Screen_Manager = ScreenManager(transition = SlideTransition())
        self.Screen_Manager.add_widget(Welcome_Screen(name = 'Welcome'))
        self.Screen_Manager.add_widget(Main_Screen(name = 'Main'))
        self.Screen_Manager.add_widget(IMU_Screen(name = 'IMU'))
        self.Screen_Manager.add_widget(About_Page(name = 'About'))
       
        return self.Screen_Manager

    #Function to change screen, call in classes
    def change_screen(self, screen_name, screen_direction):
        self.Screen_Manager.current = screen_name
        self.Screen_Manager.transition.direction = screen_direction

test = Main_App()

test.run()

#////////////////////////////////////////////////////////////
