import kivy
kivy.require('2.0.0')
from kivy.app import App
#from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition

class Screen_1(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.Label1 = Label(
            text = "Screen 1",
            color = (1,1,1,1)
        )
        self.add_widget(self.Label1)
    def on_touch_move(self,touch):
        if touch.x < touch.ox:
            print("Touch detected",touch.ox)
            Main_App.get_running_app().change_screen(screen_name="2",screen_direction="left")


class Screen_2(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.Label2 = Label(
            text = "Screen 2",
            color = (1,1,1,1)
            
        )
        self.add_widget(self.Label2)
    def on_touch_move(self,touch):
        if touch.x > touch.ox:
            Main_App.get_running_app().change_screen(screen_name="1",screen_direction="right")

    
class Main_App(App):
    

    def build(self):

        self.Screen_Manager = ScreenManager(transition=SlideTransition())
        self.Screen_Manager.add_widget(Screen_1(name='1'))
        self.Screen_Manager.add_widget(Screen_2(name='2')) 

        return self.Screen_Manager
    def change_screen(self,screen_name,screen_direction):
        print("Called Change Screen")
        self.Screen_Manager.current=screen_name
        self.Screen_Manager.transition.direction=screen_direction
        
        #self.Screen_Manager.current=screen_name
        #self.Screen_Manager.transition.direction=screen_direction

test = Main_App()
test.run()
