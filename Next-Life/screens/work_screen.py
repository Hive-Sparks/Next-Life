from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class WorkScreen(Screen):
    def __init__(self, **kwargs):
        super(WorkScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        label = Label(text="Work & Career Screen", font_size=24)
        layout.add_widget(label)

        self.add_widget(layout)
