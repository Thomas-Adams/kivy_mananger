from kivy.event import EventDispatcher
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button, ButtonBehavior
from kivy.app import App
from kivy.lang import Builder
import os

IMAGE_BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', 'buttons') + '/'
SUFFIX = '.png'
LIGHTEN_SUFFIX = '-lighten' + SUFFIX
DARKEN_SUFFIX = '-lighten' + SUFFIX


class ColorButton(Button, EventDispatcher):
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


Builder.load_string("""
<ColorButtonApp>
    orientation: "vertical"
    ColorButton:
        color_name: 'electric-violet'
        background_normal: self.b_normal
        background_down: self.b_down
        background_disabled_down: self.b_disabled_down
        background_disabled_normal: self.b_disabled_down
        text: 'Hello World!'
        color: 1, 1, 1, 1
""")


class ColorButtonApp(App, BoxLayout):

    def build(self):
        return self


if __name__ == '__main__':
    ColorButtonApp().run()
