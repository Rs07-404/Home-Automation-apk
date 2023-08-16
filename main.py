from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial
import requests


class HomeAutomate(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.firebase_url = "https://automate-switch-default-rtdb.firebaseio.com/devices/.json"
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        head = Label(text="Home Automate", font_size= 40, bold=True)
        layout.add_widget(head)

        device_1 = Device("Device 1")
        device_1.on_button.bind(on_release=partial(self.switch_on, device_1.name))
        device_1.off_button.bind(on_release=partial(self.switch_off, device_1.name))
        layout.add_widget(device_1.get_device_widget())

        device_2 = Device("Device 2")
        layout.add_widget(device_2.get_device_widget())
        device_2.on_button.bind(on_press=partial(self.switch_on, device_2.name))
        device_2.off_button.bind(on_press=partial(self.switch_off, device_2.name))

        device_3 = Device("Device 3")
        layout.add_widget(device_3.get_device_widget())
        device_3.on_button.bind(on_press=partial(self.switch_on, device_3.name))
        device_3.off_button.bind(on_press=partial(self.switch_off, device_3.name))

        device_4 = Device("Device 4")
        layout.add_widget(device_4.get_device_widget())
        device_4.on_button.bind(on_press=partial(self.switch_on, device_4.name))
        device_4.off_button.bind(on_press=partial(self.switch_off, device_4.name))

        return layout

    def switch_on(self, name, instance, **kwargs):
        data = {name: 1}
        requests.patch(url=self.firebase_url, json=data)


    def switch_off(self, name, instance, **kwargs):
        data = {name: 0}
        requests.patch(url=self.firebase_url, json=data)


class Device():
    def __init__(self, name):
        self.name = name
        self.device_layout = BoxLayout(orientation="horizontal", spacing=10, padding=10)
        self.device_layout.add_widget(Label(text=self.name, size_hint_x=None))
        self.on_button = Button(text="On", background_color="gold")
        self.off_button = Button(text="Off", background_color="dodgerblue")
        self.device_layout.add_widget(self.on_button)
        self.device_layout.add_widget(self.off_button)

    def get_device_widget(self):
        return self.device_layout


if __name__ == "__main__":
    HomeAutomate().run()

