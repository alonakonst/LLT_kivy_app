
from kivymd.app import MDApp

from kivy.core.window import Window

from View import MainScreenView

Window.size = (310, 300)


class LLTApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def build(self):
        return MainScreenView()


if __name__ == '__main__':
    # Set window.size for debugging
    from kivy.utils import platform
    if platform != 'android':
        from kivy.core.window import Window
        Window.size = (1080 / 3, 2400 / 3)

    # load 'config.env' into environment variables
    from dotenv import load_dotenv
    load_dotenv('config.env')

    dummy = False
    # check if the database exists
    from pathlib import Path
    if not Path('database.db').exists():
        dummy = True

    from Utility import initialise_database

    # If dummy==True will fill the database with content if it's empty
    initialise_database(dummy=dummy)

    LLTApp().run()
