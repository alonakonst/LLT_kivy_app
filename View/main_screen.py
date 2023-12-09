import os
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager

from View.Components.navbar import NavigationBar
from View.Screens.add_to_dict import AddToDict
from View.Screens.dictionary import Dictionary
from View.Screens.practise import Practise

class MainScreenView(BoxLayout):
    model = ObjectProperty()
    orientation = 'vertical'

    # Loading kv files of every page
    Builder.load_file('View/Screens/add_to_dict.kv')
    Builder.load_file('View/Screens/dictionary.kv')
    Builder.load_file('View/Screens/practise.kv')

    # Loading kv file of the NavigationBar
    Builder.load_file('View/Components/navbar.kv')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.navbar = NavigationBar()
        self.add_widget(self.navbar)
        self.screen_manager = ScreenManager()
        self.add_widget(self.screen_manager)

        self.screen_manager.add_widget(AddToDict(name='add_to_dict'))
        self.screen_manager.add_widget(Dictionary(name='dictionary'))
        self.screen_manager.add_widget(Practise(name='practise'))







