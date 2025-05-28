from inputs import *

#Camila Serizuela, 39673090
#comisión 312

matriz_notas_cargadas = [[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [2, 4, 6, 8, 10],
                [3, 6, 9, 4, 8],
                [3, 5, 7, 9, 2],
                [10, 9, 8, 7, 6],
                [5, 4, 3, 2, 1],
                [7, 4, 9, 2, 6],
                [6, 4, 3, 7, 8],
                [7, 7, 7, 7, 7],
                [6, 6, 6, 6, 6],
                [8, 4, 8, 4, 8],
                [5, 7, 9, 7, 3],
                [10, 8, 6, 4, 2],
                [5, 10, 10, 9, 4],
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [2, 4, 6, 8, 10],
                [3, 6, 9, 4, 8],
                [3, 5, 7, 9, 2],
                [10, 9, 8, 7, 6],
                [5, 4, 3, 2, 1],
                [7, 4, 9, 2, 6],
                [6, 4, 3, 7, 8],
                [7, 7, 7, 7, 7],
                [6, 6, 6, 6, 6],
                [8, 4, 8, 4, 8],
                [5, 7, 9, 7, 3],
                [10, 8, 6, 4, 2],
                [5, 10, 10, 9, 4]]

nombres_estudiantes = ["aa", "ab", "ac", "ad","ae", "bb","bb", "cc", "dd","ee", "ff", "gg", "hh", "ii", "jj", "kk", 
                       "ll", "mm", "nn", "oo", "pp", "qq", "rr", "ss", "tt", "uu", "vv", "xx", "yy", "zz" ]
generos_estudiantes = ["F", "M", "X"] * 10
Legajos_estudiantes = [10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010, 10011, 10012, 10013, 
                       10014, 10015, 10016, 10017, 10018, 10019, 10020, 10021, 10022, 10023, 10024, 10025, 10026, 10027, 10028, 10029, 10030]

##################################################################################################################
lista_nombres = []
lista_legajos = []
lista_generos = []
matriz_notas_materia = []
####################################################################################################################

while True:    
    imprime_opciones()
    opcion = input("\n\t> Elija una opción (1-2-3-4-5-6-7-8): ")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "6" and opcion != "7" and opcion != "8":
        opcion = input("ERROR. Elija una opción (1- 2-3-4-5-6-7-8): ")
    match opcion:
        case "1":
            carga_manual(lista_nombres, lista_generos, lista_legajos, matriz_notas_materia)
        case "2":
            opcion_dos(Legajos_estudiantes, generos_estudiantes, nombres_estudiantes, matriz_notas_cargadas)
        case "3":
            opcion_tres(matriz_notas_cargadas)
            print("\t>PROMEDIOS CALCULADOS<")
        case "4":
            opcion_cuatro(matriz_notas_cargadas, nombres_estudiantes, Legajos_estudiantes)
        case "5":
            opcion_cinco(matriz_notas_cargadas)
        case "6":    
            opcion_seis(matriz_notas_cargadas, Legajos_estudiantes, nombres_estudiantes, generos_estudiantes)           
        case "7":
            opcion_siete(matriz_notas_cargadas)
        case "8":
            print("Eligió salir del programa\n ¡Hasta la próxima!")
            break
