from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from screens.home_screen import HomeScreen  # ייבוא של מסך הבית
from screens.health_screen import HealthScreen
from screens.family_screen import FamilyScreen
from screens.work_screen import WorkScreen
from screens.leisure_screen import LeisureScreen
from screens.finance_screen import FinanceScreen
from screens.personal_growth_screen import PersonalGrowthScreen
from screens.community_screen import CommunityScreen
from screens.spirituality_screen import SpiritualityScreen
from screens.insights_screen import InsightsScreen
from kivy.graphics import Color, Rectangle


# Set a window size for better UX
Window.size = (800, 600)

class ImageButton(ButtonBehavior, Image):
    pass

class MyScreenManager(ScreenManager):
    pass

class Next_Life_App(App):
    def build(self):
        sm = MyScreenManager(transition=FadeTransition())

        # Add all the screens to the ScreenManager
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(HealthScreen(name="health"))
        sm.add_widget(FamilyScreen(name="family"))
        sm.add_widget(WorkScreen(name="work"))
        sm.add_widget(LeisureScreen(name="leisure"))
        sm.add_widget(FinanceScreen(name="finance"))
        sm.add_widget(PersonalGrowthScreen(name="personal_growth"))
        sm.add_widget(CommunityScreen(name="community"))
        sm.add_widget(SpiritualityScreen(name="spirituality"))
        sm.add_widget(InsightsScreen(name="insights"))

        # Create a navigation bar with icons
        nav_bar = BoxLayout(size_hint_y=0.1, padding=10, spacing=10)
        with nav_bar.canvas.before:
            Color(0.2, 0.2, 0.2, 1)  # Set the color
            Rectangle(size=nav_bar.size, pos=nav_bar.pos)

        # Dictionary of screen names and their display names
        screens = {
            "home": "Next-Life",
            "health": "Health",
            "family": "Family",
            "work": "Work",
            "leisure": "Leisure",
            "finance": "Finance",
            "personal_growth": "Growth",
            "community": "Community",
            "spirituality": "Spiritual",
            "insights": "Insights"
        }

        # Create navigation buttons with icons
        for screen_name, display_name in screens.items():
            btn = Button(text=display_name, background_color=(0.1, 0.5, 0.8, 1), color=(1, 1, 1, 1))
            btn.bind(on_press=self.create_nav_callback(screen_name, sm))
            nav_bar.add_widget(btn)

        # Create the main layout
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(nav_bar)
        main_layout.add_widget(sm)

        # Create a grid layout for the home screen to show summaries
        home_grid = GridLayout(cols=2, spacing=10, padding=10)

        # Add summary buttons or labels to the grid layout
        for screen_name, display_name in screens.items():
            summary_btn = Button(text=f"{display_name} Summary", size_hint_y=None, height=100)
            summary_btn.bind(on_press=self.create_nav_callback(screen_name, sm))
            home_grid.add_widget(summary_btn)

        # Add the grid layout to the home screen
        sm.get_screen('home').add_widget(home_grid)

        # Add version label at the bottom
        version_label = Label(text="Version 1.0", size_hint_y=0.05, color=(0.5, 0.5, 0.5, 1))
        main_layout.add_widget(version_label)

        # Set the default screen to HomeScreen
        sm.current = "home"

        return main_layout

    def create_nav_callback(self, screen_name, screen_manager):
        def switch_screen(instance):
            screen_manager.current = screen_name
        return switch_screen

if __name__ == "__main__":
    Next_Life_App().run()
