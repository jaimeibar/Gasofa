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
        self.input_kmtrs = TextInput(multiline=False, input_filter='int', write_tab=False)
        self.add_widget(self.input_kmtrs)

        self.add_widget(Label(text='€/l'))
        self.input_price = TextInput(multiline=False, input_filter='float', write_tab=False)
        self.add_widget(self.input_price)

        self.add_widget(Label(text='l/100'))
        self.input_avgconsumption = TextInput(multiline=False, input_filter='float', write_tab=False)
        self.add_widget(self.input_avgconsumption)

        self.add_widget(Label(text='Litres'))
        self.input_litres = TextInput(multiline=False, input_filter='int', disabled=True, readonly=True, is_focusable=False)
        self.add_widget(self.input_litres)

        self.add_widget(Label(text='€'))
        self.input_euros = TextInput(multiline=False, input='float', disabled=True, readonly=True, is_focusable=False)
        self.add_widget(self.input_euros)

        btn_go = Button(text='Go')
        btn_go.bind(on_press=self.on_press_callback)
        self.add_widget(btn_go)

        btn_reset = Button(text='Reset')
        btn_reset.bind(on_press=self.on_reset_callback)
        self.add_widget(btn_reset)

    def on_press_callback(self, value):
        """
        Number of litres and total amount in €
        :param value:
        :return:
        """
        ltrs = self.calculate_number_of_litres()
        self.input_litres.text = str(ltrs)
        total = self.calculate_bill(ltrs)
        self.input_euros.text = str(total)

    def on_reset_callback(self, value):
        """
        Clear all fields.
        :param value:
        :return:
        """
        self.input_kmtrs.text = ''
        self.input_price.text = ''
        self.input_avgconsumption.text = ''
        self.input_litres.text = ''
        self.input_euros.text = ''

    def calculate_number_of_litres(self):
        """
        Number of litres.
        :return: Number of litres
        """
        litrs = (float(self.input_kmtrs.text) * float(self.input_avgconsumption.text)) / 100
        return litrs

    def calculate_bill(self, litrs):
        """
        Total amount in €
        :param litrs: Number of litres
        :return: Total amount in €
        """
        total = float(litrs) * float(self.input_price.text)
        return total


class MainApp(App):

    title = 'Gasofa'

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    MainApp().run()
