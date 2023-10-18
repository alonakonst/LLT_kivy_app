import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class WelcomeWindow(Screen):
   user_name = ObjectProperty(None)

   def btn(self):
       print("Name:", self.user_name.text)
       self.user_name.text = ""

class SecondWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("style.kv")

class LLTApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    LLTApp().run()