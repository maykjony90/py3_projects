from kivy.app import App
from kivy.uix.button import Button

class TutorialApp(App):
    def build(self):
        return Button(text="Hello World!", background_color=(1,0,1,1),
                      font_size=150)


if __name__ == "__main":
    TutorialApp().run()
