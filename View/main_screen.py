import os
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager

from View.Screens.add_to_dict import AddToDict
from View.Screens.dictionary import Dictionary
from View.Screens.practise import Practise

class MainScreenView(ScreenManager):
    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        add_to_dict = AddToDict()
        self.add_widget(add_to_dict)

        dictionary = Dictionary()
        self.add_widget(dictionary)

        practise = Practise()
        self.add_widget(practise)



Builder.load_file(os.path.join(os.path.dirname(__file__), "main_screen.kv"))
