import pygame
from Nivel import *
from modo import *
from class_plataforma import *
from class_personaje import *
from Configuraciones import *

class NivelDos(Nivel):
    def __init__(self,  pantalla: pygame.Surface):
        W = pantalla.get_width()
        H = pantalla.get_height()

        #FONDO
        fondo = pygame.image.load("Ecenarios/Nivel_2.jpg")
        fondo = pygame.transform.scale(fondo, (W,H))

        
        #PERSONAJE
        posicion = (W/2 - 650, 182)
        tamaño = (40,80)

        diccionario_animaciones = {}
        diccionario_animaciones["quieto"] = personaje_quieto
        diccionario_animaciones["salta"] = personaje_salta
        diccionario_animaciones["camina_derecha"] = personaje_camina_derecha
        diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda

        mi_personaje = Personaje(posicion, 10, tamaño, diccionario_animaciones)

        piso = Plataforma((0, mi_personaje.lados["main"].bottom), (154,77))
        piso_2 = Plataforma((0,340),(77,77))
        piso_3 = Plataforma((0,416),(35,30))
        piso_4 = Plataforma((0,447),(40,77))
        piso_5 = Plataforma((0,521),(34,80))
        piso_6 = Plataforma((0,601),(231,77))
        piso_7 = Plataforma((0,818),(W,45))
        piso_8 = Plataforma((779,685),(133,133))
        piso_9 = Plataforma((833,608),(77,77))
        piso_10 = Plataforma((912,420),(130,399))

        #pisos que se caen
        plataforma_1 = Plataforma((460, 556),(150,30), "Plataformas/piso/0.png")
        plataforma_2 = Plataforma((248, 466),(150,30), "Plataformas/piso/0.png")
        plataforma_3 = Plataforma((490, 360),(150,30), "Plataformas/piso/0.png")
        plataforma_4 = Plataforma((700, 401),(150,30), "Plataformas/piso/0.png")
        plataforma_5 = Plataforma((709, 759),(70,60), "Plataformas/piso/0.png")


        lista_plataformas = [piso, plataforma_1, plataforma_2, plataforma_3, plataforma_4, plataforma_5, piso_2, piso_3, piso_4, piso_5, piso_6, piso_7, piso_8, piso_9, piso_10]

        super().__init__(pantalla, mi_personaje, lista_plataformas, fondo)