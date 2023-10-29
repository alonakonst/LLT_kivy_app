from kivy.app import App
from Controller.main_screen import MainScreenController


class LLTApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = MainScreenController()

    def build(self):
        return self.controller.get_screen()


if __name__ == '__main__':
    from Utility import initialise_database
    initialise_database()
    LLTApp().run()
