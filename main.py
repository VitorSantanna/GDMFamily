
#Author: João Vitor Sant' Anna
##################
####GDM Family####
##################

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class TelaPrincipal(FloatLayout):
    def click(self):
        gdm.title = "Membros da GDM"
        gdm.root_window.remove_widget(gdm.root)
        gdm.root_window.add_widget(Tela2())


class Tela2(FloatLayout):
    def click(self):
        gdm.root_window.remove_widget(gdm.root)
        gdm.root_window.add_widget(TelaPrincipal())


class GDMFamilyApp(App):
        def build(self):
            self.icon = 'icon.jpg'
            pass


gdm = GDMFamilyApp()
gdm.run()

