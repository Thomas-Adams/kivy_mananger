from kivy.event import EventDispatcher
from kivy.properties import StringProperty
from kivy.uix.actionbar import ActionDropDown, ActionItem
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import os

IMAGE_BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', 'buttons') + '/'
SUFFIX = '.png'
LIGHTEN_SUFFIX = '-lighten' + SUFFIX
DARKEN_SUFFIX = '-lighten' + SUFFIX


class ColorActionButton(ActionItem, Button, EventDispatcher):
    color_name = StringProperty()
    base_dir = IMAGE_BASE_DIR
    b_normal = StringProperty()
    b_down = StringProperty()
    b_disabled_down = StringProperty()
    b_disabled = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_color_name(self, instance, value):
        self.b_normal = self.base_dir + value + SUFFIX
        self.b_down = self.base_dir + value + LIGHTEN_SUFFIX
        self.b_disabled_down = self.base_dir + value + DARKEN_SUFFIX

class MainScreenManager(ScreenManager):
    pass

class ListScreen(Screen):
    pass

class CreateScreen(Screen):
    pass


class MainView(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        return MainView()

if __name__ == '__main__':
    MainApp().run()

