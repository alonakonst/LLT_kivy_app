from View.main_screen import MainScreenView

class MainScreenController:


    def __init__(self):
        self.view =  MainScreenView(controller=self)

    def get_screen(self):
        return self.view
