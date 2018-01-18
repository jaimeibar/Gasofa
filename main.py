# -*- coding: utf-8 -*-

from __future__ import print_function

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.logger import Logger


kivy.require('1.10.1')  # replace with your current kivy version!

__version__ = '0.1'


class MainScreen(GridLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='Kms'))
        kmtrs = TextInput(multiline=False, input_filter='int')
        self.add_widget(kmtrs)

        self.add_widget(Label(text='€/l'))
        rate = TextInput(multiline=False, input_filter='float')
        self.add_widget(rate)

        self.add_widget(Label(text='l/100'))
        consumption = TextInput(multiline=False, input_filter='float')
        self.add_widget(consumption)

        self.add_widget(Label(text='Litres'))
        litres = TextInput(multiline=False, input_filter='int', disable=True)
        self.add_widget(litres)

        self.add_widget(Label(text='Fuel Consumption'))
        fuel = TextInput(multiline=False, input_filter='int')
        self.add_widget(fuel)

        self.add_widget(Label(text='€'))
        euros = TextInput(multiline=False, input='float', disabled=True)
        self.add_widget(euros)

        btn_go = Button(text='Go')
        btn_go.bind(on_press=self.on_press_callback)
        self.add_widget(btn_go)

        btn_reset = Button(text='Reset')
        btn_reset.bind(on_press=self.on_reset_callback)
        self.add_widget(btn_reset)

    def on_press_callback(self, value):
        pass

    def on_reset_callback(self, value):
        pass


class MainApp(App):

    title = 'Gasofa'

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    MainApp().run()
