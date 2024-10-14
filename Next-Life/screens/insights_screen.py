from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class InsightsScreen(Screen):
    def __init__(self, **kwargs):
        super(InsightsScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        label = Label(text="Insights & Recommendations Screen", font_size=24)
        layout.add_widget(label)

        self.add_widget(layout)
