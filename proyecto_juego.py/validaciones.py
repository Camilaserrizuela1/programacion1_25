def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial) -> list:  
    matriz = []
    #i (q se convierte en valor_inicial) se va a repetir según el rango de cantidad de columnas indicadas
    #y estas se repiten sesegún la cantidad de filas 
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def inicializo_tablero(dificultad:str) -> list[list]:
    matriz_juego = list
    if dificultad == "Fácil":
        matriz_juego = inicializar_matriz(10, 10, 0)
    if dificultad == "Intermedio":
        matriz_juego = inicializar_matriz(20, 20, 0)
    if dificultad == "Dificil":
        matriz_juego =inicializar_matriz(30, 30, 0)
    return matriz_juego