from kivy.app import App
from kivymd.theming import ThemeManager
from kivymd.toast import toast
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.popupscreen import MDPopupScreen
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog

class Main2App(App):
    theme_cls = ThemeManager()




    def show_MDDialog(self):
        my_dialog = MDDialog(title = 'Contact Me', text = 'Whatsapp:\n 07032867046\n \nFacebook: \nSteve Simon HashTag', size_hint = [.5, .5], auto_dismiss = False,
                             events_callback = self.my_callback,)

        my_dialog.open()

    def my_callback(self, text_of_selection, popup_widget):
        print(text_of_selection)
    def waneneAllah(self):
        toast('Wanene Allah')

    def aduaUbanmu(self):
        toast('Invocation')

    def shedarBangaskiya(self):
        toast('Call to confession')

    def affirm(self):
        toast('Affirmation of Faith')

    def wakanBishara(self):
        toast('General confession')

    def adduaNemanGafara(self):
        toast('Words Of Assurance')

    def lordsPrayer(self):
        toast('Our Lords Prayer')

    def psalter(self):
        toast('Psalter')

    def scriptureReading(self):
        toast('Scripture Reading')

    def affirmation(self):
        toast('Affirmation of faith')

    def affirmation(self):
        toast('Pastoral Prayer')

    def affirmation(self):
        toast('Affirmation of faith')

    def pastoral(self):
        toast('Pastoral Prayer')

    def offertory(self):
        toast('Offering')

    def hymn(self):
        toast('Hymnal')

    def sermon(self):
        toast('Sermon Time')

    def benediction(self):
        toast('Benediction')

    def postlude(self):
        toast('Postlude')





Main2App().run()