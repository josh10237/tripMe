import os
import kivy
import utils
import kivy.utils
from kivy.app import App

from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.slider import Slider
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import os
from threading import Thread
from time import sleep

SCREEN_MANAGER = ScreenManager()
email = ""
name = ""
age = ""
gender = ""

class TripMe(App):

    def build(self):
        SCREEN_MANAGER.current = 'main'
        return SCREEN_MANAGER


Window.clearcolor = (0, .6, .6, 1)
#main color: (3, 1, 1, 1)


class MainScreen(Screen):

    def getStarted(self):
        SCREEN_MANAGER.current = 'one'

class one(Screen):
    def __init__(self, **kwargs):
            Builder.load_file('one.kv')
            super(one, self).__init__(**kwargs)

    def whyDoWeAsk(self):
        SCREEN_MANAGER.current = 'why'

    def submitEmail(self):
        name = self.ids.name.text
        email = self.ids.email.text
        age = self.ids.age.text
        gender = self.ids.gender.text
        print(name+" "+email+" "+age+" "+gender)
        SCREEN_MANAGER.current = 'two'



class why(Screen):
    def __init__(self, **kwargs):
            Builder.load_file('why.kv')
            super(why, self).__init__(**kwargs)

class two(Screen):
    def __init__(self, **kwargs):
            Builder.load_file('two.kv')
            super(two, self).__init__(**kwargs)


Builder.load_file('main.kv')
SCREEN_MANAGER.add_widget(MainScreen(name='main'))
SCREEN_MANAGER.add_widget(one(name='one'))
SCREEN_MANAGER.add_widget(why(name='why'))
SCREEN_MANAGER.add_widget(two(name='two'))

if __name__ == "__main__":
    TripMe().run()