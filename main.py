import os
import kivy
import utils
import kivy.utils
from kivy.app import App

from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import os
from threading import Thread
from time import sleep

SCREEN_MANAGER = ScreenManager()


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


class why(Screen):
    def __init__(self, **kwargs):
            Builder.load_file('why.kv')
            super(why, self).__init__(**kwargs)



Builder.load_file('main.kv')
SCREEN_MANAGER.add_widget(MainScreen(name='main'))
SCREEN_MANAGER.add_widget(one(name='one'))
SCREEN_MANAGER.add_widget(one(name='why'))

if __name__ == "__main__":
    TripMe().run()