from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.bottomnavigation import MDBottomNavigation

class NavigationBar(BoxLayout):

    def switch_screens(self, root, screen, order):
        if root.screen_manager.current_screen.order < order:
            root.screen_manager.transition.direction = 'left'
        elif root.screen_manager.current_screen.order > order:
            root.screen_manager.transition.direction = 'right'

        root.screen_manager.current = screen
