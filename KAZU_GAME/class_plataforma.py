import pygame
from Configuraciones import obtener_rectangulos

class Plataforma:
    def __init__(self, posicion, tamaño, imagen=None):
        self.imagen_presente = False
        if imagen:
            self.imagen_presente = True
            self.imagen = pygame.image.load(imagen)
            self.imagen = pygame.transform.scale(self.imagen, tamaño)
        
        self.rect = pygame.Rect(posicion, tamaño)
        self.lados_plataforma = obtener_rectangulos(self.rect)

    def draw(self, pantalla):
        if self.imagen_presente:
            pantalla.blit(self.imagen, self.rect)


