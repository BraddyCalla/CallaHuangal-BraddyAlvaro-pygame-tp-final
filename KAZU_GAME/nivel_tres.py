import pygame
from Nivel import *
from modo import *
from class_plataforma import *
from class_personaje import *
from Configuraciones import *

class NivelTres(Nivel):
    def __init__(self,  pantalla: pygame.Surface):
        W = pantalla.get_width()
        H = pantalla.get_height()

        #FONDO
        fondo = pygame.image.load("Ecenarios/Nivel_3.jpg")
        fondo = pygame.transform.scale(fondo, (W,H))

        
        #PERSONAJE
        posicion = (W/2 - 650, 673)
        tamaño = (40,80)

        diccionario_animaciones = {}
        diccionario_animaciones["quieto"] = personaje_quieto
        diccionario_animaciones["salta"] = personaje_salta
        diccionario_animaciones["camina_derecha"] = personaje_camina_derecha
        diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda

        mi_personaje = Personaje(posicion, 10, tamaño, diccionario_animaciones)

        piso = Plataforma((0, mi_personaje.lados["main"].bottom), (W,77))
        piso_2 = Plataforma((799,645),(110,110))
        piso_3 = Plataforma((855,533),(423,110))
        piso_4 = Plataforma((1076,481),(202,53))
        piso_5 = Plataforma((1148,427),(100,53))

        #pisos que se caen
        plataforma_1 = Plataforma((460,556),(150,30), "Plataformas/piso/0.png")
        plataforma_2 = Plataforma((248,466),(150,30), "Plataformas/piso/0.png")
        plataforma_3 = Plataforma((490,360),(150,30), "Plataformas/piso/0.png")
        plataforma_4 = Plataforma((700,401),(150,30), "Plataformas/piso/0.png")


        lista_plataformas = [piso, plataforma_1, plataforma_2, plataforma_3, plataforma_4, piso_2, piso_3, piso_4, piso_5]

        super().__init__(pantalla, mi_personaje, lista_plataformas, fondo)
