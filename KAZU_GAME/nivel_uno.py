import pygame
from Nivel import *
from modo import *
from class_plataforma import *
from class_plataforma_desaparece import *
from class_personaje import *
from class_enemy import *
from class_item import *
from Configuraciones import *

class NivelUno(Nivel):
    def __init__(self,  pantalla: pygame.Surface):
        W = pantalla.get_width()
        H = pantalla.get_height()

        #FONDO
        fondo = pygame.image.load("Ecenarios/Nivel_1.jpg")
        fondo = pygame.transform.scale(fondo, (W,H))
        
        #PERSONAJE
        posicion = (W/2 - 650, 670)
        tamaño = (40,80)

        diccionario_animaciones = {}
        diccionario_animaciones["quieto"] = personaje_quieto
        diccionario_animaciones["salta"] = personaje_salta
        diccionario_animaciones["camina_derecha"] = personaje_camina_derecha
        diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda

        diccionario_animaciones_ghost = {}
        diccionario_animaciones_ghost ["camina"] = fantasma_camina
        
        diccionario_animaciones_items = {}
        diccionario_animaciones_items ["quieta"] = item_manzana_gold

        # , 40, 80
        mi_personaje = Personaje(posicion, 10, tamaño, diccionario_animaciones)
        fantasma = Enemy((303,288), 10, (80,80), diccionario_animaciones_ghost)

        items = []
        item1 = Item((416,308), (30,30),diccionario_animaciones_items)
        item2 = Item((651,592), (30,30),diccionario_animaciones_items)
        items.append(item1)
        items.append(item2)

        piso = Plataforma((0, mi_personaje.lados["main"].bottom), (550,20))
        piso_2 = Plataforma((809,750),(470,89))
        piso_3 = Plataforma((875,700),(405,60))
        piso_4 = Plataforma((946,619),(333,81))
        piso_5 = Plataforma((1033,526),(244,93))
        piso_6 = Plataforma((1122,444),(89,82))
        piso_7 = Plataforma((1212,481),(67,45))
        piso_8 = Plataforma((717,285),(89,172))
        piso_9 = Plataforma((177,373),(538,84))
        piso_10 = Plataforma((0,287),(175,172))

        #pisos que se caen
        plataforma_1 = Plataforma((542,750),(89,89), "Plataformas/piso/0.png")
        plataforma_2 = Plataforma((631,750),(89,89), "Plataformas/piso/0.png")
        plataforma_3 = Plataforma((720,750),(89,89), "Plataformas/piso/0.png")
        plataforma_4 = Plataforma((860,374),(200,20), "Plataformas/piso/0.png")


        lista_plataformas = [piso, plataforma_1, plataforma_2, plataforma_3, plataforma_4, piso_2, piso_3, piso_4, piso_5, piso_6, piso_7, piso_8, piso_9, piso_10]

        super().__init__(pantalla, mi_personaje, fantasma, items, lista_plataformas, fondo)