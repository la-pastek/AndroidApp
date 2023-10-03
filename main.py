from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from KV import KV


class LoginScreen(Screen):
    pass
class HelloScreen(Screen):
    pass
class LoginApp(MDApp):

    sm = ScreenManager()
    sm.add_widget(LoginScreen(name='login'))
    sm.add_widget(HelloScreen(name='hello'))
    def login(self):
        username = self.root.get_screen('login').ids.username.text
        password = self.root.get_screen('login').ids.password.text
        if username == "ok" and password == "ok":
            # Chargez la nouvelle page (écran) "HelloScreen"
            self.root.current = 'hello'
        else:
            print("Nom d'utilisateur ou mot de passe incorrect")
    def build(self):
        screen = Builder.load_string(KV)
        return screen
LoginApp().run()
