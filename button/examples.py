from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button, ButtonBehavior
from kivy.app import App
from kivy.lang import Builder

Builder.load_string("""
<ExampleApp>
    orientation: "vertical"
    Button:
        StackLayout:
            pos: self.parent.pos
            size: self.parent.size
            orientation: 'lr-tb'
            Image:
                source: 'kivy.png'
                size_hint_x: None
                width: 74
            Label:
                size_hint_x: None
                width: 100
                text: "The text"
    Label:
        text: "A label"
        color: 0,1,0,1
        canvas.before:
            Color:
                rgba: 1, 0, 0, 1
            Rectangle:
                pos: self.pos
                size: self.size
            
""")


class ExampleApp(App, BoxLayout):

    def build(self):
        return self


if __name__ == '__main__':
    ExampleApp().run()
