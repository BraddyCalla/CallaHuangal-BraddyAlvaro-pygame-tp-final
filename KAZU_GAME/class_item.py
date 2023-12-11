import pygame
from Configuraciones import obtener_rectangulos

# , margen_x, margen_y
class Item:
    def __init__(self, posicion_inicial, tamaño, animaciones):
        # confeccion
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        # animaciones
        self.contador_pasos = 0
        self.animaciones = animaciones
        # rectangulos
        self.reescalar_animaciones()
        self.rectangulo = self.animaciones["quieta"][0].get_rect()
        #movimiento plataforma izquierda derecha
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(self.rectangulo)  

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            lista_imagenes = self.animaciones[clave]
            for i in range(len(lista_imagenes)):
                imagen = lista_imagenes[i]
                lista_imagenes[i] = pygame.transform.scale(imagen, (self.ancho, self.alto))

    def animar(self, pantalla, que_animacion: str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def update(self, pantalla, piso):
        self.animar(pantalla, "quieta")