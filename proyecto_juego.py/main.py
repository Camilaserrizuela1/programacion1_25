import pygame as pg
import pygame.mixer as mixer
from validaciones import *
mixer.init()
pg.init()

alto_ventana = 600
ancho_ventana = 800
pantalla = pg.display.set_mode((ancho_ventana, alto_ventana))


coordenadas = inicializar_matriz(10, 10, 0)

x = 300
y = 50
ancho = 10
alto = 50


#dict_batalla = {}
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