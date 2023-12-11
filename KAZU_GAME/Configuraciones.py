import pygame

def girar_imagenes(lista, flip_x, flip_y):
    lista_girada = []
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada

def rescalar_imagenes(lista_imagenes, W, H):
    for lista in lista_imagenes:
        for i in range(len(lista)):
            lista[i] = pygame.transform.scale(lista[i], (W,H))

def obtener_rectangulos(principal)->dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario ["bottom"] = pygame.Rect(principal.left, principal.bottom-10, principal.width, 10)
    diccionario ["right"] = pygame.Rect(principal.right, principal.top-2, 2, principal.height)
    diccionario ["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario ["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)

    return diccionario

#------PERSONAJE------------
personaje_quieto = [pygame.image.load("Kazuma/Quieto/0.png"),
                    pygame.image.load("Kazuma/Quieto/1.png")
                    ]

personaje_camina_derecha = [pygame.image.load("Kazuma/Camina/10.png"),
                    pygame.image.load("Kazuma/Camina/11.png"),
                    pygame.image.load("Kazuma/Camina/12.png"),
                    pygame.image.load("Kazuma/Camina/14.png")
                    ]

personaje_camina_izquierda = girar_imagenes(personaje_camina_derecha, True, False)

personaje_salta = [pygame.image.load("Kazuma/Salta/20.png"),
                   pygame.image.load("Kazuma/Salta/21.png")
                   ]

personaje_ataque_flecha = [pygame.image.load("Kazuma/Ataque flecha/0.png"),
                           pygame.image.load("Kazuma/Ataque flecha/1.png"),
                           pygame.image.load("Kazuma/Ataque flecha/2.png"),
                           pygame.image.load("Kazuma/Ataque flecha/3.png"),
                           ]

personaje_flecha = pygame.image.load("Kazuma/flecha/4.png")

#----------ITEMS--------------
item_manzana = [pygame.image.load("items/Manzana/0.png"),
                pygame.image.load("items/Manzana/1.png"),
                pygame.image.load("items/Manzana/2.png"),
                pygame.image.load("items/Manzana/3.png"),
                pygame.image.load("items/Manzana/4.png"),
                pygame.image.load("items/Manzana/5.png"),
                pygame.image.load("items/Manzana/6.png"),
                pygame.image.load("items/Manzana/7.png"),
                pygame.image.load("items/Manzana/8.png"),
                pygame.image.load("items/Manzana/9.png"),
                pygame.image.load("items/Manzana/10.png"),
                pygame.image.load("items/Manzana/11.png"),
                pygame.image.load("items/Manzana/12.png"),
                pygame.image.load("items/Manzana/13.png"),
                pygame.image.load("items/Manzana/14.png"),
                pygame.image.load("items/Manzana/15.png"),
                pygame.image.load("items/Manzana/16.png")
                ]

item_manzana_gold = [pygame.image.load("items/Manzana dorada/0.png"),
                     pygame.image.load("items/Manzana dorada/1.png"),
                     pygame.image.load("items/Manzana dorada/2.png"),
                     pygame.image.load("items/Manzana dorada/3.png"),
                     pygame.image.load("items/Manzana dorada/4.png")
                     ]

item_manzana_run = [pygame.image.load("items/Manzana camina/43.png"),
                    pygame.image.load("items/Manzana camina/44.png")
                     ]

#------------ENEMIGOS-------------

#Camaleon
camaleon_ataque = [pygame.image.load("Enemigos/Camaleon/ataque/0.png"),
                   pygame.image.load("Enemigos/Camaleon/ataque/1.png"),
                   pygame.image.load("Enemigos/Camaleon/ataque/2.png"),
                   pygame.image.load("Enemigos/Camaleon/ataque/3.png"),
                   pygame.image.load("Enemigos/Camaleon/ataque/4.png"),
                   pygame.image.load("Enemigos/Camaleon/ataque/5.png"),
                   pygame.image.load("Enemigos/Camaleon/ataque/6.png"),
                   pygame.image.load("Enemigos/Camaleon/ataque/7.png"),
                   pygame.image.load("Enemigos/Camaleon/ataque/8.png"),
                   pygame.image.load("Enemigos/Camaleon/ataque/9.png")
                   ]

camaleon_camina = [pygame.image.load("Enemigos/Camaleon/camina/0.png"),
                   pygame.image.load("Enemigos/Camaleon/camina/1.png"),
                   pygame.image.load("Enemigos/Camaleon/camina/2.png"),
                   pygame.image.load("Enemigos/Camaleon/camina/3.png"),
                   pygame.image.load("Enemigos/Camaleon/camina/4.png"),
                   pygame.image.load("Enemigos/Camaleon/camina/5.png"),
                   pygame.image.load("Enemigos/Camaleon/camina/6.png"),
                   pygame.image.load("Enemigos/Camaleon/camina/7.png"),
                   pygame.image.load("Enemigos/Camaleon/camina/8.png"),
                   pygame.image.load("Enemigos/Camaleon/camina/9.png"),
                   pygame.image.load("Enemigos/Camaleon/camina/10.png"),
                   pygame.image.load("Enemigos/Camaleon/camina/11.png"),
                   pygame.image.load("Enemigos/Camaleon/camina/12.png")

                   ]

camaleon_muerte = [pygame.image.load("Enemigos/Camaleon/muerte/0.png"),
                   pygame.image.load("Enemigos/Camaleon/muerte/1.png"),
                   pygame.image.load("Enemigos/Camaleon/muerte/2.png"),
                   pygame.image.load("Enemigos/Camaleon/muerte/3.png"),
                   pygame.image.load("Enemigos/Camaleon/muerte/4.png")
                   ]

#Fantasma
fantasma_camina = [pygame.image.load("Enemigos/Fantasma/camina/0.png"),
                   pygame.image.load("Enemigos/Fantasma/camina/1.png"),
                   pygame.image.load("Enemigos/Fantasma/camina/2.png"),
                   pygame.image.load("Enemigos/Fantasma/camina/3.png"),
                   pygame.image.load("Enemigos/Fantasma/camina/4.png"),
                   pygame.image.load("Enemigos/Fantasma/camina/5.png"),
                   pygame.image.load("Enemigos/Fantasma/camina/6.png"),
                   pygame.image.load("Enemigos/Fantasma/camina/7.png"),
                   pygame.image.load("Enemigos/Fantasma/camina/8.png"),
                   pygame.image.load("Enemigos/Fantasma/camina/9.png")
                   ]

fantasma_muerte = [pygame.image.load("Enemigos/Fantasma/Desaparece/0.png"),
                   pygame.image.load("Enemigos/Fantasma/Desaparece/1.png"),
                   pygame.image.load("Enemigos/Fantasma/Desaparece/2.png"),
                   pygame.image.load("Enemigos/Fantasma/Desaparece/3.png"),
                   pygame.image.load("Enemigos/Fantasma/Desaparece/4.png")
                   ]

#Megumin
megumin_quieta = [pygame.image.load("Enemigos/Megumin/quieta/30.png"),
                  pygame.image.load("Enemigos/Megumin/quieta/49.png")
                   ]

megumin_ataque = [pygame.image.load("Enemigos/Megumin/ataque/26.png"),
                  pygame.image.load("Enemigos/Megumin/ataque/28.png")
                   ]

megumin_explosiones = [pygame.image.load("Enemigos/Megumin/explosiones/0.png"),
                       pygame.image.load("Enemigos/Megumin/explosiones/1.png"),
                       pygame.image.load("Enemigos/Megumin/explosiones/2.png"),
                       pygame.image.load("Enemigos/Megumin/explosiones/3.png"),
                       pygame.image.load("Enemigos/Megumin/explosiones/4.png"),
                       pygame.image.load("Enemigos/Megumin/explosiones/5.png")

                       ]

megumin_muerte = [pygame.image.load("Enemigos/Megumin/muerte/30.png"),
                  pygame.image.load("Enemigos/Megumin/muerte/31.png"),
                  pygame.image.load("Enemigos/Megumin/muerte/32.png"),
                  pygame.image.load("Enemigos/Megumin/muerte/33.png"),
                  pygame.image.load("Enemigos/Megumin/muerte/34.png")
                   ]

#------------TRAMPAS---------------

#Roca
roca_caida = [pygame.image.load("Trampas/Roca/caida/2.png"),
              pygame.image.load("Trampas/Roca/caida/3.png"),
              pygame.image.load("Trampas/Roca/caida/4.png")
              ]

roca_deteccion = [pygame.image.load("Trampas/Roca/Deteccion/0.png"),
                  pygame.image.load("Trampas/Roca/Deteccion/1.png"),
                  pygame.image.load("Trampas/Roca/Deteccion/2.png"),
                  pygame.image.load("Trampas/Roca/Deteccion/3.png"),
                  ]

roca_normal = pygame.image.load("Trampas/Roca/normal/0.png")

#Sierra
sierra_moviendose = [pygame.image.load("Trampas/sierra/moviendose/0.png"),
                     pygame.image.load("Trampas/sierra/moviendose/1.png"),
                     pygame.image.load("Trampas/sierra/moviendose/2.png"),
                     pygame.image.load("Trampas/sierra/moviendose/3.png"),
                     pygame.image.load("Trampas/sierra/moviendose/4.png"),
                     pygame.image.load("Trampas/sierra/moviendose/5.png"),
                     pygame.image.load("Trampas/sierra/moviendose/6.png")
                     ]

sierra_quieta = pygame.image.load("Trampas/sierra/quieto/Off.png")

puntos_sierra = pygame.image.load("Trampas/sierra/puntos referencia/Chain.png")

#------------PLATAFORMAS---------------

plataforma = pygame.image.load("Plataformas/piso/0.png")

plataforma_desaparece = pygame.image.load("Plataformas/piso desaparece/0.png")

#------------VIDAS---------------

vida = pygame.image.load("Vidas\pixel-heart-2779422_960_720.png")
