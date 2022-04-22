from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Window.size = (640,480)

class Win(Widget):
    def btn_pressed(self):
        pass

class WinApp(App):
    def build(self):
        self.title = 'Parser'
        return Win()
        
WinApp().run()