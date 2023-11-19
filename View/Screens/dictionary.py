from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivymd.uix.list import OneLineListItem
class Dictionary(Screen):
    table = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self):
        for _ in range(50):
            self.ids.container.add_widget(
                OneLineListItem(
                    text=f"This is element number {_}"
                )
            )


