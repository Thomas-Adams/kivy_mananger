from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.utils import get_color_from_hex
from kivymd.theming import ThemableBehavior, ThemeManager


class ColorLabel(Label):

    def __init__(self, **kwargs):
        super(ColorLabel, self).__init__(**kwargs)
        self.color = get_color_from_hex('#222222')
        self.font_size = 14
        self.bold = False


class MaterialTextInput(TextInput):

    def __init__(self, **kwargs):
        super(MaterialTextInput, self).__init__(**kwargs)
        self.font_size = 14
        self.size = (300, 40)
        self.size_hint_max = (300, 40)
        self.background_active =''
        self.background_normal =''
        self.background_color = get_color_from_hex('#ffffff')


class CreateFormView(BoxLayout):
    pass


class CreateFormApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'

    def build(self):
        return CreateFormView()


if __name__ == '__main__':
    CreateFormApp().run()
