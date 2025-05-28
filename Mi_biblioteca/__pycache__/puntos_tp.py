"""
Una institución educativa desea procesar los datos de sus estudiantes.
Para ello, se tienen los siguientes datos:
 Una matriz de enteros, de 30 filas por 5 columnas donde:
o Cada fila representa un estudiante.
o Cada columna representa una materia.
o Cada valor en la intersección es una calificación entera entre 1 y 10.
 Una lista de nombre de los estudiantes.
 Una lista de géneros de los estudiantes. Cada género debe ser alguno de los siguientes: [‘F’ | ‘M’ | ‘X’]
 Una lista de legajos de los estudiantes. Cada legajo debe ser numérico del tipo entero de cinco cifras.
Cada una de estas listas, se corresponden con las filas de la matriz. Es decir, que se debe trabajar como listas
paralelas entre la matriz y las otras listas.
Se deberá programar un menú de opciones operado por consola, que realice lo siguiente:
1 – Realizar la carga de los datos en la matriz y en cada una de las listas. Realizar una función para validar cada
dato a ser cargado.
2 – Mostrar todos los datos, esto es la matriz completa de calificaciones conjuntamente con las listas de legajo,
género y nombre del estudiante .Realizar una función que muestre uno y otra que muestre todos.
3 – Calcular el promedio de cada estudiante y guardarlo en una nueva lista. Realizar una función que calcule el
promedio.
4 – Ordenar y mostrar los datos de los estudiantes por promedio de manera DESC. Realizar una función que
ordene, la cual deberá ordenar de manera ASC o DESC de acuerdo a un parámetro de ordenamiento.
5 – Mostrar la/s materia/s con mayor promedio general. Realizar una función para mostrar todas y otra para
mostrar una. Teniendo en cuenta que no hay una lista de materias, sino que cada columna de la matriz
representa una materia, entonces cada materia tomará la siguiente nomenclatura para su nombre MATERIA_
índice más uno. Por ejemplo: para la materia del índice cero de la columna, será MATERIA_1.
6 – Buscar y mostrar todos los datos de un estudiante por legajo, incluyendo el promedio calculado en el ítem 3.
Realizar una función de búsqueda. Realizar una función que muestre uno y otra que muestre todos.
7 – Realizar una funcion que reciba la matriz de calificaciones y el número de materia (indice más uno) como parámetros, 
y retorne una lista de elementos, donde en el indice 0 estará la cantidad de veces que re repite la nota 1,
en el indice 1 estará la cantidad de veces que re repite la nota 2, y así sucesivamente hasta el inidice 9 donde estará
la cantidad de veces que re repite la nota 10.
8 - Salir del programa.
NOTAS:
Nota 0: Los datos de la matriz y las listas podrán estar hardcodeados a los efectos de realizar las pruebas de
funcionamiento correspondientes.
Nota 1: No se podrá acceder a ningún ítem del menú, sin antes haber cargado los datos. En tal sentido, realizar la
validación correspondiente.
Nota 2: Los puntos deben ser accedidos mediante un menú de opciones.
Nota 3: Cada ítem del menú deberá ser una función.
Nota 4: Se deberá desarrollar biblioteca y funciones propias, las mismas deberán estar correctamente documentadas.
Nota 5: Se deberá desarrollar una función para la validación de cada uno de los datos.
Nota 6: Desarrollar una función que recorra los elementos (mostrar todos) y otra que muestre un elemento (mostrar uno).
La segunda será llamada dentro de la primera.
Nota 7: Para realizar el menú de opciones, se deberá utilizar la estructura de control match.
Nota 8: El menú de opciones deberá estar contenido dentro (anidado) de una estructura de control while

"""