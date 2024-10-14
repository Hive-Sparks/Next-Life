from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class SpiritualityScreen(Screen):
    def __init__(self, **kwargs):
        super(SpiritualityScreen, self).__init__(**kwargs)
        # ... existing code ...
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Spirituality & Meaning Screen", font_size=24)
        layout.add_widget(label)

        self.add_widget(layout)
    