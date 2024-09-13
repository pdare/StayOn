from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from stayon import StayOnC


#kv = Builder.load_file(os.path.join(ROOT_DIR, "RunChecksApp.kv"))
WindowWidth = '400'
WindowHeight = '100'
Config.set('graphics', 'width', WindowWidth)
Config.set('graphics', 'height', WindowHeight)

class MyBoxLayout(BoxLayout):
    pass

class RunStayOnApp(App):
    def build(self):
        return MyBoxLayout()
    
    def beginStayOn(self):
        print("running stay on \n")
        self.stay_on = StayOnC()
        self.stay_on.runStayOn()

if __name__ == '__main__':
    RunStayOnApp().run()