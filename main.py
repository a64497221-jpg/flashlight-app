from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import sys  # <-- قم باستيراد هذه المكتبة في الأعلى

try:
    from plyer import flash
except ImportError:
    flash = None

Window.size = (390, 740)

class MainContainer(BoxLayout):
    def __init__(self, **kwargs):
        super(MainContainer, self).__init__(**kwargs)

    def turn_on(self, button_instance):
        if flash: 
            flash.on()
        print("Flash ON & App Closing")
        
        # --- سطر واحد فقط لإغلاق التطبيق ---
        sys.exit() 

    def turn_off(self, button_instance):
        if flash: 
            flash.off()
        print("Flash OFF")
        # لا داعي لإظهار الزر مرة أخرى لأن التطبيق سيُغلق.

    def show_settings(self, *args):
        self.ids.home_view.opacity = 0
        self.ids.home_view.disabled = True
        self.ids.settings_view.opacity = 1
        self.ids.settings_view.disabled = False

    def show_home(self, *args):
        self.ids.home_view.opacity = 1
        self.ids.home_view.disabled = False
        self.ids.settings_view.opacity = 0
        self.ids.settings_view.disabled = True

class MainApp(App):
    def build(self):
        self.title = "AMMAR ALJYNIED"
        return MainContainer()

if __name__ == '__main__':
    MainApp().run()