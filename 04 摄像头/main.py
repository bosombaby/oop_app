import datetime
import webbrowser

from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from file_share import FileShare

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    img_path = ''

    def start(self):
        self.ids.camera.play = True
        self.ids.camera.opacity = 1
        self.ids.camera.texture = self.ids.camera._camera.texture
        self.ids.camera_button.text = 'Stop Camera'

    def stop(self):
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera.texture = None
        self.ids.camera_button.text = 'Start Camera'

    def capture(self):
        current_time = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        self.img_path = f'files/{current_time}.png'
        self.ids.camera.export_to_png(self.img_path)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.img_path


class ImageScreen(Screen):
    message = 'Please create a link first'

    def create_link(self):
        img_path = App.get_running_app().root.ids.camera_screen.img_path
        img_share = FileShare(img_path)
        self.img_link = img_share.share()
        self.ids.img_label.text = self.img_link

    def copy_link(self):
        try:
            Clipboard.copy(self.img_link)
        except Exception:
            self.ids.img_label.text = self.message

    def open_link(self):
        try:
            webbrowser.open(self.img_link)
        except Exception:
            self.ids.img_label.text = self.message


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
