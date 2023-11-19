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

    Builder.load_file('View/Screens/add_to_dict.kv')
    Builder.load_file('View/Screens/dictionary.kv')
    Builder.load_file('View/Screens/practise.kv')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(AddToDict(name='add_to_dict'))
        self.add_widget(Dictionary(name='dictionary'))
        self.add_widget(Practise(name='practise'))



