from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
import requests


# kv文件要和主文件夹放在同一个目录下面
Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    url = 'https://image.baidu.com/search/acjson'
    params = {
        'tn': 'resultjson_com',
        'ipn': 'rj',
        'queryWord': 'Python',
        'word': 'Python',
        'pn': 0,  # 返回结果的起始位置
        'rn': 10,  # 返回结果数量
    }
    def search_image(self):
        # query = self.manager.current_screen.ids.query_text.text
        # response = requests.get(self.url, params=self.params)
        # if response.status_code == 200:
        #     print(response.content.json())
        self.manager.current_screen.ids.img.source = 'files/bg.jpg'

class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()