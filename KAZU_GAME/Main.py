import pygame, sys
from Configuraciones import *
from pygame.locals import *
from modo import * 
from nivel_uno import NivelUno
from nivel_dos import NivelDos
from GUI_form_principal import *

W,H = 1280,853
TAMAÑO_PANTALLA = (W,H)
FPS = 18

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
pygame.display.set_caption("KAZUMA GAME")

icono = pygame.image.load("Interfaz/icon.png")
pygame.display.set_icon(icono)

form_principal = FormPrincipal(PANTALLA, 100, 200,800,350,(203,142,29), (0,105,37), 5, True)

fondo = pygame.image.load("Interfaz/Fondo_interfaz.png")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

while True:
    RELOJ.tick(FPS)
    PANTALLA.blit(fondo, (0,0))
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == QUIT:
            pygame.quit()
            sys.exit(0)
    
    form_principal.update(eventos)
    
    pygame.display.update()