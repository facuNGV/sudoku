import pygame
from constantes import *
from imagenes import cargar_imagen, DICCIONARIO_IMAGENES
from logica_sudoku import inicializar_tablero_sudoku





# fuente = pygame.font.Font(None, 40)

# facil = fuente.render("Facil", True, "white")
# intermedio = fuente.render("Intermedio", True, "white")
# dificil = fuente.render("Dificil", True, "white")

# if dificultad == "facil":
#     facil = fuente.render("Facil", True, "green")
# elif dificultad == "intermedio":
#     intermedio = fuente.render("Intermedio", True, "green")
# elif dificultad == "dificil":
#     dificil = fuente.render("Dificil", True, "green")

# facil_rect = facil.get_rect()
# intermedio_rect = intermedio.get_rect()
# dificil_rect = dificil.get_rect()
# facil_rect.topleft = (1000, 100)
# intermedio_rect.topleft = (1000, 140)
# dificil_rect.topleft = (1000, 180)


            
def pantalla_menu(eventos, estado_juego):
    estado_juego['pantalla'].blit(cargar_imagen("img/fondo.jpg"), (0, 0))
    fuente = pygame.font.Font(None, 40)
    dibujar_botones_menu(estado_juego['pantalla'], fuente)
    
    # facil = fuente.render("Facil", True, "white")
    # intermedio = fuente.render("Intermedio", True, "white")
    # dificil = fuente.render("Dificil", True, "white")
    
    # if dificultad == "facil":
    #     facil = fuente.render("Facil", True, "green")
    # elif dificultad == "intermedio":
    #     intermedio = fuente.render("Intermedio", True, "green")
    # elif dificultad == "dificil":
    #     dificil = fuente.render("Dificil", True, "green")
    
    # facil_rect = facil.get_rect()
    # intermedio_rect = intermedio.get_rect()
    # dificil_rect = dificil.get_rect()
    # facil_rect.topleft = (1000, 100)
    # intermedio_rect.topleft = (1000, 140)
    # dificil_rect.topleft = (1000, 180)
                    
    # pantalla.blit(facil, facil_rect)
    # pantalla.blit(intermedio, intermedio_rect)
    # pantalla.blit(dificil, dificil_rect)
    
    # for evento in eventos:
    #     if evento.type == pygame.MOUSEBUTTONDOWN:
    #         if facil_rect.collidepoint(evento.pos):
    #             dificultad = "facil"
    #         elif intermedio_rect.collidepoint(evento.pos):
    #             dificultad = "intermedio"
    #         elif dificil_rect.collidepoint(evento.pos):
    #             dificultad = "dificil"
    
    pygame.display.flip()

def dibujar_botones_menu(pantalla, fuente):
        for opcion in OPCIONES_MENU:
            x, y = opcion["posicion"]
            texto = fuente.render(opcion["texto"], True, BLANCO)
            texto_rect = texto.get_rect(center=(x + ANCHO_BOTON // 2, y + ALTO_BOTON // 2))
            boton_rect = pygame.Rect(x, y, ANCHO_BOTON, ALTO_BOTON)
            if texto_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(pantalla, COLOR_BOTON_SELECCION, boton_rect, border_radius=RADIO_BOTON)
            else:
                pygame.draw.rect(pantalla, COLOR_BOTON, boton_rect, border_radius=RADIO_BOTON)
            pantalla.blit(texto, texto_rect.topleft)

def pantalla_juego(estado_juego:dict):
    estado_juego['pantalla'].blit(cargar_imagen("img\ingame-fondo.jpg"), (0, 0))
    errores = str(estado_juego['errores'])
    
    
    
    dibujar_temporizador(estado_juego)
    dibujar_tablero(estado_juego)
    
    fuente = pygame.font.SysFont(None, 50)
    errores = fuente.render(errores, True, "black")
    
    for elemento in DICCIONARIO_IMAGENES:
        estado_juego['pantalla'].blit(elemento["surface"], (elemento["posicion_x"], elemento["posicion_y"]))
    
    estado_juego['pantalla'].blit(errores, (580, 42))
    
    pygame.display.flip()

def pantalla_puntajes(estado_juego:dict):
    estado_juego['pantalla'].fill("lightblue")
    fuente = pygame.font.SysFont(None, 74)
    texto = fuente.render("Pantalla de Puntajes", True, "black")
    estado_juego['pantalla'].blit(texto, (400, 300))
    pygame.display.flip()

def dibujar_tablero(estado_juego:dict):
    fuente = pygame.font.SysFont(None, 32)
    cell_size = 60
    
    for i in range(9):
        for j in range(9):
            # Obtener el valor de la celda actual
            value = estado_juego['sudoku'][i][j]
            numero = fuente.render(str(estado_juego['sudoku'][i][j]), True, "black")
            
            if value != " ":
                color = "#edbfb7"
            else:
                color = "#db8779"
            

            # Dibujar el rectángulo (celda)          j * cell_size + 200                   Y                 ANCHO     ALTO
            pygame.draw.rect(estado_juego['pantalla'], color, (j * cell_size + 400, i * cell_size + 100, cell_size, cell_size))
            
            # Dibujar borde para cada celda
            pygame.draw.rect(estado_juego['pantalla'], "#b3341e", (j * cell_size + 400, i * cell_size + 100, cell_size, cell_size), 1)
            
            
            if value != " ":
                estado_juego['pantalla'].blit(numero, (j * cell_size + 425, i * cell_size + 120))
                
    for elemento in LINEAS_TABLERO:
        x1, y1, x2, y2 = elemento
        pygame.draw.line(estado_juego['pantalla'], "red", (x1, y1), (x2, y2), 3)
    pygame.draw.rect(estado_juego['pantalla'], "red", (400, 100, 545, 545), 5)
    


def dibujar_temporizador(estado_juego:dict):
    fuente = pygame.font.SysFont(None, 50)
    texto = fuente.render(estado_juego['tiempo'], True, "white")
    estado_juego['pantalla'].blit(texto, (100, 100))