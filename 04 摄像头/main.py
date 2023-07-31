from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        label = Label(text='Hello Kivy', font_size=50)
        button = Button(text='Click me!', background_color=(0, 0, 1, 1))
        button.bind(on_press=self.on_button_press)
        return label, button

    def on_button_press(self, instance):
        print('Button pressed!')


if __name__ == '__main__':
    MyApp().run()
