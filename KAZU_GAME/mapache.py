import pygame, sys
from Configuraciones import *
from pygame.locals import *
from modo import * 
pygame.init()

W,H = 1280,853
TAMAÑO_PANTALLA = (W,H)
FPS = 18

colorTexto = "White"
fuente = pygame.font.SysFont("Arial", 20)
texto = fuente.render("Tiempo", True, colorTexto)

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)



fondo = pygame.image.load("Ecenarios/Nivel_1.jpg")
fondo = pygame.transform.scale(fondo,TAMAÑO_PANTALLA)

pygame.display.set_caption("Primer juego")

flag = True
while flag:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
    
    PANTALLA.blit(fondo, (0,0))
    lista_teclas = pygame.key.get_pressed()
    PANTALLA.blit(texto,(10,10))
    tiempo = pygame.time.get_ticks() / 1000
    texto = fuente.render("Tiempo: :"+str(tiempo), True, colorTexto)
    if lista_teclas[pygame.K_0]:
        print("0")

    if lista_teclas[pygame.K_LEFT]:
        print("Izquierda")

    if lista_teclas[pygame.K_RIGHT]:
        print("Derecha")
    
    if lista_teclas[pygame.K_ESCAPE]:
        flag = False

    pygame.display.update()

pygame.quit()