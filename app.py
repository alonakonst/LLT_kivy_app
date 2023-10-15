import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self,**kwargs):
        super(childApp, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='Your Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)


        self.press = Button(text = 'Submit')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        print("Name of the Student is: " +self.s_name.text)

class parentApp(App):
    def build(self):
        return childApp()

if __name__=="__main__":
    parentApp().run()