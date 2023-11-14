from kivy.uix.screenmanager import Screen
import os
from kivy.lang import Builder


class Practise(Screen):
    def answer(self, instance):
        print(f"answer pressed ({instance.text})")


Builder.load_file(os.path.join(os.path.dirname(__file__), "practise.kv"))
