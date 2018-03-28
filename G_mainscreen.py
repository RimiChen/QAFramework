import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Button
class abu(App):
    def build(self):
        return Button(text = "test GUI", font_size = 40)

a = abu()
a.run()