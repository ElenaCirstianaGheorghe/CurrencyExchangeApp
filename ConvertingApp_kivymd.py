from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from ConvertingApp_OOP import *
from ConvertingApp_scraping import exchange_dict, symbols_dict
from ConvertingApp_helper import KV

Window.size = (300, 500)

class ConvertingApp(MDApp):

    icons = []
    for i in range(33):
        icons.append(f"Flags\{i}.png")  #don't forget to write the path of the directory where the Flags file is stored 

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "400"

        self.root = Builder.load_string(KV)
        return self.root

    def callback_for_menu_items1(self, *args):
        """ Is assigns to the first label text the currency name selected
        by the user."""
        self.root.ids.label_item1.text = args[0]

    def show_example_list_bottom_sheet1(self):
        """ It shows the list of the currencies together with their flags.
        If an item from the list is selected the function
        callback_for_menu_items1(self, *args) is called.
        i = flag index"""

        bottom_sheet_menu = MDListBottomSheet()
        i = 0
        for key in exchange_dict:
            bottom_sheet_menu.add_item(
                f"{key}", lambda x, y=key: self.callback_for_menu_items1(f"{y}"),
            icon = self.icons[i]
            )
            i+=1
        bottom_sheet_menu.open()

    def callback_for_menu_items2(self, *args):
        """ It assigns to the second label text the currency name selected
        by the user."""
        self.root.ids.label_item2.text = args[0]

    def show_example_list_bottom_sheet2(self):
        """ It shows the list of the currencies together with their flags.
        If an item from the list is selected the function
        callback_for_menu_items2(self, *args) is called.
        i = flag index """

        bottom_sheet_menu = MDListBottomSheet()
        i = 0
        for key in exchange_dict:
            bottom_sheet_menu.add_item(
                f"{key}",
                lambda x, y=key: self.callback_for_menu_items2(
                    f"{y}"),
                icon = self.icons[i]
                )
            i +=1

        bottom_sheet_menu.open()

    def convert(self):
        """ It colects the information submitted by the user and uses the
        function from the module exchange_oop to make the exchange.
        It displays the conversion through the result_label.text.
        If an exception occurs a dialog box is displayed in order to inform the
        user to introduce an adequate value or to choose the currencies."""

        try:
            converted_currency = Ccy(self.root.ids.label_item1.text,
                                float(self.root.ids.user_input.text))
            converted_currency.Converting_Currency(self.root.ids.label_item2.text)
            self.root.ids.result_label.text = f"{str(converted_currency)}\
                                {symbols_dict[self.root.ids.label_item2.text]}"
        except ValueError:
            self.dialog = MDDialog(
                title = "Atenție!",text="Valoare necorespunzătoare!",
                type = "alert", size_hint= (0.6, 0.5),
                buttons=[
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color,
                        on_release = self.close_dialog),
                ],
            )
            self.dialog.open()
        except Exception:
            self.dialog = MDDialog(
                title = "Atenție!",text="Selectează moneda!",
                type = "alert", size_hint= (0.6, 0.5),
                buttons=[
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color,
                        on_release = self.close_dialog),
                ],
            )
            self.dialog.open()

    def close_dialog(self, instance):
        """It closes the dialog box."""

        self.dialog.dismiss()

    def clear_info(self):
        """ It erases all the inputs from the user and the result of the
        exchange."""

        self.root.ids.label_item1.text = "Monedă"
        self.root.ids.label_item2.text = "Monedă"
        self.root.ids.result_label.text = "Rezultat"
        self.root.ids.user_input.text = ""

ConvertingApp().run()
