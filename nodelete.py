from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
Window.size = (300,600)


class Player:
    def __init__(self, name):
        self.name = name

class HalamanUtama(Screen):
    def __init__(self, **kwargs):
        super(HalamanUtama, self).__init__(**kwargs)
        self.name = "halamanutama"
        self.layout = "layout_halaman_utama"

        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI TASK.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1), allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        details1 = Button(text= "Details",font_size=14, pos_hint= {"x":0.735,"top":0.760},size_hint=(0.185,0.03), background_color= (0,0,0,1))
        details1.bind(on_release= self.details1)
        global_layout.add_widget(details1)

        details2 = Button(text= "Details",font_size=14, pos_hint= {"x":0.735,"top":0.628},size_hint=(0.185,0.03), background_color= (0,0,0,1))
        details2.bind(on_release= self.details2)
        global_layout.add_widget(details2)

        details3 = Button(text= "Details",font_size=14, pos_hint= {"x":0.735,"top":0.485},size_hint=(0.185,0.03), background_color= (0,0,0,1))
        details3.bind(on_release= self.details3)
        global_layout.add_widget(details3)

        details4 = Button(text= "Details",font_size=14, pos_hint= {"x":0.735,"top":0.346},size_hint=(0.185,0.03), background_color= (0,0,0,1))
        details4.bind(on_release= self.details4)
        global_layout.add_widget(details4)

        details5 = Button(text= "Details",font_size=14, pos_hint= {"x":0.735,"top":0.215},size_hint=(0.185,0.03), background_color= (0,0,0,1))
        details5.bind(on_release= self.details5)
        global_layout.add_widget(details5)

        exambutton=Button(pos_hint= {"x": 0.438, "top": 0.085}, size_hint= (0.13, 0.085), background_color= (0, 0, 0, 0))
        exambutton.bind(on_release= self.exambutton)
        global_layout.add_widget(exambutton)

        exitbutton=Button(pos_hint= {"x": 0.75, "top": 0.085}, size_hint= (0.13, 0.085), background_color= (0, 0, 0, 0))
        exitbutton.bind(on_release= self.exitbutton)
        global_layout.add_widget(exitbutton)


    def exambutton (self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "left"

    def exitbutton (self, obj):
        App.get_running_app().stop()
        Window.close()

    def details1(self,*args):
        self.manager.current = "welcomewindow"

    def details2(self,*args):
        self.manager.current = "welcomewindoww"

    def details3(self,*args):
        self.manager.current = "welcomewindowww"

    def details4(self,*args):
        self.manager.current = "welcomewindowwww"

    def details5(self,*args):
        self.manager.current = "welcomewindowwwww"

class ExamList(Screen):
    def __init__(self, **kwargs):
        super(ExamList, self).__init__(**kwargs)
        self.name = "examlist"
        self.layout = "layout_exam_list"

        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI EXAM.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1), allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        details1 = Button(text= "Details",font_size=14, pos_hint= {"x":0.735,"top":0.760},size_hint=(0.185,0.03), background_color= (0,0,0,1))
        details1.bind(on_release= self.details1)
        global_layout.add_widget(details1)

        details2 = Button(text= "Details",font_size=14, pos_hint= {"x":0.735,"top":0.628},size_hint=(0.185,0.03), background_color= (0,0,0,1))
        details2.bind(on_release= self.details2)
        global_layout.add_widget(details2)

        details3 = Button(text= "Details",font_size=14, pos_hint= {"x":0.735,"top":0.490},size_hint=(0.185,0.03), background_color= (0,0,0,1))
        details3.bind(on_release= self.details3)
        global_layout.add_widget(details3)

        details4 = Button(text= "Details",font_size=14, pos_hint= {"x":0.735,"top":0.351},size_hint=(0.185,0.03), background_color= (0,0,0,1))
        details4.bind(on_release= self.details4)
        global_layout.add_widget(details4)

        details5 = Button(text= "Details",font_size=14, pos_hint= {"x":0.735,"top":0.220},size_hint=(0.185,0.03), background_color= (0,0,0,1))
        details5.bind(on_release= self.details5)
        global_layout.add_widget(details5)

        taskbutton=Button(pos_hint= {"x":0.1,"top":0.085}, size_hint= (0.13, 0.085), background_color= (0, 0, 0, 0))
        taskbutton.bind(on_release= self.taskbutton)
        global_layout.add_widget(taskbutton)

        exitbutton=Button(pos_hint= {"x": 0.75, "top": 0.085}, size_hint= (0.13, 0.085), background_color= (0, 0, 0, 0))
        exitbutton.bind(on_release= self.exitbutton)
        global_layout.add_widget(exitbutton)

    def taskbutton (self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def exitbutton (self, obj):
        App.get_running_app().stop()
        Window.close()

    def details1(self,*args):
        self.manager.current = "goodbyewindow"
        self.manager.transition.direction = "left"

    def details2(self,*args):
        self.manager.current = "goodbyewindoww"
        self.manager.transition.direction = "left"

    def details3(self,*args):
        self.manager.current = "goodbyewindowww"
        self.manager.transition.direction = "left"

    def details4(self,*args):
        self.manager.current = "goodbyewindowwww"
        self.manager.transition.direction = "left"

    def details5(self,*args):
        self.manager.current = "goodbyewindowwwww"
        self.manager.transition.direction = "left"

class WelcomeWindow(Screen):
    # Introduce names of the 4 players

    def __init__(self, **kwargs):
        super(WelcomeWindow, self).__init__(**kwargs)
        self.name = "welcomewindow"
        self.layout = "layout_welcome_window"

        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI ADD TASK.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        self.name_input_player_i = TextInput(id="player", text="Task 1", multiline=False, pos_hint= {'center_x':0.495, 'center_y':0.825}, size_hint= (0.9, 0.067)) # <--- user inputs name here
        global_layout.add_widget(self.name_input_player_i)

        self.name_input_player_ii = TextInput(id="taskdesc",hint_text= "Example: Video/Powerpoint/Thesis", multiline = False, pos_hint= {'center_x':0.495, 'center_y':0.710}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_ii)

        self.name_input_player_iii = TextInput(id="Deadline", hint_text= "DD-MM-YYYY", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.595}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iii)

        self.name_input_player_iv = TextInput(id="Reminder", hint_text= "DD-MM-YYYY , HH:MM", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.485}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iv)

        # Create button to go to next screen
        go_further_button = Button(pos_hint= {"x":0.72,"top":0.993},size_hint= (0.25,0.05), background_color= (0,0,0,0))
        go_further_button.bind(on_release=self.go_further)
        global_layout.add_widget(go_further_button)

        exambutton = Button(pos_hint={"x": 0.438, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exambutton.bind(on_release=self.exambutton)
        global_layout.add_widget(exambutton)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        backbutton =Button(pos_hint= {"x":0.045,"top":0.993},size_hint= (0.285,0.05), background_color= (0,0,0,0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

    def exambutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "left"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def go_further(self, *args):
        self.player1 = Player(self.name_input_player_i.text)# <--- name is assigned to player here
        self.player2 = Player(self.name_input_player_ii.text)
        self.player3 = Player(self.name_input_player_iii.text)
        self.player4 = Player(self.name_input_player_iv.text)
        self.manager.current = "firstround"
        self.manager.transition.direction = "left"

class WelcomeWindow2(Screen):
    # Introduce names of the 4 players

    def __init__(self, **kwargs):
        super(WelcomeWindow2, self).__init__(**kwargs)
        self.name = "welcomewindoww"
        self.layout = "layout_welcome_windoww"

        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI ADD TASK.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        self.name_input_player_i = TextInput(id="player", text="Task 2", multiline=False, pos_hint= {'center_x':0.495, 'center_y':0.825}, size_hint= (0.9, 0.067)) # <--- user inputs name here
        global_layout.add_widget(self.name_input_player_i)

        self.name_input_player_ii = TextInput(id="taskdesc",hint_text= "Example: Video/Powerpoint/Thesis", multiline = False, pos_hint= {'center_x':0.495, 'center_y':0.710}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_ii)

        self.name_input_player_iii = TextInput(id="Deadline", hint_text= "DD-MM-YYYY", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.595}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iii)

        self.name_input_player_iv = TextInput(id="Reminder", hint_text= "DD-MM-YYYY , HH:MM", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.485}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iv)

        # Create button to go to next screen
        go_further_button = Button(pos_hint= {"x":0.72,"top":0.993},size_hint= (0.25,0.05), background_color= (0,0,0,0))
        go_further_button.bind(on_release=self.go_further)
        global_layout.add_widget(go_further_button)

        exambutton = Button(pos_hint={"x": 0.438, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exambutton.bind(on_release=self.exambutton)
        global_layout.add_widget(exambutton)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        backbutton =Button(pos_hint= {"x":0.045,"top":0.993},size_hint= (0.285,0.05), background_color= (0,0,0,0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

    def exambutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "left"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def go_further(self, *args):
        self.player1 = Player(self.name_input_player_i.text)# <--- name is assigned to player here
        self.player2 = Player(self.name_input_player_ii.text)
        self.player3 = Player(self.name_input_player_iii.text)
        self.player4 = Player(self.name_input_player_iv.text)
        self.manager.current = "firstroundd"
        self.manager.transition.direction = "left"

class WelcomeWindow3(Screen):
    # Introduce names of the 4 players

    def __init__(self, **kwargs):
        super(WelcomeWindow3, self).__init__(**kwargs)
        self.name = "welcomewindowww"
        self.layout = "layout_welcome_windowww"

        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI ADD TASK.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        self.name_input_player_i = TextInput(id="player", text="Task 3", multiline=False, pos_hint= {'center_x':0.495, 'center_y':0.825}, size_hint= (0.9, 0.067)) # <--- user inputs name here
        global_layout.add_widget(self.name_input_player_i)

        self.name_input_player_ii = TextInput(id="taskdesc",hint_text= "Example: Video/Powerpoint/Thesis", multiline = False, pos_hint= {'center_x':0.495, 'center_y':0.710}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_ii)

        self.name_input_player_iii = TextInput(id="Deadline", hint_text= "DD-MM-YYYY", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.595}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iii)

        self.name_input_player_iv = TextInput(id="Reminder", hint_text= "DD-MM-YYYY , HH:MM", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.485}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iv)

        # Create button to go to next screen
        go_further_button = Button(pos_hint= {"x":0.72,"top":0.993},size_hint= (0.25,0.05), background_color= (0,0,0,0))
        go_further_button.bind(on_release=self.go_further)
        global_layout.add_widget(go_further_button)

        exambutton = Button(pos_hint={"x": 0.438, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exambutton.bind(on_release=self.exambutton)
        global_layout.add_widget(exambutton)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        backbutton =Button(pos_hint= {"x":0.045,"top":0.993},size_hint= (0.285,0.05), background_color= (0,0,0,0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

    def exambutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "left"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def go_further(self, *args):
        self.player1 = Player(self.name_input_player_i.text)# <--- name is assigned to player here
        self.player2 = Player(self.name_input_player_ii.text)
        self.player3 = Player(self.name_input_player_iii.text)
        self.player4 = Player(self.name_input_player_iv.text)
        self.manager.current = "firstrounddd"
        self.manager.transition.direction = "left"

class WelcomeWindow4(Screen):
    # Introduce names of the 4 players

    def __init__(self, **kwargs):
        super(WelcomeWindow4, self).__init__(**kwargs)
        self.name = "welcomewindowwww"
        self.layout = "layout_welcome_windowwww"

        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI ADD TASK.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        self.name_input_player_i = TextInput(id="player", text="Task 4", multiline=False, pos_hint= {'center_x':0.495, 'center_y':0.825}, size_hint= (0.9, 0.067)) # <--- user inputs name here
        global_layout.add_widget(self.name_input_player_i)

        self.name_input_player_ii = TextInput(id="taskdesc",hint_text= "Example: Video/Powerpoint/Thesis", multiline = False, pos_hint= {'center_x':0.495, 'center_y':0.710}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_ii)

        self.name_input_player_iii = TextInput(id="Deadline", hint_text= "DD-MM-YYYY", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.595}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iii)

        self.name_input_player_iv = TextInput(id="Reminder", hint_text= "DD-MM-YYYY , HH:MM", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.485}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iv)

        # Create button to go to next screen
        go_further_button = Button(pos_hint= {"x":0.72,"top":0.993},size_hint= (0.25,0.05), background_color= (0,0,0,0))
        go_further_button.bind(on_release=self.go_further)
        global_layout.add_widget(go_further_button)

        exambutton = Button(pos_hint={"x": 0.438, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exambutton.bind(on_release=self.exambutton)
        global_layout.add_widget(exambutton)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        backbutton =Button(pos_hint= {"x":0.045,"top":0.993},size_hint= (0.285,0.05), background_color= (0,0,0,0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

    def exambutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "left"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def go_further(self, *args):
        self.player1 = Player(self.name_input_player_i.text)# <--- name is assigned to player here
        self.player2 = Player(self.name_input_player_ii.text)
        self.player3 = Player(self.name_input_player_iii.text)
        self.player4 = Player(self.name_input_player_iv.text)
        self.manager.current = "firstroundddd"
        self.manager.transition.direction = "left"

class WelcomeWindow5(Screen):
    # Introduce names of the 4 players

    def __init__(self, **kwargs):
        super(WelcomeWindow5, self).__init__(**kwargs)
        self.name = "welcomewindowwwww"
        self.layout = "layout_welcome_windowwwww"

        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI ADD TASK.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        self.name_input_player_i = TextInput(id="player", text="Task 5", multiline=False, pos_hint= {'center_x':0.495, 'center_y':0.825}, size_hint= (0.9, 0.067)) # <--- user inputs name here
        global_layout.add_widget(self.name_input_player_i)

        self.name_input_player_ii = TextInput(id="taskdesc",hint_text= "Example: Video/Powerpoint/Thesis", multiline = False, pos_hint= {'center_x':0.495, 'center_y':0.710}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_ii)

        self.name_input_player_iii = TextInput(id="Deadline", hint_text= "DD-MM-YYYY", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.595}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iii)

        self.name_input_player_iv = TextInput(id="Reminder", hint_text= "DD-MM-YYYY , HH:MM", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.485}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iv)

        # Create button to go to next screen
        go_further_button = Button(pos_hint= {"x":0.72,"top":0.993},size_hint= (0.25,0.05), background_color= (0,0,0,0))
        go_further_button.bind(on_release=self.go_further)
        global_layout.add_widget(go_further_button)

        exambutton = Button(pos_hint={"x": 0.438, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exambutton.bind(on_release=self.exambutton)
        global_layout.add_widget(exambutton)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        backbutton =Button(pos_hint= {"x":0.045,"top":0.993},size_hint= (0.285,0.05), background_color= (0,0,0,0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

    def exambutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "left"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def go_further(self, *args):
        self.player1 = Player(self.name_input_player_i.text)# <--- name is assigned to player here
        self.player2 = Player(self.name_input_player_ii.text)
        self.player3 = Player(self.name_input_player_iii.text)
        self.player4 = Player(self.name_input_player_iv.text)
        self.manager.current = "firstrounddddd"
        self.manager.transition.direction = "left"

class FirstRound(Screen):
    #Give explanation of first round + option to add points for every player
    def __init__(self, **kwargs):
        super(FirstRound, self).__init__(**kwargs)
        self.name = "firstround"
        self.layout = "layout_first_round"

    def on_enter(self, *args):
        #Create layout
        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI DETAILS TASK 2.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        #Create Labels
        welcome_window = self.manager.get_screen('welcomewindow')  # get a reference to the WelcomeWindow instance
        label_player_name_i = Label(text=welcome_window.player1.name,color = (0,0,0,1), pos_hint = {'center_x':0.125, 'center_y':0.850}) # <--- Label should get the name of the player here
        label_player_name_ii = Label(text=welcome_window.player2.name, color=(0,0,0,1),  pos_hint= {'center_x':0.135, 'center_y':0.730})
        label_player_name_iii = Label(text=welcome_window.player3.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.158, 'center_y': 0.610})
        label_player_name_iv = Label(text=welcome_window.player4.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.240, 'center_y': 0.499})
        global_layout.add_widget(label_player_name_i)
        global_layout.add_widget(label_player_name_ii)
        global_layout.add_widget(label_player_name_iii)
        global_layout.add_widget(label_player_name_iv)

        exambutton = Button(pos_hint={"x": 0.438, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exambutton.bind(on_release=self.exambutton)
        global_layout.add_widget(exambutton)

        backbutton = Button(pos_hint={"x": 0.045, "top": 0.993}, size_hint=(0.285, 0.05), background_color=(0, 0, 0, 0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

    def exambutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "left"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"


class FirstRound2(Screen):
    #Give explanation of first round + option to add points for every player
    def __init__(self, **kwargs):
        super(FirstRound2, self).__init__(**kwargs)
        self.name = "firstroundd"
        self.layout = "layout_first_roundd"

    def on_enter(self, *args):
        #Create layout
        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI DETAILS TASK 2.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        #Create Labels
        welcome_windoww = self.manager.get_screen('welcomewindoww')  # get a reference to the WelcomeWindow instance
        label_player_name_i = Label(text=welcome_windoww.player1.name,color = (0,0,0,1), pos_hint = {'center_x':0.125, 'center_y':0.850}) # <--- Label should get the name of the player here
        label_player_name_ii = Label(text=welcome_windoww.player2.name, color=(0,0,0,1),  pos_hint= {'center_x':0.135, 'center_y':0.730})
        label_player_name_iii = Label(text=welcome_windoww.player3.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.158, 'center_y': 0.610})
        label_player_name_iv = Label(text=welcome_windoww.player4.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.240, 'center_y': 0.499})
        global_layout.add_widget(label_player_name_i)
        global_layout.add_widget(label_player_name_ii)
        global_layout.add_widget(label_player_name_iii)
        global_layout.add_widget(label_player_name_iv)

        exambutton = Button(pos_hint={"x": 0.438, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exambutton.bind(on_release=self.exambutton)
        global_layout.add_widget(exambutton)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        backbutton = Button(pos_hint={"x": 0.045, "top": 0.993}, size_hint=(0.285, 0.05), background_color=(0, 0, 0, 0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

    def backbutton(self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def exambutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "left"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

class FirstRound3(Screen):
    #Give explanation of first round + option to add points for every player
    def __init__(self, **kwargs):
        super(FirstRound3, self).__init__(**kwargs)
        self.name = "firstrounddd"
        self.layout = "layout_first_rounddd"

    def on_enter(self, *args):
        #Create layout
        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI DETAILS TASK 2.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        #Create Labels
        welcome_windowww = self.manager.get_screen('welcomewindowww')  # get a reference to the WelcomeWindow instance
        label_player_name_i = Label(text=welcome_windowww.player1.name,color = (0,0,0,1), pos_hint = {'center_x':0.125, 'center_y':0.850}) # <--- Label should get the name of the player here
        label_player_name_ii = Label(text=welcome_windowww.player2.name, color=(0,0,0,1),  pos_hint= {'center_x':0.135, 'center_y':0.730})
        label_player_name_iii = Label(text=welcome_windowww.player3.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.158, 'center_y': 0.610})
        label_player_name_iv = Label(text=welcome_windowww.player4.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.240, 'center_y': 0.499})
        global_layout.add_widget(label_player_name_i)
        global_layout.add_widget(label_player_name_ii)
        global_layout.add_widget(label_player_name_iii)
        global_layout.add_widget(label_player_name_iv)

        exambutton = Button(pos_hint={"x": 0.438, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exambutton.bind(on_release=self.exambutton)
        global_layout.add_widget(exambutton)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        backbutton = Button(pos_hint={"x": 0.045, "top": 0.993}, size_hint=(0.285, 0.05), background_color=(0, 0, 0, 0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

    def backbutton(self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def exambutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "left"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

class FirstRound4(Screen):
    #Give explanation of first round + option to add points for every player
    def __init__(self, **kwargs):
        super(FirstRound4, self).__init__(**kwargs)
        self.name = "firstroundddd"
        self.layout = "layout_first_roundddd"

    def on_enter(self, *args):
        #Create layout
        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI DETAILS TASK 2.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        #Create Labels
        welcome_windowwww = self.manager.get_screen('welcomewindowwww')  # get a reference to the WelcomeWindow instance
        label_player_name_i = Label(text=welcome_windowwww.player1.name,color = (0,0,0,1), pos_hint = {'center_x':0.125, 'center_y':0.850}) # <--- Label should get the name of the player here
        label_player_name_ii = Label(text=welcome_windowwww.player2.name, color=(0,0,0,1),  pos_hint= {'center_x':0.135, 'center_y':0.730})
        label_player_name_iii = Label(text=welcome_windowwww.player3.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.158, 'center_y': 0.610})
        label_player_name_iv = Label(text=welcome_windowwww.player4.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.240, 'center_y': 0.499})
        global_layout.add_widget(label_player_name_i)
        global_layout.add_widget(label_player_name_ii)
        global_layout.add_widget(label_player_name_iii)
        global_layout.add_widget(label_player_name_iv)

        exambutton = Button(pos_hint={"x": 0.438, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exambutton.bind(on_release=self.exambutton)
        global_layout.add_widget(exambutton)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        backbutton = Button(pos_hint={"x": 0.045, "top": 0.993}, size_hint=(0.285, 0.05), background_color=(0, 0, 0, 0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

    def backbutton(self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def exambutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "left"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

class FirstRound5(Screen):
    #Give explanation of first round + option to add points for every player
    def __init__(self, **kwargs):
        super(FirstRound5, self).__init__(**kwargs)
        self.name = "firstrounddddd"
        self.layout = "layout_first_rounddddd"

    def on_enter(self, *args):
        #Create layout
        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI DETAILS TASK 2.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        #Create Labels
        welcome_windowwwww = self.manager.get_screen('welcomewindowwwww')  # get a reference to the WelcomeWindow instance
        label_player_name_i = Label(text=welcome_windowwwww.player1.name,color = (0,0,0,1), pos_hint = {'center_x':0.125, 'center_y':0.850}) # <--- Label should get the name of the player here
        label_player_name_ii = Label(text=welcome_windowwwww.player2.name, color=(0,0,0,1),  pos_hint= {'center_x':0.135, 'center_y':0.730})
        label_player_name_iii = Label(text=welcome_windowwwww.player3.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.158, 'center_y': 0.610})
        label_player_name_iv = Label(text=welcome_windowwwww.player4.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.240, 'center_y': 0.499})
        global_layout.add_widget(label_player_name_i)
        global_layout.add_widget(label_player_name_ii)
        global_layout.add_widget(label_player_name_iii)
        global_layout.add_widget(label_player_name_iv)

        exambutton = Button(pos_hint={"x": 0.438, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exambutton.bind(on_release=self.exambutton)
        global_layout.add_widget(exambutton)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        backbutton = Button(pos_hint={"x": 0.045, "top": 0.993}, size_hint=(0.285, 0.05), background_color=(0, 0, 0, 0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

    def backbutton(self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def exambutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "left"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

class GoodbyeWindow(Screen):
    # Introduce names of the 4 players

    def __init__(self, **kwargs):
        super(GoodbyeWindow, self).__init__(**kwargs)
        self.name = "goodbyewindow"
        self.layout = "layout_goodbye_window"

        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI ADD EXAM.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        self.name_input_player_i = TextInput(id="player", text="Exam 1", multiline=False, pos_hint= {'center_x':0.495, 'center_y':0.825}, size_hint= (0.9, 0.067)) # <--- user inputs name here
        global_layout.add_widget(self.name_input_player_i)

        self.name_input_player_ii = TextInput(id="taskdesc",hint_text= "Example: Calculation/Essay", multiline = False, pos_hint= {'center_x':0.495, 'center_y':0.710}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_ii)

        self.name_input_player_iii = TextInput(id="Deadline", hint_text= "DD-MM-YYYY", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.595}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iii)

        self.name_input_player_iv = TextInput(id="Reminder", hint_text= "DD-MM-YYYY , HH:MM", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.485}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iv)

        # Create button to go to next screen
        go_further_button = Button(pos_hint= {"x":0.72,"top":0.993},size_hint= (0.25,0.05), background_color= (0,0,0,0))
        go_further_button.bind(on_release=self.go_further)
        global_layout.add_widget(go_further_button)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        backbutton =Button(pos_hint= {"x":0.045,"top":0.993},size_hint= (0.285,0.05), background_color= (0,0,0,0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

        taskbutton = Button(pos_hint={"x": 0.1, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        taskbutton.bind(on_release=self.taskbutton)
        global_layout.add_widget(taskbutton)

    def taskbutton (self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "right"

    def go_further(self, *args):
        self.player1 = Player(self.name_input_player_i.text)# <--- name is assigned to player here
        self.player2 = Player(self.name_input_player_ii.text)
        self.player3 = Player(self.name_input_player_iii.text)
        self.player4 = Player(self.name_input_player_iv.text)
        self.manager.current = "secondround"
        self.manager.transition.direction = "left"

class GoodbyeWindow2(Screen):
    # Introduce names of the 4 players

    def __init__(self, **kwargs):
        super(GoodbyeWindow2, self).__init__(**kwargs)
        self.name = "goodbyewindoww"
        self.layout = "layout_goodbye_windoww"

        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI ADD EXAM.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        self.name_input_player_i = TextInput(id="player", text="Exam 2", multiline=False, pos_hint= {'center_x':0.495, 'center_y':0.825}, size_hint= (0.9, 0.067)) # <--- user inputs name here
        global_layout.add_widget(self.name_input_player_i)

        self.name_input_player_ii = TextInput(id="taskdesc",hint_text= "Example: Calculation/Essay", multiline = False, pos_hint= {'center_x':0.495, 'center_y':0.710}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_ii)

        self.name_input_player_iii = TextInput(id="Deadline", hint_text= "DD-MM-YYYY", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.595}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iii)

        self.name_input_player_iv = TextInput(id="Reminder", hint_text= "DD-MM-YYYY , HH:MM", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.485}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iv)

        # Create button to go to next screen
        go_further_button = Button(pos_hint= {"x":0.72,"top":0.993},size_hint= (0.25,0.05), background_color= (0,0,0,0))
        go_further_button.bind(on_release=self.go_further)
        global_layout.add_widget(go_further_button)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        backbutton =Button(pos_hint= {"x":0.045,"top":0.993},size_hint= (0.285,0.05), background_color= (0,0,0,0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

        taskbutton = Button(pos_hint={"x": 0.1, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        taskbutton.bind(on_release=self.taskbutton)
        global_layout.add_widget(taskbutton)

    def taskbutton (self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "right"

    def go_further(self, *args):
        self.player1 = Player(self.name_input_player_i.text)# <--- name is assigned to player here
        self.player2 = Player(self.name_input_player_ii.text)
        self.player3 = Player(self.name_input_player_iii.text)
        self.player4 = Player(self.name_input_player_iv.text)
        self.manager.current = "secondroundd"
        self.manager.transition.direction = "left"

class GoodbyeWindow3(Screen):
    # Introduce names of the 4 players

    def __init__(self, **kwargs):
        super(GoodbyeWindow3, self).__init__(**kwargs)
        self.name = "goodbyewindowww"
        self.layout = "layout_goodbye_windowww"

        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI ADD EXAM.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        self.name_input_player_i = TextInput(id="player", text="Exam 3", multiline=False, pos_hint= {'center_x':0.495, 'center_y':0.825}, size_hint= (0.9, 0.067)) # <--- user inputs name here
        global_layout.add_widget(self.name_input_player_i)

        self.name_input_player_ii = TextInput(id="taskdesc",hint_text= "Example: Calculation/Essay", multiline = False, pos_hint= {'center_x':0.495, 'center_y':0.710}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_ii)

        self.name_input_player_iii = TextInput(id="Deadline", hint_text= "DD-MM-YYYY", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.595}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iii)

        self.name_input_player_iv = TextInput(id="Reminder", hint_text= "DD-MM-YYYY , HH:MM", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.485}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iv)

        # Create button to go to next screen
        go_further_button = Button(pos_hint= {"x":0.72,"top":0.993},size_hint= (0.25,0.05), background_color= (0,0,0,0))
        go_further_button.bind(on_release=self.go_further)
        global_layout.add_widget(go_further_button)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        backbutton =Button(pos_hint= {"x":0.045,"top":0.993},size_hint= (0.285,0.05), background_color= (0,0,0,0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

        taskbutton = Button(pos_hint={"x": 0.1, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        taskbutton.bind(on_release=self.taskbutton)
        global_layout.add_widget(taskbutton)

    def taskbutton (self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "right"

    def go_further(self, *args):
        self.player1 = Player(self.name_input_player_i.text)# <--- name is assigned to player here
        self.player2 = Player(self.name_input_player_ii.text)
        self.player3 = Player(self.name_input_player_iii.text)
        self.player4 = Player(self.name_input_player_iv.text)
        self.manager.current = "secondrounddd"
        self.manager.transition.direction = "left"

class GoodbyeWindow4(Screen):
    # Introduce names of the 4 players

    def __init__(self, **kwargs):
        super(GoodbyeWindow4, self).__init__(**kwargs)
        self.name = "goodbyewindowwww"
        self.layout = "layout_goodbye_windowwww"

        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI ADD EXAM.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        self.name_input_player_i = TextInput(id="player", text="Exam 4", multiline=False, pos_hint= {'center_x':0.495, 'center_y':0.825}, size_hint= (0.9, 0.067)) # <--- user inputs name here
        global_layout.add_widget(self.name_input_player_i)

        self.name_input_player_ii = TextInput(id="taskdesc",hint_text= "Example: Calculation/Essay", multiline = False, pos_hint= {'center_x':0.495, 'center_y':0.710}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_ii)

        self.name_input_player_iii = TextInput(id="Deadline", hint_text= "DD-MM-YYYY", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.595}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iii)

        self.name_input_player_iv = TextInput(id="Reminder", hint_text= "DD-MM-YYYY , HH:MM", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.485}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iv)

        # Create button to go to next screen
        go_further_button = Button(pos_hint= {"x":0.72,"top":0.993},size_hint= (0.25,0.05), background_color= (0,0,0,0))
        go_further_button.bind(on_release=self.go_further)
        global_layout.add_widget(go_further_button)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        backbutton =Button(pos_hint= {"x":0.045,"top":0.993},size_hint= (0.285,0.05), background_color= (0,0,0,0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

        taskbutton = Button(pos_hint={"x": 0.1, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        taskbutton.bind(on_release=self.taskbutton)
        global_layout.add_widget(taskbutton)

    def taskbutton (self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "right"

    def go_further(self, *args):
        self.player1 = Player(self.name_input_player_i.text)# <--- name is assigned to player here
        self.player2 = Player(self.name_input_player_ii.text)
        self.player3 = Player(self.name_input_player_iii.text)
        self.player4 = Player(self.name_input_player_iv.text)
        self.manager.current = "secondroundddd"
        self.manager.transition.direction = "left"

class GoodbyeWindow5(Screen):
    # Introduce names of the 4 players

    def __init__(self, **kwargs):
        super(GoodbyeWindow5, self).__init__(**kwargs)
        self.name = "goodbyewindowwwww"
        self.layout = "layout_goodbye_windowwwww"

        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI ADD EXAM.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        self.name_input_player_i = TextInput(id="player", text="Exam 5", multiline=False, pos_hint= {'center_x':0.495, 'center_y':0.825}, size_hint= (0.9, 0.067)) # <--- user inputs name here
        global_layout.add_widget(self.name_input_player_i)

        self.name_input_player_ii = TextInput(id="taskdesc",hint_text= "Example: Calculation/Essay", multiline = False, pos_hint= {'center_x':0.495, 'center_y':0.710}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_ii)

        self.name_input_player_iii = TextInput(id="Deadline", hint_text= "DD-MM-YYYY", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.595}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iii)

        self.name_input_player_iv = TextInput(id="Reminder", hint_text= "DD-MM-YYYY , HH:MM", multiline = False, pos_hint = {'center_x':0.495, 'center_y':0.485}, size_hint= (0.9,0.067))
        global_layout.add_widget(self.name_input_player_iv)

        # Create button to go to next screen
        go_further_button = Button(pos_hint= {"x":0.72,"top":0.993},size_hint= (0.25,0.05), background_color= (0,0,0,0))
        go_further_button.bind(on_release=self.go_further)
        global_layout.add_widget(go_further_button)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        backbutton =Button(pos_hint= {"x":0.045,"top":0.993},size_hint= (0.285,0.05), background_color= (0,0,0,0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

        taskbutton = Button(pos_hint={"x": 0.1, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        taskbutton.bind(on_release=self.taskbutton)
        global_layout.add_widget(taskbutton)

    def taskbutton (self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "right"

    def go_further(self, *args):
        self.player1 = Player(self.name_input_player_i.text)# <--- name is assigned to player here
        self.player2 = Player(self.name_input_player_ii.text)
        self.player3 = Player(self.name_input_player_iii.text)
        self.player4 = Player(self.name_input_player_iv.text)
        self.manager.current = "secondrounddddd"
        self.manager.transition.direction = "left"

class SecondRound(Screen):
    #Give explanation of first round + option to add points for every player
    def __init__(self, **kwargs):
        super(SecondRound, self).__init__(**kwargs)
        self.name = "secondround"
        self.layout = "layout_second_round"

    def on_enter(self, *args):
        #Create layout
        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI DETAILS EXAM 2.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        #Create Labels
        goodbye_window = self.manager.get_screen('goodbyewindow')  # get a reference to the WelcomeWindow instance
        label_player_name_i = Label(text=goodbye_window.player1.name,color = (0,0,0,1), pos_hint = {'center_x':0.125, 'center_y':0.847}) # <--- Label should get the name of the player here
        label_player_name_ii = Label(text=goodbye_window.player2.name, color=(0,0,0,1),  pos_hint=  {'center_x':0.127, 'center_y':0.725})
        label_player_name_iii = Label(text=goodbye_window.player3.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.160, 'center_y': 0.605})
        label_player_name_iv = Label(text=goodbye_window.player4.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.240, 'center_y': 0.490})
        global_layout.add_widget(label_player_name_i)
        global_layout.add_widget(label_player_name_ii)
        global_layout.add_widget(label_player_name_iii)
        global_layout.add_widget(label_player_name_iv)

        backbutton = Button(pos_hint={"x": 0.045, "top": 0.993}, size_hint=(0.285, 0.05), background_color=(0, 0, 0, 0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        taskbutton = Button(pos_hint={"x": 0.1, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        taskbutton.bind(on_release=self.taskbutton)
        global_layout.add_widget(taskbutton)

    def taskbutton (self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "right"

class SecondRound2(Screen):
    #Give explanation of first round + option to add points for every player
    def __init__(self, **kwargs):
        super(SecondRound2, self).__init__(**kwargs)
        self.name = "secondroundd"
        self.layout = "layout_second_roundd"

    def on_enter(self, *args):
        #Create layout
        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI DETAILS EXAM 2.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        #Create Labels
        goodbye_windoww = self.manager.get_screen('goodbyewindoww')  # get a reference to the WelcomeWindow instance
        label_player_name_i = Label(text=goodbye_windoww.player1.name,color = (0,0,0,1), pos_hint = {'center_x':0.125, 'center_y':0.847}) # <--- Label should get the name of the player here
        label_player_name_ii = Label(text=goodbye_windoww.player2.name, color=(0,0,0,1),  pos_hint=  {'center_x':0.127, 'center_y':0.725})
        label_player_name_iii = Label(text=goodbye_windoww.player3.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.160, 'center_y': 0.605})
        label_player_name_iv = Label(text=goodbye_windoww.player4.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.240, 'center_y': 0.490})
        global_layout.add_widget(label_player_name_i)
        global_layout.add_widget(label_player_name_ii)
        global_layout.add_widget(label_player_name_iii)
        global_layout.add_widget(label_player_name_iv)

        backbutton = Button(pos_hint={"x": 0.045, "top": 0.993}, size_hint=(0.285, 0.05), background_color=(0, 0, 0, 0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        taskbutton = Button(pos_hint={"x": 0.1, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        taskbutton.bind(on_release=self.taskbutton)
        global_layout.add_widget(taskbutton)

    def taskbutton (self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "right"

class SecondRound3(Screen):
    #Give explanation of first round + option to add points for every player
    def __init__(self, **kwargs):
        super(SecondRound3, self).__init__(**kwargs)
        self.name = "secondrounddd"
        self.layout = "layout_second_rounddd"

    def on_enter(self, *args):
        #Create layout
        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI DETAILS EXAM 2.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        #Create Labels
        goodbye_windowww = self.manager.get_screen('goodbyewindowww')  # get a reference to the WelcomeWindow instance
        label_player_name_i = Label(text=goodbye_windowww.player1.name,color = (0,0,0,1), pos_hint = {'center_x':0.125, 'center_y':0.847}) # <--- Label should get the name of the player here
        label_player_name_ii = Label(text=goodbye_windowww.player2.name, color=(0,0,0,1),  pos_hint=   {'center_x':0.127, 'center_y':0.725})
        label_player_name_iii = Label(text=goodbye_windowww.player3.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.160, 'center_y': 0.605})
        label_player_name_iv = Label(text=goodbye_windowww.player4.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.240, 'center_y': 0.490})
        global_layout.add_widget(label_player_name_i)
        global_layout.add_widget(label_player_name_ii)
        global_layout.add_widget(label_player_name_iii)
        global_layout.add_widget(label_player_name_iv)

        backbutton = Button(pos_hint={"x": 0.045, "top": 0.993}, size_hint=(0.285, 0.05), background_color=(0, 0, 0, 0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        taskbutton = Button(pos_hint={"x": 0.1, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        taskbutton.bind(on_release=self.taskbutton)
        global_layout.add_widget(taskbutton)

    def taskbutton (self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "right"

class SecondRound4(Screen):
    #Give explanation of first round + option to add points for every player
    def __init__(self, **kwargs):
        super(SecondRound4, self).__init__(**kwargs)
        self.name = "secondroundddd"
        self.layout = "layout_second_roundddd"

    def on_enter(self, *args):
        #Create layout
        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI DETAILS EXAM 2.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        #Create Labels
        goodbye_windowwww = self.manager.get_screen('goodbyewindowwww')  # get a reference to the WelcomeWindow instance
        label_player_name_i = Label(text=goodbye_windowwww.player1.name,color = (0,0,0,1), pos_hint = {'center_x':0.125, 'center_y':0.847}) # <--- Label should get the name of the player here
        label_player_name_ii = Label(text=goodbye_windowwww.player2.name, color=(0,0,0,1),  pos_hint=   {'center_x':0.127, 'center_y':0.725})
        label_player_name_iii = Label(text=goodbye_windowwww.player3.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.160, 'center_y': 0.605})
        label_player_name_iv = Label(text=goodbye_windowwww.player4.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.240, 'center_y': 0.490})
        global_layout.add_widget(label_player_name_i)
        global_layout.add_widget(label_player_name_ii)
        global_layout.add_widget(label_player_name_iii)
        global_layout.add_widget(label_player_name_iv)

        backbutton = Button(pos_hint={"x": 0.045, "top": 0.993}, size_hint=(0.285, 0.05), background_color=(0, 0, 0, 0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        taskbutton = Button(pos_hint={"x": 0.1, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        taskbutton.bind(on_release=self.taskbutton)
        global_layout.add_widget(taskbutton)

    def taskbutton (self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "right"

class SecondRound5(Screen):
    #Give explanation of first round + option to add points for every player
    def __init__(self, **kwargs):
        super(SecondRound5, self).__init__(**kwargs)
        self.name = "secondrounddddd"
        self.layout = "layout_second_rounddddd"

    def on_enter(self, *args):
        #Create layout
        global_layout = FloatLayout()
        self.add_widget(global_layout)

        self.image = Image(source='REVISI DETAILS EXAM 2.jpeg', pos_hint={'left': 1, 'top': 1}, size_hint=(1, 1),
                           allow_stretch=True, keep_ratio=False)
        global_layout.add_widget(self.image)

        #Create Labels
        goodbye_windowwwww = self.manager.get_screen('goodbyewindowwwww')  # get a reference to the WelcomeWindow instance
        label_player_name_i = Label(text=goodbye_windowwwww.player1.name,color = (0,0,0,1), pos_hint = {'center_x':0.125, 'center_y':0.847}) # <--- Label should get the name of the player here
        label_player_name_ii = Label(text=goodbye_windowwwww.player2.name, color=(0,0,0,1),  pos_hint= {'center_x':0.127, 'center_y':0.725})
        label_player_name_iii = Label(text=goodbye_windowwwww.player3.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.160, 'center_y': 0.605})
        label_player_name_iv = Label(text=goodbye_windowwwww.player4.name, color=(0, 0, 0, 1), pos_hint={'center_x': 0.240, 'center_y': 0.490})
        global_layout.add_widget(label_player_name_i)
        global_layout.add_widget(label_player_name_ii)
        global_layout.add_widget(label_player_name_iii)
        global_layout.add_widget(label_player_name_iv)

        backbutton = Button(pos_hint={"x": 0.045, "top": 0.993}, size_hint=(0.285, 0.05), background_color=(0, 0, 0, 0))
        backbutton.bind(on_release=self.backbutton)
        global_layout.add_widget(backbutton)

        exitbutton = Button(pos_hint={"x": 0.75, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        exitbutton.bind(on_release=self.exitbutton)
        global_layout.add_widget(exitbutton)

        taskbutton = Button(pos_hint={"x": 0.1, "top": 0.085}, size_hint=(0.13, 0.085), background_color=(0, 0, 0, 0))
        taskbutton.bind(on_release=self.taskbutton)
        global_layout.add_widget(taskbutton)

    def taskbutton (self, *args):
        self.manager.current = "halamanutama"
        self.manager.transition.direction = "right"

    def exitbutton(self, obj):
        App.get_running_app().stop()
        Window.close()

    def backbutton(self, *args):
        self.manager.current = "examlist"
        self.manager.transition.direction = "right"

WindowManager = ScreenManager()
WindowManager.add_widget(HalamanUtama())
WindowManager.add_widget(ExamList())
WindowManager.add_widget(WelcomeWindow())
WindowManager.add_widget(WelcomeWindow2())
WindowManager.add_widget(WelcomeWindow3())
WindowManager.add_widget(WelcomeWindow4())
WindowManager.add_widget(WelcomeWindow5())
WindowManager.add_widget(FirstRound())
WindowManager.add_widget(FirstRound2())
WindowManager.add_widget(FirstRound3())
WindowManager.add_widget(FirstRound4())
WindowManager.add_widget(FirstRound5())
WindowManager.add_widget(GoodbyeWindow())
WindowManager.add_widget(GoodbyeWindow2())
WindowManager.add_widget(GoodbyeWindow3())
WindowManager.add_widget(GoodbyeWindow4())
WindowManager.add_widget(GoodbyeWindow5())
WindowManager.add_widget(SecondRound())
WindowManager.add_widget(SecondRound2())
WindowManager.add_widget(SecondRound3())
WindowManager.add_widget(SecondRound4())
WindowManager.add_widget(SecondRound5())

class LYPApp(App):
    def build(self):
        return WindowManager
    def vibrate(self, time):
        vibrator.vibrate(time=5)
    def pattern(self, pattern):
        vibrator.pattern([0, 0, 1, 2])
    def exists(self):
        return self._exists()
    def cancel(self):
        self._cancel()

        # private
    def _vibrate(self, **kwargs):
        raise NotImplementedError()
    def _pattern(self, **kwargs):
        raise NotImplementedError()
    def _exists(self, **kwargs):
        raise NotImplementedError()
    def _cancel(self, **kwargs):
        raise NotImplementedError()

if _name_ == "_main_":
    LYPApp().run()
