import random

def inicializar_matriz(cant_filas:int, cant_columnas:int, valor_inicial:any)->list[list[any]]:
    """
    Esta función se encarga de inicializar una matriz con un valor inicial.
    Recibe: cant_filas(int): Cantidad de filas que va a tener la matriz
            cant_columnas(int): Cantidad de columnas que va a tener la matriz
            valor_inicial(any): Dato con el que se va a inicializar la matriz
    Retorna: matriz(list[list[any]]): Matriz con las dimensiones creada con los datos cargados como valor inicial. 
    """
    matriz = []
    for _ in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz

def mostrar_sudoku(matriz:list[list])->None:
    """
    Esta funcion se encarga de imprimir en consola la cuadricula del sudoku.
    Recibe: matriz(list[list])
    No retorna nada.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == 3 or j == 6:
                print(" ", end=" ")  
            print(matriz[i][j], end=" ")
        if i == 2 or i == 5:
            print(" ")
        print("")

def generar_sudoku(matriz):
    for i in range(9):
        for j in range(9):
            if matriz[i][j] == 0:  # Solo intentamos llenar celdas vacías
                numeros = list(range(1, 10))  # Convertimos el rango a una lista
                random.shuffle(numeros)  # Barajamos los números del 1 al 9
                for numero in numeros:
                    if validar_numero_sudoku(matriz, numero, i, j):
                        matriz[i][j] = numero
                        if generar_sudoku(matriz):
                            return True
                        matriz[i][j] = 0  # Retrocedemos si no encontramos una solución
                return False  # Si no hay números válidos, volvemos
    return True  # Si todas las celdas se llenaron, el Sudoku está completo

def validar_numero_sudoku(matriz, numero, fila, columna):
    # Validar la fila
    for i in range(9):
        if matriz[fila][i] == numero:
            return False
    
    # Validar la columna
    for j in range(9):
        if matriz[j][columna] == numero:
            return False
    
    # Validar la subcuadrícula de 3x3
    subcuadrícula_fila_inicio = (fila // 3) * 3
    subcuadrícula_columna_inicio = (columna // 3) * 3
    
    for i in range(3):
        for j in range(3):
            if matriz[subcuadrícula_fila_inicio + i][subcuadrícula_columna_inicio + j] == numero:
                return False
    
    return True

# ----------------------

def ocultar_celdas(matriz:list[list[int]], porcentaje:float = 0.2):
    cantidad_celdas_a_ocultar = int(81 * porcentaje)
    copia_tablero = matriz[:]
    for _ in range(cantidad_celdas_a_ocultar):
        fila = random.randint(0,8)
        columna = random.randint(0,8)
        while copia_tablero[fila][columna] == " ":
            fila = random.randint(0,8)
            columna = random.randint(0,8)
        copia_tablero[fila][columna] = " "
    return copia_tablero


def inicializar_tablero_sudoku():
    matriz = inicializar_matriz(9, 9, 0)
    generar_sudoku(matriz)
    return ocultar_celdas(matriz)