import pygame
from Configuraciones import obtener_rectangulos

# , margen_x, margen_y
class Enemy:
    def __init__(self, posicion_inicial, velocidad, tamaño, animaciones):
        # confeccion
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        # animaciones
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        # rectangulos
        self.reescalar_animaciones()
        self.rectangulo = self.animaciones["camina"][0].get_rect()
        #movimiento plataforma izquierda derecha
        self.esta_en_el_piso = True
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(self.rectangulo)
        # movimiento        
        self.velocidad = velocidad
        self.desplazamiento_y = 1000      

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
        tiempo = pygame.time.get_ticks() / 1000
        tiempo = int(tiempo)
        direccion = ""

        if tiempo % 2 == 0:
            direccion = "derecha"
        else:
            direccion = "izquierda"

        if direccion == "izquierda":
            self.mover(self.velocidad * -1)
        elif direccion == "derecha":
            self.mover(self.velocidad)

        self.animar(pantalla, "camina")