import os

import kivy
from kivy import platform
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
import kivy.garden.filebrowser
from kivy.uix.popup import Popup

class FileBrowserApp(App):

    def build(self):
        self.root = FloatLayout()
        button = Button(text='Select Files', pos_hint={'x':0, 'y': 0}, size_hint=(0.2, 0.1))
        button.bind(on_press=self.do_select)
        self.root.add_widget(button)
        return self.root

    def do_select(self, *args):
        homeDir = None
        if platform == 'win':
            homeDir = os.environ["HOMEPATH"]
        elif platform == 'android':
            homeDir = os.path.dirname(os.path.abspath(__file__))
        elif platform == 'linux':
            homeDir = os.environ["HOME"]
        self.pop = UploadPopup(homeDir, 'import')
        self.pop.start()


class UploadPopup:
    def __init__(self, homeDir, text='import'):
        self.fbrowser = kivy.garden.filebrowser.FileBrowser(select_string='Select',
                                                            multiselect=True, filters=['*.csv'], path=homeDir)
        self.fbrowser.bind(
            on_success=self._fbrowser_success,
            on_canceled=self._fbrowser_canceled,
            on_submit=self._fbrowser_success)
        self.popup = Popup(
            title='select',
            content=self.fbrowser, size_hint=(0.9, 0.9),
            auto_dismiss=False
        )
        self.selected = []

    def start(self):
        self.popup.open()
        return self.selected

    def _fbrowser_success(self, fbInstance):
        if len(fbInstance.selection) == 0:
            return
        for file in fbInstance.selection:
            self.selected.append(os.path.join(fbInstance.path, file))
        print('selected: ' + str(self.selected))
        self.popup.dismiss()
        self.fbrowser = None

    def _fbrowser_canceled(self, instance):
        self.popup.dismiss()
        self.fbrowser = None


if __name__=="__main__":
    app = FileBrowserApp()
    app.run()