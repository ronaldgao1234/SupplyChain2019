#!/usr/bin/env python
# -*- encoding: utf-8

import datetime
import pandas as pd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import dfgui
import pandas as pd
from kivy import platform
import os
import kivy
import kivy.garden.filebrowser
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from SupplyChain import main
from utils.GenerateDataBase import generateDatabase

class Visualisation(App):
    pass


class GraphDraw(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxLayout, self).__init__(**kwargs)
        update = self._trigger_layout
        fbind = self.fbind
        fbind('spacing', update)
        fbind('padding', update)
        fbind('children', update)
        fbind('orientation', update)
        fbind('parent', update)
        fbind('size', update)
        fbind('pos', update)
        self.selected = []
        self.db = None

    def file_select(self):
        homeDir = None
        if platform == 'win':
            homeDir = os.environ["HOMEPATH"]
        elif platform == 'android':
            homeDir = os.path.dirname(os.path.abspath(__file__))
        elif platform == 'linux':
            homeDir = os.environ["HOME"]
        self.pop = UploadPopup(homeDir, 'import')
        self.selected = self.pop.start()

    def generate_database(self):
        self.db = generateDatabase(10)
        dfgui.show(self.db)

    def run_ai(self):
        out = main(self.selected, self.db)
        dfgui.show(out)

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
        for file in self.selected:
            xls = pd.read_csv(file)
            dfgui.show(xls)

        self.popup.dismiss()
        self.fbrowser = None

    def _fbrowser_canceled(self, instance):
        self.popup.dismiss()
        self.fbrowser = None

if __name__ == '__main__':
    Visualisation().run()