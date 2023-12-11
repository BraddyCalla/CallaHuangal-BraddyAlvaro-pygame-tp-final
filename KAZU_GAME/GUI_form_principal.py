import pygame
from pygame.locals import *

from GUI_button import *
from GUI_slider import *
from GUI_textbox import *
from GUI_label import *
from GUI_form import *
from GUI_button_image import *
from GUI_form_menu_score import *
from GUI_form_menu_play import *
from GUI_checkbox import *

class FormPrincipal(Form):
    def __init__(self, screen, x,y,w,h, color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen,x,y,w,h,color_background,color_border,border_size,active)

        self.volumen = 0.2
        self.flag_play = True
        pygame.mixer.init()

        ##Controles##
        self.txtbox = TextBox(self._slave, x, y, 130, 50, 150, 30, (180,168,154),"White", (42,12,15), (0,105,37), 2,font = "Arial",font_size=15,font_color = "Black")
        self.btn_play = CheckBox(self._slave, x, y, 130,100,50,50,"Interfaz/Music_On.png","Interfaz/Music_Off.png")
        self.label_volumen = Label(self._slave, 650, 190, 100, 50, "20%", "Arial", 15, "White", "Interfaz/Table2.png")
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 500, 15, self.volumen, (42,12,15), (0,105,37))
        self.btn_tabla = Button_Image(self._slave, x, y, 360, 100, 50, 50, "Interfaz/Menu_BTN.png", self.btn_tabla_click, "xd")

        self.btn_jugar = Button_Image(self._slave, x,y, 220, 100, 120, 50, "Interfaz/Play.png", self. btn_jugar_click, "a")

        #Agrego los controles a la lista
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_jugar)

        pygame.mixer.music.load("Sound/Fondo/Nivel_1.mp3")

        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.render()


    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
                
                if self.btn_play.get_esta_prendido():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                self.flag_play = not self.flag_play
        else:
            self.hijo.update(lista_eventos)
    
    def render(self):
        self._slave.fill(self._color_background)

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen *100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_tabla_click(self, texto):
        dic_score = [{"Jugador":"Tomi", "Score": 1000},
                     {"Jugador":"Oliver", "Score": 5000},
                     {"Jugador":"Henry", "Score": 2500}]
        form_puntaje = FormMenuScore(self._master,
                                     250,
                                     25,
                                     500,
                                     550,
                                     (220,0,220),
                                     "White",
                                     True,
                                     "Interfaz/Window.png",
                                     dic_score,
                                     100,
                                     10,
                                     10)
        self.show_dialog(form_puntaje)

    def btn_jugar_click(self, param):
        frm_jugar = FormMenuPlay(screen = self._master,
                                 x=self._master.get_width()/2 - 350,
                                 y = self._master.get_height()/2 - 350,
                                 w = 500,
                                 h = 500,
                                 color_background = (220,0,220),
                                 color_border = (0,105,37),
                                 active = True, path_image = "Interfaz/Window.png")
        self.show_dialog(frm_jugar)




