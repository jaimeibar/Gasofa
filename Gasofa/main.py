# -*- coding: utf-8 -*-

from __future__ import print_function

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.logger import Logger


kivy.require('1.10.0')  # replace with your current kivy version!

__version__ = '0.2'


class MainScreen(GridLayout):


    def on_press_callback(self, value):
        """
        Number of litres and total amount in €
        :param value:
        :return:
        """
        ltrs = self.calculate_number_of_litres()
        total = self.calculate_bill(ltrs)
        self.ids.inputlitres.text = str(ltrs)
        self.ids.inputeuros.text = str(total)

    def on_clear_callback(self, value):
        """
        Clear all fields.
        :param value:
        :return:
        """
        self.ids.inputkms.text = ''
        self.ids.inputprice.text = ''
        self.ids.inputavgconsumption.text = ''
        self.ids.inputlitres.text = ''
        self.ids.inputeuros.text = ''

    def calculate_number_of_litres(self):
        """
        Number of litres.
        :return: Number of litres
        """
        litrs = (float(self.ids.inputkms.text) * float(self.ids.inputavgconsumption.text)) / 100
        return litrs

    def calculate_bill(self, litrs):
        """
        Total amount in €
        :param litrs: Number of litres
        :return: Total amount in €
        """
        total = float(litrs) * float(self.ids.inputprice.text)
        return total


class MainApp(App):

    title = 'Gasofa'

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    Logger.info('Starting Gasofa')
    MainApp().run()
