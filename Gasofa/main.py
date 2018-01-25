# -*- coding: utf-8 -*-

from __future__ import print_function

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.logger import Logger


kivy.require('1.10.0')  # replace with your current kivy version!

__version__ = '0.2'


class MainScreen(GridLayout):

    def on_press_callback(self):
        """
        Number of litres and total amount in €
        """
        ltrs = self.calculate_number_of_litres()
        total = self.calculate_bill(ltrs)
        self.ids.inputlitres.text = str(ltrs)
        self.ids.inputeuros.text = str(total)

    def on_clear_callback(self):
        """
        Clear all text input fields.
        """
        for fd in self.get_all_input_text_fields():
            fd.text = ''

    def on_text_validate_callback(self):
        """
        Check input text fields and enable/disable them depending on
        previous status.
        """
        Logger.info('on text validate callback')
        fields = self.get_input_text_fields()
        if all(fields):
            self.ids.btngo.disabled = False
            self.ids.btnclear.disabled = False
        elif any(fields):
            self.ids.btngo.disabled = True
            self.ids.btnclear.disabled = True

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

    def get_input_text_fields(self):
        """
        Return a list with all writable input text fields available.
        :return: list of writable input text fields available.
        """
        inputtext = [self.ids.inputkms, self.ids.inputprice,
                     self.ids.inputavgconsumption]
        return inputtext

    def get_all_input_text_fields(self):
        """
        Builds a list containing all input text fields.
        :return: List containing all input text fields.
        """
        fids = [self.ids.inputlitres, self.ids.inputeuros]
        fids.extend(self.get_input_text_fields())
        return fids


class MainApp(App):

    title = 'Gasofa'

    def build(self):
        return MainScreen()


if __name__ == '__main__':
    Logger.info('Starting Gasofa')
    MainApp().run()
