from kivymd.app import MDApp
from kivy.core.window import Window
from Controller.main_screen import MainScreenController
from kivy.lang import Builder
Window.size = (310, 580)

class LLTApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = MainScreenController()

    def build(self):
        return self.controller.get_screen()


if __name__ == '__main__':
    from Utility import initialise_database
    # If dummy=True will fill the database with content if it's empty
    initialise_database(dummy=True)
    LLTApp().run()
