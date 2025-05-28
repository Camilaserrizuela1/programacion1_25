def contiene_algo (cadena)-> bool:
    '''
    Función que chequea que lo que se ingreso no sea un espacio vacío(=""), 
    independientemente de lo que se haya ingresado
    
    Args:
    :param cadena: cadena a chequear

    :return: (bool) devuelve true si contiene algo. Sino, false
    '''
    if len(cadena) > 0:
        return True

def contiene_letras(cadena:str) -> bool:
    '''
    Función que recorre la cadena de caracteres y verica que sean letras
    
    Args:
    :param solo_letras: bandera:bool
    :param contador: cuenta la cantidad de letras (mayusculas o minusculas) que se encontraron

    :return solo_letras: retorna true si contiene letras, sino retornara false
    '''
    solo_letras = True
    contador = 0
    #chequeo q no sea cadena vacia
    if len(cadena) == 0:        
        solo_letras = False
#recorro cadena. La pasa a ascii. Incremento contador de caracteres
    for i in range(len(cadena)):  
        ascii=ord(cadena[i]) 
            #minusculas                        #mayusculas                  #32 = espacio vacio
        if (ascii >= 65 and ascii <=90) or (ascii >= 97 and ascii <= 122) or ascii == 32:  
            contador += 1
            #si las cantidades son distintas es false
    if contador != len(cadena):  
        solo_letras = False     
    return solo_letras

def contiene_numero(cadena:str)-> bool:     #declaro cadena:str xq si es int se rompe en len y en ascii q trabajan con caracteres. chequeo despues q sea un numero
    '''
    Función que recorre la cadena de caracteres recibida y verifica que sea números

    Args:
    :param es_numero: bandera:bool. Si hay numeros va a ser True, sino false
    :param contador_caracteres: cuenta la cantidad de numeros que se encontraron

    :return: retorna es_numero 
    '''
    es_numero = False
    contador_caracteres = 0
    #recorro cadena, la paso a ascii. Si esta en el rango de números, incremento contador y lo comparo
    for i in range(len(cadena)):
        ascii=ord(cadena[i])       
        if (ascii > 47 and ascii < 58):     
            contador_caracteres += 1  
    if contador_caracteres == len(cadena): 
            es_numero = True                
    return es_numero

def validar_mayuscula(cadena: str) -> str:
    '''
    Función que chequea/valida que la cadena ingresada sean letras y esten en mayúsculas. 
    Si esta en minúscula, la pasa a mayúscula
    
    :param cadena: (str): string a validar
    :param nueva_cadena: bandera donde se guaradan las letras validadas en mayúsculas

    :return: devuelve la cadena validada en mayúsculas
    '''
    nueva_cadena ="" 

    if contiene_algo == False:  
        nueva_cadena = ("Cadena vacia")
#recorro el contenido de cadena. guardo para caracter en 'caracter' y lo paso a ascii
    for i in range(len(cadena)):    
        caracter = cadena[i]   
        ascii = ord(caracter)   
    #minusculas
        if ascii >= 97 and ascii <= 122:    
            mayuscula = chr(ascii - 32)     #chr me pasa el codigo ascii a caracter
            nueva_cadena += mayuscula
#mayusculas
        elif ascii >= 65 and ascii <= 90: 
            nueva_cadena += caracter 
        else:
            nueva_cadena= ("No se ingreso cadena de letras")   #x si se ingreso otra cosa como un doble espacio vacio
    return nueva_cadena


def validar_genero(genero:str)-> bool:
    '''
    Función que valida que el dato que se ingreso (mayúscula o minúscula) corresponde a un genero (F | M | X)

    Args:
    :param genero: (str) letra a validar
    :param es_genero: bandera:bool. Si es genero será true, sino, false

    :return: retorna es_genero:bool
    '''
    es_genero = False
    #chequeo que haya solo 1 caracter
    if len(genero) != 1:
        es_genero = False   
    #chequeo q haya letra (minusculas o mayusculas)
    if contiene_letras(genero) == False: 
        es_genero = False
    #la paso a ascii, si es minuscula le resto 32 para pasarla  a mayuscula
    ascii = ord(genero)          
    if ascii >= 97 and ascii <= 122:    
        ascii -= 32      
    #Si es:     #F           #M            #X
    if ascii == 70 or ascii == 77 or ascii == 88:
        es_genero = True  
    return es_genero



def validar_duplicados(lista:list, valor) -> bool:
    '''
    Función que chequea que el valor ingresado sea único en la lista, que no este repetido.
    
    Args:
    :param lista: lista donde se va a buscar el valor
    :valor: valor a buscar en la lista
    
    :return: va aretornar true si ya se encuentra en la lista o  false si es único.  '''
    esta_repetido = False
    if valor in lista:
        esta_repetido = True
    return esta_repetido 


def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial) -> list:  
    '''
    Función que inicializará(armará) una matriz según los parametros que ingrese. Arma la estructura
    
    Args:
    :param cantidad_filas: (int) número de filas que tendrá la matriz.
    :param cantidad_columnas: (int) número de columnas que tendrá cada fila.
    :param valor_inicial: valor con el que se llenaran todas las posiciones de la matriz. Puede ser numeros, letras, atc
    :param matriz: lista de lista donde se armará la matriz

    :return: retornara :matriz:(list) según los parametros recibidos. 
      '''
    matriz = []
    #i (q se convierte en valor_inicial) se va a repetir según el rango de cantidad de columnas indicadas
    #y estas se repiten sesegún la cantidad de filas 
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz


def carga_matriz_secuencialmente(matriz:list):
    '''
    Función que permite cargar una matriz ya inicializada, de manera secuencial
    
    Args:
    :param matriz: lista de lista sobre la que se hará la carga
    
    :fila: calcula cuantas filas tiene la matriz
    :columnas: calcula cuantas columas hay por fila tomando como para metro el indice 0
    
    :return: devuelve la matriz cargada con los valores ingresados
    
    '''
    fila = len(matriz)
    columnas = len(matriz[0])

    for i in range(fila):
        print(f"Carga de las notas del alumno: {i+1}")
        for j in range(columnas):
            materia = input("Ingrese que materia quiere cargar (1-5): ")
            while contiene_numero(materia) == False:
                materia = input("ERROR. Ingrese que materia quiere cargar (1-5): ")
            materia = int(materia)-1
            while materia < 0 or materia > 4:  
                materia = input("ERROR. Ingrese que materia quiere cargar (1-5): ")
            while matriz[i][materia] != 0:
                 materia = input("La nota de la materia seleccionada para este alumno ya fue cargado\n" \
                 "Ingrese que materia quiere cargar (1-5): ")

            nota = input("Ingrese la nota(1 a 10): ") 
            while contiene_algo == False:
                nota =input("ERROR. Ingrese la nota(1 a 10): ")
            while contiene_numero(nota) == False:  
                nota =input("ERROR. Ingrese la nota(1 a 10): ")
            nota = int(nota)
            while nota < 1 or nota > 10: 
                nota =input("ERROR. Ingrese la nota(1 a 10): ")
            matriz[i][materia] = nota
    return matriz


def mostrar_matriz (matriz):
    '''
    Función que imprime la matriz correctamente
    '''
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            print (matriz[fila][columna], end= "")
        print()


def mostrar_lista(lista:list):
    '''
    función que imprime la lista correctamente, un valor debajo de otro
    '''
    for i in range(len(lista)):
        print(lista[i])
    

def mostrar_datos (lista_a:list, lista_b:list, lista_c:list, matriz = 0, opcional_1 = 0)-> None:
    '''
    Función que imprime los parametros (4) ingresados de manera correcta.
    Como una matriz, donde los contenidos de cada listas se imprimen uno debajo del otro
    Cada parametro se imprime uno al lado del otro 
    
    Args:
    :param lista_a: (list) primer parametro
    :param lista_b: (list) segundo parametro
    :param lista_c: (list) tercer parametro
    :param matriz: parametro opcional
    :param opcional_1: parametro opcional
    '''
    #tres listas
    if matriz == 0 and opcional_1 == 0:
        for i in range(len(lista_a)):
            print(f"{lista_a[i]}\t{lista_b[i]}\t{lista_c[i]}")
  
#tres listas y 1 matriz
    elif matriz != 0 and opcional_1 == 0:
        for i in range(len(lista_a)):
            print(f"{lista_a[i]}\t{lista_b[i]}\t{lista_c[i]}", end="\t")
            for j in range(len(matriz[i])):
                print (matriz[i][j], end= " ")
            print()

#4 listas y 1 matriz
    elif matriz != 0 and opcional_1 != 0:
        opcional_1 = calcular_promedio(matriz)
        for i in range(len(lista_a)):
            print(f"{lista_a[i]}\t{lista_b[i]}\t{lista_c[i]}\t{opcional_1[i]}", end="\t")
            for j in range(len(matriz[i])):
                print (matriz[i][j], end= " ")
            print()



#CALCULA EL PROMEDIO POR FILA
def calcular_promedio(matriz)-> list[float]:
    '''
    Función que recorre las filas matriz, suma los valores contenidos en las intersecciones y 
    los divide por la cantindad de columnas, para obtener el promedio de cada fila y a estos guardarlos en
    una nueva lista.
    
    Args:
    :param matriz: lista de lista sobre la que se calculara el promedio
    
    :return: retorna una lista con los promedios de cada fila de la matriz
    '''
    lista_promedios = []
    for fila in range(len((matriz))):      
        suma = 0
        contador = 0
        for columna in range(len(matriz[fila])):     
            suma += matriz[fila][columna]       
            contador += 1                   
        if contador > 0:
            promedios = suma / contador
        else:
            promedios = 0
        lista_promedios += [promedios]       
    return lista_promedios

#PROMEDIOS
def promedios_por_columnas(matriz)-> list:
    '''
    Función que calcula el promedio de las columas contenidas en una matriz

    Args:
    :param matriz: lista de listas sobre el que se calculara el promedio de sus columnas

    :cantidad_filas: cuenta cantidad de filas
    :cantidad_columas: cuenta cantidad de columnas que tiene el parametro desde el indice 0
    :promedio_columnas: (list) inicializo la lista según la cantidad de columnas ingresadas. Se guardaran los promedios
    
    :return: devuelve promedio_columnas actualizada con los promedios de cada columna 
    '''
    
    cantidad_filas = len(matriz) 
    cantidad_columnas = len(matriz[0]) 
    promedio_columna= [0]* cantidad_columnas
    for j in range(cantidad_columnas): 
        suma= 0 
        contador = 0
        for i in range(cantidad_filas): 
            if matriz[i][j] > 0:
                suma += matriz[i][j]
                contador += 1
        if contador > 0:            #si hay un valor mayor a cero calculo el promedio
            promedio_columna[j] = suma / contador
        else:
            promedio_columna[j] = 0 #para evitar q se rompa
    return promedio_columna


def promedio_mayor(matriz)-> str:
    '''
    Función que calcula cual es el promedio mayor de los promedios de las columnas

    Args:
    :param matriz: lista de lista sombre la que se calculara el promedio de sus columnas
                    y sobre estos, se calculara cual fue mayor.
    
    :promedio: lista donde se guardara la lista de los promedios por columnas sobre el parametro ingresado
    :mayor: bandera que contiene el indice 0, este se ira comparando con el siguiente 
    :mayores: cadena vacía deonde se iran guardando los valores de 'mayor' en caso de que haya mas de uno

    :return: devuelve el promedio de mayor valor
    '''
    promedio = promedios_por_columnas(matriz)   
    mayor = promedio[0]                     
    #comienza en 1 xq 0 esta en 'mayor'. los comparo, de 1 ser mas grande q 0, se actualiza mayor
    for i in range(1, len(promedio)):  
        if promedio[i] > mayor:  
            mayor = promedio[i]  
    mayores=""        
    for i in range(len(promedio)):  #recorro nuevamente par ver si hay mas de  1 promedio mayor
        if promedio[i] == mayor:    
            mayores += (f"MATERIA_{i+1}\tPromedio: {promedio[i]}\n")    #\n para q el siguiente se imprima abajo
    return mayores


    

def ordenar(lista_a:list, lista_b:list, lista_c:list, primer_modo = 1, segundo_modo = 2) ->None:
    '''
    Función que ordena los parametros:list de manera ascendente( modo 1) o descende(modo 2) según el modo ingresado.
    Toma como primer críterio de ordenamiendo a lista_c que se ordenara según lo que indique primer_modo
    Como segundo criterio, en caso de que el primero resulte en empana, toma a lista_a y 
    lo ordenará según lo que indique segundo_modo

    :param lista_a: primera lista (segúndo criterio de ordenamiendo)
    :param lista_b: segunda lista 
    :param lista_c: tercera lista (primer criterio de ordenamiendo)
    :param primer_modo: odena a lista_c. 1 = ascendente, 2 =  descendente
                        Si no se le da un parametro de ordenamiendo(1-2), orderará de manera ascendente (1)
    :param segundo_modo: en caso de empate, orderana a lista_2 según el modo indicado: 1= ascendente, 2 = descendente
                        Si no se le da un parámetro de ordenamiento(1-2), ordenará de manera descendente (2)
    '''
#i recorre la lista de 0 al anteultimo, xq j es quien va a recorrer hasta el ultimo(i+1 xq 0 se recorrer en i)
    for i in range(0, len(lista_a)-1, 1): 
        for j in range(i+1, len(lista_a), 1): # Compara i con todos los siguientes
#comparo indice i(q es 0) con indice j(q es 1) si es mayor o menor y los voy ordenando y asi hasta recorrer toda la lista
            if (lista_c[i] > lista_c[j] and primer_modo == 1) or (lista_c[i] < lista_c[j] and primer_modo == 2) :
                #Swap(intercambio)
                primer_auxiliar = lista_b[i]
                lista_b[i] = lista_b[j]
                lista_b[j] = primer_auxiliar

                segundo_auxiliar = lista_a[i]
                lista_a[i] = lista_a[j]
                lista_a[j] = segundo_auxiliar

                tercer_auxiliar = lista_c[i]
                lista_c[i] = lista_c[j]
                lista_c[j] = tercer_auxiliar
                #2do criterio. Si los valores de la lista c son iguales, entra el segundo criterio
            elif lista_c[i] == lista_c[j]:  
                 if (lista_a[i] > lista_a[j] and segundo_modo == 1) or (lista_a[i] < lista_a[j] and segundo_modo == 2):
                    primer_auxiliar = lista_b[i]
                    lista_b[i] = lista_b[j]
                    lista_b[j] = primer_auxiliar

                    segundo_auxiliar = lista_a[i]
                    lista_a[i] = lista_a[j]
                    lista_a[j] = segundo_auxiliar

                    tercer_auxiliar = lista_c[i]
                    lista_c[i] = lista_c[j]
                    lista_c[j] = tercer_auxiliar


def buscador(valor:int, lista:list) -> int:
    '''
    Función que recorre el segundo parametro, busca el valor indicado en el primer parametro y guarda su indice
    :param valor: (int) primer parametro, valor a ser buscado
    :param lista: (list) segundo parametro, lista sombre la que se buscara el valor indicado
    
    :return: devuelve el indice que contiene que valor que se busco en la lista
    '''
    indice= None
    for i in range(len(lista)):   
        if lista[i] == valor:       
            indice = i              
    return indice



def contador_notas(matriz:list, materia=int) -> list:
    '''
    función que retorna la cantidad de veces que se repiten los valores (1-10) de un indice(materia) en la matriz recibida
    
      Args:
    :param matriz: lista sobre la que se hara la busqueda
    :param materia: inidice de la matriz recibida

    :return: (list) Lista con la cantidad de veces que se repiten los números   
         '''
    contador_calificaciones = [0] * 10
    
    i = materia - 1 
#for va a recorrer las notas de cad fila de la matriz, no los indices
    for fila in matriz:
        #nota es el numero q se encontro en la interseccion fila/columna
        nota = fila[i]
        if nota >= 1 and nota <= 10:
            #cuenta  la cantidad de veces q aparecio esa nota en ese recorrido
            contador_calificaciones[nota -1] += 1
             #[nota - 1] me va inidicar el inidice correcto donde se tienen q guardar cda recuento
    return contador_calificaciones

