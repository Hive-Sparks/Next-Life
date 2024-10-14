from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class FamilyScreen(Screen):
    def __init__(self, **kwargs):
        super(FamilyScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        label = Label(text="Family & Relationships Screen", font_size=24)
        layout.add_widget(label)

        self.add_widget(layout)
