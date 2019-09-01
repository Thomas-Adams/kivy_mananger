from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


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
