from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        # Main layout for the home screen
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # List of categories
        categories = [
            ("Health & Wellness", "health"),
            ("Family & Relationships", "family"),
            ("Work & Career", "work"),
            ("Leisure & Hobbies", "leisure"),
            ("Finance & Budget", "finance"),
            ("Personal Growth", "personal_growth"),
            ("Community & Environment", "community"),
            ("Spirituality & Meaning", "spirituality"),
            ("Insights & Recommendations", "insights")
        ]

        # Create a button for each category
        for category_name, screen_name in categories:
            button = Button(text=category_name, size_hint_y=None, height=50)
            button.bind(on_press=lambda instance, name=screen_name: self.go_to_screen(name))
            layout.add_widget(button)

        # Add layout to screen
        # self.add_widget(layout)

    def go_to_screen(self, screen_name):
        # Navigate to the selected screen
        self.manager.current = screen_name
