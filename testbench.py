'''
Test Bench

'''

from multiprocessing import Value
import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.label import Label

#from kivy.uix.image import Image
#from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.uix.screenmanager import SlideTransition
#from kivy.uix.scrollview import ScrollView

class Main_Class(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.Slider_1 = Slider(
            min=0, 
            max=100, 
            step=20
            )

        self.add_widget(self.Slider_1)

        self.Test1 = Button(
            disabled = True,
            #text settings
            #text = "20*",
            #font_size = "84sp",
            #bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.0, "y":.0},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.Test2 = Button(
            disabled = True,
            #text settings
            #text = "20*",
            #font_size = "84sp",
            #bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.1, "y":.0},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.Test3 = Button(
            disabled = True,
            #text settings
            #text = "20*",
            #font_size = "84sp",
            #bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.2, "y":.0},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.Test4 = Button(
            disabled = True,
            #text settings
            #text = "20*",
            #font_size = "84sp",
            #bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.3, "y":.0},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.Test5 = Button(
            disabled = True,
            #text settings
            #text = "20*",
            #font_size = "84sp",
            #bold = True,
            #size and position
            size_hint = (.10,.10),
            pos_hint = {"x":.4, "y":.0},
            #color settings
            color = (0,0,0,1),
            background_color = (255,0,0,255)
        )

        self.Slider_1.bind(value = self.OnSlider)

    def OnSlider(self, instance, slider_value):
            #print("Slider value is ",int(slider_value))
            #print(self.Slider_1.value)

            if self.Slider_1.value == 0:
                self.remove_widget(self.Test1)
                self.remove_widget(self.Test2)
                self.remove_widget(self.Test3)
                self.remove_widget(self.Test4)
                self.remove_widget(self.Test5)

            elif self.Slider_1.value == 20:  
                self.remove_widget(self.Test1)
                self.remove_widget(self.Test2)
                self.remove_widget(self.Test3)
                self.remove_widget(self.Test4)
                self.remove_widget(self.Test5)
                self.add_widget(self.Test1)

            elif self.Slider_1.value == 40:  
                self.remove_widget(self.Test1)
                self.remove_widget(self.Test2)
                self.remove_widget(self.Test3)
                self.remove_widget(self.Test4)
                self.remove_widget(self.Test5)
                self.add_widget(self.Test1)
                self.add_widget(self.Test2)

            elif self.Slider_1.value == 60:  
                self.remove_widget(self.Test1)
                self.remove_widget(self.Test2)
                self.remove_widget(self.Test3)
                self.remove_widget(self.Test4)
                self.remove_widget(self.Test5)
                self.add_widget(self.Test1)
                self.add_widget(self.Test2)
                self.add_widget(self.Test3)

            elif self.Slider_1.value == 80:  
                self.remove_widget(self.Test1)
                self.remove_widget(self.Test2)
                self.remove_widget(self.Test3)
                self.remove_widget(self.Test4)
                self.remove_widget(self.Test5)
                self.add_widget(self.Test1)
                self.add_widget(self.Test2)
                self.add_widget(self.Test3)
                self.add_widget(self.Test4)

            elif self.Slider_1.value == 100:  
                self.remove_widget(self.Test1)
                self.remove_widget(self.Test2)
                self.remove_widget(self.Test3)
                self.remove_widget(self.Test4)
                self.remove_widget(self.Test5)
                self.add_widget(self.Test1)
                self.add_widget(self.Test2)
                self.add_widget(self.Test3)
                self.add_widget(self.Test4)
                self.add_widget(self.Test5)


class Test_App(App):

    def build(self):
        return Main_Class()

test = Test_App()
test.run()
