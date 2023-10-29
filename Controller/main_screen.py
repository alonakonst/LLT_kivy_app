from View.main_screen import MainScreenView, InsertIntoDictionary

class MainScreenController:


    def __init__(self,model):
        self.model = model
        self.view =  MainScreenView(controller=self)

    def get_screen(self):
        return self.view
