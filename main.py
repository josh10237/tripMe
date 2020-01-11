import os

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import os
from threading import Thread
from time import sleep

SCREEN_MANAGER = ScreenManager()


class ProjectNameGUI(App):
    """
    Class to handle running the GUI Application
    """

    def build(self):
        """
        Build the application
        :return: Kivy Screen Manager instance
        """
        return SCREEN_MANAGER


Window.clearcolor = ((158/255), (247/255), (243/255), 1)  # White


class MainScreen(Screen):

    def getStarted(self):
        SCREEN_MANAGER.current = 'image_screen'


class OneScreen(Screen):
    def __init__(self, **kwargs):
            Builder.load_file('One.kv')
            super(OneScreen, self).__init__(**kwargs)



Builder.load_file('main.kv')
SCREEN_MANAGER.add_widget(MainScreen(name='main'))
SCREEN_MANAGER.add_widget(OneScreen(name='One'))

if __name__ == "__main__":
    ProjectNameGUI().run()