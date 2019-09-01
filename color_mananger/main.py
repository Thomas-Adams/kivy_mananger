from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class MainView(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        return MainView()

if __name__ == '__main__':
    MainApp().run()
