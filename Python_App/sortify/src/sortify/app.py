"""
This app is a grocery list sorter to make your visit to the store as fast as possible
"""
from functools import partial

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Sortify(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        box1 = toga.Box()
        box2 = toga.Box()

        main = toga.Box()

        self.input_text = toga.TextInput()
        self.input_text.style.width = 200
        self.input_text.style.padding_top = 20
        self.input_text.style.padding_left = 10

        self.added = toga.TextInput(readonly=True)
        self.added.style.width = 200
        self.added.style.padding_top = 20
        self.added.style.padding_left = 10

        addButton = toga.Button('Add', on_press=partial((Sortify.enterdata), main_box = main, text = self.input_text))
        addButton.style.padding_top = 20
        addButton.style.padding_left = 10

        # adding
        box1.add(self.input_text)
        box1.add(addButton)

        # adding in main box
        main.add(box1)

        main.style.update(direction=COLUMN)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main
        self.main_window.show()

    def enterdata(self, main_box,text):

        new_box = toga.Box()
        label = toga.Label(text)

        new_box.add(label)
        main_box.add(new_box)






def main():
    return Sortify()
