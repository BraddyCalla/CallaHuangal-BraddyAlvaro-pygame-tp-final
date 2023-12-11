import pygame
from modo import *


class Nivel:
    def __init__(self, pantalla, personaje_principal, enemy, items, lista_plataformas, imagen_fondo):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.enemy = enemy
        self.items1 = items[0]
        self.items2 = items[1]
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        self.W = imagen_fondo.get_width()
    
    def update(self, lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()

        self.leer_inputs()
        self.actualizar_pantalla()


    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo, (0,0))

        for plataforma in self.plataformas:
            plataforma.draw(self._slave)

        self.jugador.update(self._slave, self.plataformas)
        self.enemy.update(self._slave, self.plataformas)
        self.items1.update(self._slave, self.plataformas)
        self.items2.update(self._slave, self.plataformas)
            

    def leer_inputs(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.jugador.rectangulo.x < self.W - self.jugador.velocidad - self.jugador.rectangulo.width:
            self.jugador.que_hace = "derecha"
        elif keys[pygame.K_LEFT] and self.jugador.rectangulo.x > self.jugador.velocidad:
            self.jugador.que_hace = "izquierda"
        elif keys[pygame.K_UP] or (keys[pygame.K_UP] and keys[pygame.K_LEFT]) or (keys[pygame.K_UP] and keys[pygame.K_RIGHT]):
            self.jugador.que_hace = "salta"
        else:
            self.jugador.que_hace = "quieto"

    def dibujar_rectangulos(self):
        if get_mode() == True:
            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, "Orange", self.jugador.lados[lado],2)
            
            for lado in self.enemy.lados:
                pygame.draw.rect(self._slave, "Red", self.enemy.lados[lado],2)

            for lado in self.items1.lados:
                pygame.draw.rect(self._slave, "Red", self.items1.lados[lado],2)

            for lado in self.items2.lados:
                pygame.draw.rect(self._slave, "Red", self.items2.lados[lado],2)

            for plataforma in self.plataformas:
                for lado in plataforma.lados:
                    pygame.draw.rect(self._slave, "Green", plataforma.lados[lado], 2)


