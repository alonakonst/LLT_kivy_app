from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.bottomnavigation import MDBottomNavigation

class NavigationBar(BoxLayout):

    def switch_screens(self, root, screen, order):
        print(root.screen_manager.current)
        root.screen_manager.current = screen
        print(root.screen_manager.current)

    #todo: implement this logic in my function
    def change_screen(self, to_screen):
        sm = self.ids.tab_manager
        print(type(sm))
        current = sm.current_screen
        if current.order < sm.get_screen(to_screen).order:   sm.transition.direction = 'left'
        if current.order > sm.get_screen(to_screen).order:   sm.transition.direction = 'right'
        self.current_tab = current.order