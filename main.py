from Controller.main_screen import MainScreenController

from kivymd.app import MDApp

# from kivy.core.window import Window
# Window.size = (310, 580)


class LLTApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = MainScreenController()

    def build(self):
        return self.controller.get_screen()


if __name__ == '__main__':
    dummy = False
    # check if the database exists
    from pathlib import Path
    if not Path('database.db').exists():
        dummy = True

    from Utility import initialise_database

    # If dummy==True will fill the database with content if it's empty
    initialise_database(dummy=dummy)

    LLTApp().run()
