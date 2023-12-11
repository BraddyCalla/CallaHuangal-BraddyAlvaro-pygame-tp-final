import pygame
from Configuraciones import obtener_rectangulos
import time

class PlataformaDesaparece:
    def __init__(self, posicion, tamaño, imagen=None):
        self.imagen_presente = False
        self.tiempo_desaparicion = 3  # segundos
        self.tiempo_aparicion = 3  # segundos
        self.tiempo_ultimo_cambio = time.time()

        if imagen:
            self.imagen_presente = True
            self.imagen = pygame.image.load(imagen)
            self.imagen = pygame.transform.scale(self.imagen, tamaño)
        
        self.rect = pygame.Rect(posicion, tamaño)
        self.lados_plataforma = obtener_rectangulos(self.rect)

    def desaparecer(self):
        self.imagen_presente = False
        self.tiempo_ultimo_cambio = time.time()

    def reaparecer(self):
        self.imagen_presente = True
        self.tiempo_ultimo_cambio = time.time()

    def update(self):
        tiempo_actual = time.time()
        if self.imagen_presente and tiempo_actual - self.tiempo_ultimo_cambio >= self.tiempo_desaparicion:
            self.desaparecer()
        elif not self.imagen_presente and tiempo_actual - self.tiempo_ultimo_cambio >= self.tiempo_aparicion:
            self.reaparecer()

    def draw(self, pantalla):
        if self.imagen_presente:
            pantalla.blit(self.imagen, self.rect)