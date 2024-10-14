from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class CommunityScreen(Screen):
    def __init__(self, **kwargs):
        super(CommunityScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        label = Label(text="Community & Environment Screen", font_size=24)
        layout.add_widget(label)

        self.add_widget(layout)
