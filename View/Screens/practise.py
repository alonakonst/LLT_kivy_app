from kivy.uix.screenmanager import Screen
import os
from kivy.lang import Builder


class Practise(Screen):
    def answer0(self):
        pass

    def answer1(self):
        pass

    def answer2(self):
        pass

    def answer3(self):
        pass


Builder.load_file(os.path.join(os.path.dirname(__file__), "practise.kv"))
