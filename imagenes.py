import pygame
from funciones import *

reset = cargar_imagen("img/reset.webp", (80, 80))
volver = cargar_imagen("img/volver.png", (80, 80))
reset_white = cargar_imagen("img/reset_white.png", (80, 80))
volver_white = cargar_imagen("img/volver_white.png", (80, 80))
error = cargar_imagen("img/error.png", (70, 70))

reset_rect = reset.get_rect()
reset_rect.topleft = (1100, 100) 

volver_rect = volver.get_rect()
volver_rect.topleft = (1100, 550)

volver_white_rect = volver_white.get_rect()
volver_rect.topleft = (1100, 550)

DICCIONARIO_IMAGENES = [
    {
        "nombre": "reset",
        "surface": reset,
        "surface_rect": reset_rect,
        "url": "img/reset.webp",
        "posicion_x": 1100,
        "posicion_y": 100,
    },
    {
        "nombre": "reset_white",
        "surface": reset_white,
        "surface_rect": reset_rect,
        "url": "img/reset.webp",
        "posicion_x": 1100,
        "posicion_y": 100,
    },
    {
        "nombre": "volver",
        "surface": volver,
        "surface_rect": volver_rect,
        "url": "img/volver.png",
        "posicion_x": 1100,
        "posicion_y": 550,
    },
    {
        "nombre": "volver_white",
        "surface": volver_white,
        "surface_rect": volver_rect,
        "url": "img/volver_white.png",
        "posicion_x": 1100,
        "posicion_y": 550,
    },
    {
        "nombre": "error",
        "surface": error,
        "surface_rect": None,
        "url": "img/error.png",
        "posicion_x": 500,
        "posicion_y": 20,
    }, 
]