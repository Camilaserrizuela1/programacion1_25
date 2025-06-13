import pygame as pg
import pygame.mixer as mixer
from validaciones import *
import complementos
mixer.init()
pg.init()

alto_ventana = 600
ancho_ventana = 800
pantalla = pg.display.set_mode((ancho_ventana, alto_ventana))

#######################################################
titulo = pg.display.set_caption("BATALLA NAVAL")
imagen_icono = pg.image.load("C:/Users/Pc Gamer Diego/Desktop/Cami/312_ejercicios/complementos_juego/ancla1.png")
icono = pg.display.set_icon(imagen_icono)
musica = mixer.music.load("C:/Users/Pc Gamer Diego/Desktop/Cami/312_ejercicios/complementos_juego/war-battle-military.mp3")
volumen = mixer.music.set_volume(0.1)
play_music = mixer.music.play()
#mixer.music.stop() para deternerla

sonido_disparo = mixer.Sound("C:/Users/Pc Gamer Diego/Desktop/Cami/312_ejercicios/complementos_juego/cannon.mp3")
sonido_disparo.set_volume(0.4)
sonido_agua =  mixer.Sound("C:/Users/Pc Gamer Diego/Desktop/Cami/312_ejercicios/complementos_juego/gota.mp3")
sonido_agua.set_volume(0.4)
#sonido.play() para iniciarlo donde quiera 

x = 50
y = 50
ancho_sub = 10
ancho_dest = 20
ancho_crucero = 30
ancho_acorazado = 40
alto = 10

dict_submarino = {}     #(x4) ocupa 1
dict_submarino["imagen"] = pg.image.load("C:/Users/Pc Gamer Diego/Desktop/Cami/312_ejercicios/complementos_juego/submarino.png")
dict_submarino["imagen"] = pg.transform.scale(dict_submarino["imagen"], (ancho_sub, alto))
#dict_submarino["rectangulo_pos"] = pg.Rect(x, y, ancho, alto)
#dict_submarino["puntos"] = 0

dict_destructores = {}  #(x3) ocupa 2 casilleros
dict_destructores["imagen"] = pg.image.load("C:/Users/Pc Gamer Diego/Desktop/Cami/312_ejercicios/complementos_juego/destructor.png")
dict_destructores["imagen"] = pg.transform.scale(dict_destructores["imagen"], (ancho_dest, alto))

dict_crucero = {}  #(x2) ocupa 3 casilleros
dict_crucero["imagen"] = pg.image.load("C:/Users/Pc Gamer Diego/Desktop/Cami/312_ejercicios/complementos_juego/crucero_de_batalla.png")
dict_crucero["imagen"] = pg.transform.scale(dict_crucero["imagen"], (ancho_crucero, alto))

dict_acorazado = {}  #(x1) ocupa 4 casilleros
dict_acorazado["imagen"] = pg.image.load("C:/Users/Pc Gamer Diego/Desktop/Cami/312_ejercicios/complementos_juego/acorazado.png")
dict_acorazado["imagen"] = pg.transform.scale(dict_acorazado["imagen"], (ancho_acorazado, alto))

dict_agua = {}  #(x3) ocupa 2 casilleros
dict_agua["imagen"] = pg.image.load("C:/Users/Pc Gamer Diego/Desktop/Cami/312_ejercicios/complementos_juego/ola.png")
dict_agua["imagen"] = pg.transform.scale(dict_agua["imagen"], (ancho_sub, alto))
######################################################
coordenadas = inicializar_matriz(10, 10, 0)



fondo = pg.image.load("C:/Users/Pc Gamer Diego/Desktop/Cami/312_ejercicios/complementos_juego/fondo_juego.png")
fondo = pg.transform.scale(fondo, (ancho_ventana, alto_ventana))
#dict_batalla['rect'] = pg.Rect(x, y, ancho, alto)
#dict_batalla['punto'] = 0 



while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            quit()

    pantalla.blit(fondo, (0, 0))
    pg.display.flip()


def colocar_naves(tablero, submarinos, destructores, cruceros, acorazados):
#  Cuatro (4) submarinos de un (1) casillero
#  Tres (3) destructores de dos (2) casilleros
#  Dos (2) cruceros de tres (3) casilleros
#  Un (1) acorazado de cuatro (4) casilleros
    pass