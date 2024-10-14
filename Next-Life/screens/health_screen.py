from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class HealthScreen(Screen):
    def __init__(self, **kwargs):
        super(HealthScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        label = Label(text="Health & Wellness Screen", font_size=24)
        layout.add_widget(label)

        self.add_widget(layout)
