import os
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


class NavigationBar(BoxLayout):
    pass


Builder.load_file(os.path.dirname(__file__), "view/components/navbar.kv")
