from validaciones import *

def imprime_opciones() -> None:
    '''
    Función que imprime una serie de opciones
    '''
    print("- Cargar los datos (nombre, legajo, genero) y notas, OPCION: 1") 
    print("- Ver todos los datos (calificaciones, legajo, nombres y genero), OPCION: 2 ")
    print("- Calcular el promedio de cada estudiante, OPCION: 3")
    print("- Ordenar y mostrar los datos de los estudiantes según promedio, OPCION: 4")
    print("- Mostrar la/s materia/s con mayor promedio general, OPCION: 5")
    print("- Buscar por legajo y mostrar todos los datos del estudiante, OPCION: 6")
    print("- Elegir una materia y ver la cantidad de veces que se repiten las notas, OPCIÓN: 7")
    print("- Salir del programa y volver al menú anterior: OPCION: 8")
    

def carga_manual (lista_nombres:list, lista_generos:list, lista_legajos:list, matriz:list):
    '''
    Función que realiza una carga secuencial de cada uno de los parámetros (listas vacias)
    ''' 
    for i in range(30):
        print(f"Carga del estudiante: {i+1}")
    #carga nombre
        ingresar_nombre = input("Ingrese nombre del alumno: ")
        while contiene_letras(ingresar_nombre) == False:            #14
            ingresar_nombre = input("Error. Ingrese nombre del alumno: ")
        lista_nombres += [ingresar_nombre] 
    #carga genero           
        ingresar_genero = input("Ingrese genero (F | M | X): ")
        while validar_genero(ingresar_genero) == False :            #91
            ingresar_genero = input("Error. Ingrese genero (F | M | X): ")
        ingresar_genero = validar_mayuscula(ingresar_genero)        #61
        lista_generos += [ingresar_genero]
    #carga legajos
        ingresar_legajo = input("Ingrese numero de legajo: ")
        while contiene_algo(ingresar_legajo) == False:              #1
            ingresar_legajo = input("ERROR. Ingrese numero de legajo (cinco números): ")
        while contiene_numero(ingresar_legajo) == False:            #40
             ingresar_legajo = input("ERROR. Ingrese numero de legajo (cinco números): ")
        while len(ingresar_legajo) != 5:
            ingresar_legajo = input("ERROR. Ingrese numero de  legajo (cinco números): ")
        while validar_duplicados(lista_legajos, ingresar_legajo) == True:       #119
             ingresar_legajo = input("ERROR. Ingrese numero de legajo (cinco números): ")
        lista_legajos += [int(ingresar_legajo)]  
    #carga de las notas
        if len(matriz) == 0: 
            matriz = inicializar_matriz(30, 5, 0)       #134
    matriz = carga_matriz_secuencialmente(matriz)       #155



def opcion_dos (Legajos_estudiantes:list, generos_estudiantes:list, nombres_estudiantes:list, matriz_notas_cargadas:list)->  None:
    '''
    Función que muestra todos los datos (la matriz completa y las listas de legajo, géneros y nombres)
'''
    print("LEGAJOS\tGENEROS\tNOMBRES\tNOTAS")
    print("\tMaterias:\t1|2|3|4|5")
    mostrar_datos(Legajos_estudiantes, generos_estudiantes, nombres_estudiantes, matriz_notas_cargadas) #214
    

def opcion_tres (matriz:list) -> list:          #252
    '''
    Función que calcula el promedio y los guarda en una nueva lista 
    '''
    lista= calcular_promedio(matriz)
    return lista


def opcion_cuatro(matriz:list, nombres_estudiantes:list, Legajos_estudiantes:list):         #338
    '''Función que ordena y muestra los datos de los estudiantes por promedio de manera DESC'''
    llamar_promedio = opcion_tres(matriz)
    ordenar(nombres_estudiantes, Legajos_estudiantes, llamar_promedio, 2, 2)
    print("Legajos Nombres PROMEDIOS (ORDEN DESCENDENTE)")
    mostrar_datos(Legajos_estudiantes, nombres_estudiantes, llamar_promedio)


def opcion_cinco(matriz):           #278 y 309
    '''
    Función que muestra la/s materia/s con mayor promedio general
    '''
    llamado_cinco = promedio_mayor(matriz)
    print("\nMATERIA/S CON MAYOR PROMEDIO:")
    print(f"{llamado_cinco}\n")


def opcion_seis(matriz:list, legajos:list, nombres:list, generos:list):
    '''
     Función que Busca y muestra todos los datos de un estudiante por legajo. 
     '''
    buscar_legajo=input("> Ingrese el legajo del alumno(10001-10030): ")
    while  contiene_algo == False:
            buscar_legajo=input("ERROR. Ingrese el legajo del alumno(10001-10030): ")
    while contiene_numero(buscar_legajo)== False:
        buscar_legajo=input("ERROR. Ingrese el legajo del alumno(10001-10030): ")
    legajo_valido= int(buscar_legajo)
    while legajo_valido < 10001 or legajo_valido > 10030:
        buscar_legajo=input("ERROR. Ingrese el legajo del alumno(10001-10030): ")
    llamado_buscar = buscador(legajo_valido, legajos)       #386
    llamar_promedio = opcion_tres(matriz)

    print("LEGAJO\tGENERO\tNOMBRE\tPROMEDIO NOTAS\n")
    mostrar_datos([legajos[llamado_buscar]], 
                    [generos[llamado_buscar]], 
                    [nombres[llamado_buscar]], 
                    [matriz[llamado_buscar]],
                    [llamar_promedio[llamado_buscar]])
    

def opcion_siete(matriz):
    '''
    funcion que recibe la matriz de calificaciones y el número de materia como parámetros, 
    y retorne una lista de elementos'''
    
    materia = input("Que materia quiere buscar? (1-5): ")
    while contiene_algo(materia) == False:
        materia = input("ERROR. Que materia quiere buscar? (1-5): ")
    while contiene_numero(materia) == False:
        materia = input("ERROR. Que materia quiere buscar? (1-5): ")
    materia = int(materia)
    while materia < 1 or materia > 5:
        materia = input("ERROR. Que materia quiere buscar? (1-5): ")
    notas = ["Nota: 1", "Nota: 2", "Nota: 3", "Nota: 4", "Nota: 5", "Nota: 6", "Nota: 7", "Nota: 8", "Nota: 9", "Nota: 10"]
    cantidad = ["cantidad:"]*10
    veces_materias = contador_notas(matriz, materia)        #402
    
    mostrar_datos(notas, cantidad, veces_materias)
