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
        self.input_kmtrs = TextInput(multiline=False, input_filter='int')
        self.add_widget(self.input_kmtrs)

        self.add_widget(Label(text='€/l'))
        self.input_rate = TextInput(multiline=False, input_filter='float')
        self.add_widget(self.input_rate)

        self.add_widget(Label(text='l/100'))
        self.input_consumption = TextInput(multiline=False, input_filter='float')
        self.add_widget(self.input_consumption)

        self.add_widget(Label(text='Litres'))
        self.input_litres = TextInput(multiline=False, input_filter='int', disable=True)
        self.add_widget(self.input_litres)

        self.add_widget(Label(text='Fuel Consumption'))
        self.input_fuel = TextInput(multiline=False, input_filter='int')
        self.add_widget(self.input_fuel)

        self.add_widget(Label(text='€'))
        self.input_euros = TextInput(multiline=False, input='float', disabled=True)
        self.add_widget(self.input_euros)

        btn_go = Button(text='Go')
        btn_go.bind(on_press=self.on_press_callback)
        self.add_widget(btn_go)

        btn_reset = Button(text='Reset')
        btn_reset.bind(on_press=self.on_reset_callback)
        self.add_widget(btn_reset)

    def on_press_callback(self, value):
        print('Foo {0}'.format(self.kmtrs.text))

    def on_reset_callback(self, value):
        pass

    def calculate_litres(self, **kwargs):
        pass

class MainApp(App):

    title = 'Gasofa'

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    MainApp().run()
