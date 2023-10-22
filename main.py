import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import sqlite3
from Controller.main_screen import MainScreenController
from Model.main_screen import MainScreenModel


class LLTApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = MainScreenModel()
        self.controller = MainScreenController(self.model)

    def build(self):
        return self.controller.get_screen()


LLTApp().run()