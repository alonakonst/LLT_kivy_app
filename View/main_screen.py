import os

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreenView(ScreenManager):
    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        welcome_window = WelcomeWindow()
        self.add_widget(welcome_window)

        second_window = SecondWindow()
        self.add_widget(second_window)

        insert_dict = InsertIntoDictionary()
        self.add_widget(insert_dict)

        display = DisplayDictionary()
        self.add_widget(display)

class WelcomeWindow(Screen):
        pass


class SecondWindow(Screen):
    pass


class InsertIntoDictionary(Screen):
    pass


class DisplayDictionary(Screen):
    pass


Builder.load_file(os.path.join(os.path.dirname(__file__), "main_screen.kv"))

print("also this")