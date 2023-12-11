import pygame
from Configuraciones import obtener_rectangulos

# , margen_x, margen_y
class Personaje:
    def __init__(self, posicion_inicial, velocidad, tamaño, animaciones):
        # confeccion
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        # gravedad
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        # animaciones
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        # rectangulos
        self.reescalar_animaciones()
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        #movimiento plataforma izquierda derecha
        self.esta_en_el_piso = True
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(self.rectangulo)
        # movimiento        
        self.velocidad = velocidad
        self.desplazamiento_y = 0

        # self._cantidad_pasos = 0
        # self._cantidad_saltos = 0
        # self._contador_saltos = 0
        # self._esta_en_el_piso = True
        # self._esta_chocando_derecha = False
        # self._esta_chocando_izquierda = False
        # self._margen_x = margen_x
        # self._margen_y = margen_y
        # self._posicion = []
        # for i in posicion_inicial:
        #     self._posicion.append(i)
        

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

    def aplicar_gravedad(self, pantalla, plataformas):
        if self.esta_saltando:
            self.animar(pantalla, "salta")
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        for piso in plataformas:
            if self.lados["bottom"].colliderect(piso.lados_plataforma["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = piso.rect.top + 5
                break
            else:
                self.esta_saltando = True

    # def verificar_colision_piso(self, pisos):
    #     estado_anterior =self._esta_en_el_piso
    #     self._esta_en_el_piso = False
    #     self._esta_chocando_derecha = False
    #     self._esta_chocando_izquierda = False
    #     for piso in pisos:
    #         if self.lados["bottom"].colliderect(piso.lados_plataforma["top"]):
    #             if not estado_anterior:
    #                 self._posicion[1] = piso.lados_plataforma["top"].top - self.rectangulo.height - self._margen_y
    #             self._contador_salto = 0
    #             self._esta_en_el_piso = True
    #         elif self.lados["right"].colliderect(piso.lados_plataforma["left"]):
    #             self._esta_chocando_derecha = True
    #             self.que_hace = "quieto"
    #         elif self.lados["left"].colliderect(piso.lados_plataforma["right"]):
    #             self._esta_chocando_izquierda = True
    #             self.que_hace = "quieto"
    #         elif self.lados["top"].colliderect(piso.lados_plataforma["bottom"]) or self.rectangulo.top< 0+80:
    #             self._cantidad_pasos = -6

    # def update(self, pantalla, piso):
    #     self.verificar_colision_piso(piso)
    #     if self.que_hace == "derecha" and (self._esta_chocando_derecha == False):
    #         if not self.esta_saltando:
    #             self.animar(pantalla, "camina_derecha")
    #         self.mover(self.velocidad)
    #     elif self.que_hace == "izquierda" and (self._esta_chocando_izquierda == False):
    #         if not self.esta_saltando:
    #             self.animar(pantalla, "camina_izquierda")
    #         self.mover(self.velocidad * -1)
    #     elif self.que_hace == "salta":
    #         if not self.esta_saltando:
    #             self.esta_saltando = True
    #             self.desplazamiento_y = self.potencia_salto
    #     elif self.que_hace == "quieto":
    #         if not self.esta_saltando:
    #             self.animar(pantalla, "quieto")

    def update(self, pantalla, piso):
        if self.que_hace == "derecha":
            if not self.esta_saltando:
                self.animar(pantalla, "camina_derecha")
            self.mover(self.velocidad)
        elif self.que_hace == "izquierda":
            if not self.esta_saltando:
                self.animar(pantalla, "camina_izquierda")
            self.mover(self.velocidad * -1)
        elif self.que_hace == "salta":
            if not self.esta_saltando:
                self.esta_saltando = True
                self.desplazamiento_y = self.potencia_salto
        elif self.que_hace == "quieto":
            if not self.esta_saltando:
                self.animar(pantalla, "quieto")

        self.aplicar_gravedad(pantalla, piso)