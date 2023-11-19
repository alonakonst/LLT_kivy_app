from View.main_screen import MainScreenView
from kivy.lang import Builder
class MainScreenController:


    def __init__(self):
        self.view =  MainScreenView(controller=self)


    def get_screen(self):


        self.view.current='add_to_dict'

        return self.view
