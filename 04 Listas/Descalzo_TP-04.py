#Ejercicio 1
notas = [10,9,8,7,6,5,4,3,2,1] #Lista con notas de 10 estudiantes

a = 0 #Mostrar la lista completa
for n in notas:
    a += 1
    if a != 10:
        print(n, end=" ")
    else:
        print(n)

print(f"El promedio de las {len(notas)} notas es {sum(notas)/len(notas)}.") #Promedio de las notas
print(f"La nota mas alta fue {max(notas)}.") #Nota mas alta
print(f"La nota mas baja fue {min(notas)}.") #Nota mas baja

#Ejercicio 2
lista = [] #Lista de productos

for i in range(5): #Pide al usuario ingresar 5 productos
    lista.append(input("Ingrese 5 productos en su lista: "))

a = 0 #Muestra los productos ordenados alfabeticamente
for i in sorted(lista):
    a += 1
    if a != len(lista):
        print(i, end=" ")
    else:
        print(i)
print("")

eliminar = input("Desea eliminar algun producto? ") #Pregunta al usuario que desea eliminar

if eliminar in lista: #Busca el elemento en la lista y lo elimina, si existe
    lista.remove(eliminar)
    for i in sorted(lista):
        a += 1
        if a != len(lista):
            print(i, end=" ")
        else:
            print(i)
else:
    print("El producto seleccionado no pertenece a la lista.")
print("")

#Ejercicio 3
numeros = [] #Lista de numeros
pares = [] #Lista de numeros pares
impares = [] #Lista de numeros impares

import random #Genera 15 numeros randoms y los agrega a una lista
for i in range(15):
    numero = random.randint(1,100)
    numeros.append(numero)

for i in numeros: #Evalua si los numeros son pares o impares y los agrega una lista para cada categoria
    if i%2 == 0:
        pares.append(i)
    else:
        impares.append(i)

a = 0 #Imprime la lista de numeros pares
print(f"La lista de numeros pares es: ")
for i in pares:
    a += 1
    if a != len(pares):
        print(i, end=" ")
    else:
        print(i)
print("")

a = 0 #Imprime la lista de numeros impares
print(f"La lista de numeros impares es: ")
for i in impares:
    a += 1
    if a != len(impares):
        print(i, end=" ")
    else:
        print(i)
print("")

print(f"La lista de numeros pares contiene {len(pares)} numeros y la lista de numeros impares contiene {len(impares)}") #Cuenta la cantidad de numeros en cada lista.

#Ejercicio 4
datos = [1,3,5,3,7,1,9,5,3] #Lista de numeros
datos2 = [] #Nueva lista sin elementos repetidos

for i in datos: #Agrega numeros sin repetir a otra lista
    if not i in datos2:
        datos2.append(i)

a = 0
for i in datos2: #Muestra la lista de numeros sin repetir
    if a != len(datos2):
        print(i, end=" ")
    else:
        print(i)

#Ejercicio 5
estudiantes = ["Jorge","Rodrigo","Pablo","Diego","Sebastian","Maria", "Agustina","Facundo"] #Lista de estudiantes

a = 0 #Muestra la lista original
for i in estudiantes:
    if a != len(estudiantes):
        print(i,end=" ")
    else:
        print(i)

salir = False
while not salir: #Menu que se repite hasta que se presione S

    opcion = input("Desea (A)gregar o (E)liminar un estudiante? \n" #Pide que se elija una opcion e imprime por pantalla             
    "Si lo que desea es terminar, presione S: ")
    print(f"\nOpcion: {opcion}")

    if opcion in "Aa": #Opcion Agregar (Opcion A)

        while True: #Valida que el nombre elegido contenga solo letras, y que ya no se encuentre en la lista, y lo agrega a la lista.
            agregar = input("Ingrese el nombre del estudiante (solo letras): ")
            print(f"Estudiante: {agregar}")
            if agregar.isalpha:
                if agregar in estudiantes:
                    print("El estudiante ya se encuentra en la lista.")
                    break
                else:
                    estudiantes.append(agregar)
                    a = 0
                    for i in estudiantes:
                        if a != len(estudiantes):
                            print(i,end=" ")
                        else:
                            print(i)
                    break
            else:
                print("Error. Solo letras.")

    elif opcion in "Ee": #Opcion Eliminar (Opcion E)

        while True: #Valida que el nombre elegido contenga solo letras, y que se encuentre en la lista, y lo elimina de la lista.
            eliminar = input("Ingrese el nombre del estudiante (solo letras): ")
            print(f"Estudiante: {eliminar}")
            if eliminar.isalpha:            
                if not eliminar in estudiantes:
                    print("El estudiante no se encuentra en la lista.")
                    break
                else:
                    estudiantes.remove(eliminar)
                    for i in estudiantes:
                        if a != len(estudiantes):
                            print(i,end=" ")
                        else:
                            print(i)                 
                    break
            else:
                print("Error. Solo letras.")
                
    elif opcion in "Ss": #Opcion Salir (Opcion S)
        break

    else: #Opcion Incorrecta
        print("Error. Ingrese una opcion valida.")

#Ejercicio 6
numeros = [2,3,4,5,6,7,1] #Lista con 7 numeros.
numeros2 = [] #Lista con 7 numeros una posicion hacia la derecha.

numeros2.append(numeros[len(numeros)-1]) #Coloca el ultimo numero de la primera lista al inicio de la segunda
for i in range(len(numeros)-1): #Coloca los 6 primeros numeros una posicion mas adelante
    numeros2.insert(i+1,numeros[i])

a = 0 #Muestra la lista de numeros original
for i in numeros:
    if a != len(numeros):
        print(i,end=" ")
    else:
        print(i)
print("")

for i in numeros2: #Muestra la nueva lista de numeros
    if a != len(numeros2):
        print(i,end=" ")
    else:
        print(i)
print("")

#Ejercicio 7
dia = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"] #Filas
temperatura = ["Minima","Maxima"] #Columnas
matriz_temperatura = [[20,24], #Matriz con temperaturas minimas y temperaturas maximas de los ultimos 7 dias
                      [21,26],
                      [22,29],
                      [22,27],
                      [23,28],
                      [22,27],
                      [22,26]]

for i in range(7): #Imprime los datos de la matriz
    for j in range(2):
        if j != 1:
            print(matriz_temperatura[i][j], end=" ")
        else:
            print(matriz_temperatura[i][j])
print("")

matriz_min_max = [[],[]] #Se calcula el promedio de las temperaturas minimas y las maximas y se imprime en pantalla
for i in range(7):
    for j in range(2):
        matriz_min_max[j].append(matriz_temperatura[i][j])
prom_minima = sum(matriz_min_max[0])/len(matriz_temperatura)
prom_maxima = sum(matriz_min_max[1])/len(matriz_temperatura)
print(f"El promedio de las temperaturas minimas es {prom_minima:.2f} y el de las temperaturas maximas es {prom_maxima:.2f}.")

amplitud = [0,0,0,0,0,0,0] #Se calcula el dia con mayor amplitud termica y se imprime en pantalla
for i in range(2):
    for j in range(7):
        if amplitud[j] == 0:
            amplitud[j] -= matriz_min_max[i][j]
        else:
            amplitud[j] += matriz_min_max[i][j]
print(f"El dia que se registro la mayor amplitud termica fue el dia {dia[amplitud.index(max(amplitud))]}.")

#Ejercicio 8
nombres = ["Ana", "Beto", "Carla", "David", "Elena"] #Lista con filas
materias = ["Quimica", "Fisica", "Matematicas"] #Lista con columnas
matriz_estudiantes = [[10,5,7], #Matriz con las notas de 5 estudiantes en 3 materias
                      [8,4,2],
                      [1,4,2],
                      [2,4,9],
                      [5,8,3]]
matriz_promedio1 = [] #Lista con promedios por estudiante
matriz_promedio2 = [[],[],[]] #Lista con promedios por materia

for i in range(5): #Imprime los datos de la matriz
    for j in range(3):
        if j != 2:
            print(matriz_estudiantes[i][j], end=" ")
        else:
            print(matriz_estudiantes[i][j])
print("")

for i in range(5): #Calcula el promedio de cada estudiante y lo imprime por pantalla
    prom_estudiante = sum(matriz_estudiantes[i])/len(matriz_estudiantes[i])
    matriz_promedio1.append(prom_estudiante)
    print(f"El promedio de {nombres[i]} fue de {matriz_promedio1[i]:.2f}.")
print("")

for i in range(5): #Calcula el promedio de cada materia y lo imprime por pantalla
    for j in range(3):
        matriz_promedio2[j].append(matriz_estudiantes[i][j])
for i in range(3):
    prom_materias = sum(matriz_promedio2[i])/len(matriz_promedio2[i])
    print(f"El promedio en {materias[i]} fue de {prom_materias}.")

#Ejercicio 9
posicion = [11,12,13,21,22,23,31,32,33] #Lista con posiciones del tateti
matriz_tateti = [["-","-","-"], #Matriz con tateti
                 ["-","-","-"],
                 ["-","-","-"]]
fila = ""
columna = ""
t = True

for i in range(3): #Imprime por pantalla el tateti
    for j in range(3):
        if j != 2:
            print(matriz_tateti[i][j], end=" ")
        else:
            print(matriz_tateti[i][j])
print("")

while t: #El juego se ejecuta hasta haber un ganador

    while not fila in (1,2,3): #Valida que el valor ingresado como fila sea un numero dentro del rango
        while not fila.isnumeric():
            fila = input("Ingrese una fila para X: ")
            if not fila.isnumeric():
                print("Error. Ingrese un numero.")
        fila = int(fila)
        if not fila in (1,2,3):
            print("Error. El valor ingresado esta fuera del rango.")
            fila = ""
    
    while not columna in (1,2,3): #Valida que el valor ingresado como columna sea un numero dentro del rango
        while not columna.isnumeric():
            columna = input("Ingrese una columna para X: ")
            if not columna.isnumeric():
                print("Error. Ingrese un numero.")
        columna = int(columna)
        if not columna in (1,2,3):
            print("Error. El valor ingresado esta fuera del rango.")
            fila = ""

    matriz_tateti[fila-1][columna-1] = "X" #Ingresa la opcion elegida en el tateti

    for i in range(3): #Imprime por pantalla el tateti
        for j in range(3):
            if j != 2:
                print(matriz_tateti[i][j], end=" ")
            else:
                print(matriz_tateti[i][j])
    print("")

    fila = "" #Reinicia los valores ingresados
    columna = ""

    while not fila in (1,2,3): #Valida que el valor ingresado como fila sea un numero dentro del rango
        while not fila.isnumeric():
            fila = input("Ingrese una fila para O: ")
            if not fila.isnumeric():
                print("Error. Ingrese un numero.")
        fila = int(fila)
        if not fila in (1,2,3):
            print("Error. El valor ingresado esta fuera del rango.")
            fila = ""
    
    while not columna in (1,2,3): #Valida que el valor ingresado como columna sea un numero dentro del rango
        while not columna.isnumeric():
            columna = input("Ingrese una columna para O: ")
            if not columna.isnumeric():
                print("Error. Ingrese un numero.")
        columna = int(columna)
        if not columna in (1,2,3):
            print("Error. El valor ingresado esta fuera del rango.")
            fila = ""
    
    matriz_tateti[fila-1][columna-1] = "O" #Ingresa la opcion elegida en el tateti

    for i in range(3): #Imprime por pantalla el tateti
        for j in range(3):
            if j != 2:
                print(matriz_tateti[i][j], end=" ")
            else:
                print(matriz_tateti[i][j])
    print("")
    
    fila = "" #Reinicia los valores ingresados
    columna = ""

    for i in range(3): #Evalua si alguno de los jugadores completo alguna de las lineas horizontales
        c_x = 0
        c_o = 0    
        for j in range(3):
            if matriz_tateti[i][j] == "X":
                c_x += 1
            elif matriz_tateti[i][j] == "O":
                c_o +=1
        if c_x == 3:
            print("El jugador X ha ganado.")
            t = False
            break
        elif c_o == 3:
            print("El jugador O ha ganado.")
            t = False
            break

    for i in range(3): #Evalua si alguno de los jugadores completo alguna de las lineas verticales
        c_x = 0
        c_o = 0    
        for j in range(3):
            if matriz_tateti[j][i] == "X":
                c_x += 1
            elif matriz_tateti[j][i] == "O":
                c_o +=1
        if c_x == 3:
            print("El jugador X ha ganado.")
            t = False
            break
        elif c_o == 3:
            print("El jugador O ha ganado.")
            t = False
            break
    
    
    c_x = 0 #Evalua si alguno de los jugadores completo la linea oblicua que inicia en el primer espacio del tateti
    c_o = 0    
    for i in range(3):
        if matriz_tateti[i][i] == "X":
            c_x += 1
        elif matriz_tateti[i][i] == "O":
            c_o +=1
    if c_x == 3:
        print("El jugador X ha ganado.")
        t = False
        break
    elif c_o == 3:
        print("El jugador O ha ganado.")
        t = False
        break

    c_x = 0 #Evalua si alguno de los jugadores completo la linea oblicua que inicia en el ultimo espacio del tateti
    c_o = 0    
    for i in range(2,-1,-1):
        if matriz_tateti[2-i][i] == "X":
            c_x += 1
        elif matriz_tateti[2-i][i] == "O":
            c_o +=1
    if c_x == 3:
        print("El jugador X ha ganado.")
        t = False
        break
    elif c_o == 3:
        print("El jugador O ha ganado.")
        t = False
        break

#Ejercicio 10
productos = ["a","b","c","d"] #Lista de filas
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"] #Lista de columnas
matriz_productos = [[4,2,6,3,4,6,8], #Matriz que contiene el total de ventas de 4 productos en 7 dias
                    [2,1,8,2,4,2,7],
                    [3,7,9,3,5,9,2],
                    [7,2,6,9,3,5,0]]
productos_suma = [0,0,0,0]
dias_suma = [0,0,0,0,0,0,0]

for i in range(4): #Calcula y muestra por pantalla el total vendido por cada producto.
        productos_suma[i] = sum(matriz_productos[i])
        print(f"El producto {productos[i]} vendio un total de {productos_suma[i]} unidades.")

for i in range(4): #Calcula y muestra por pantalla el dia con mayores ventas totales.
    for j in range (7):
        dias_suma[j] += matriz_productos[i][j]
print(f"El dia con mayor ventas fue el dia {dias[dias_suma.index(max(dias_suma))]}.")

print(f"El producto mas vendido fue {productos[productos_suma.index(max(productos_suma))]}.") #Muestra por pantalla el producto mas vendido de la semana.

#Ejercicio 11
nombres = ["Felipe", "Julieta", "Alejandro", "Victoria", "Leonardo", "Elena", "Gabriel", "Mariana", "Santiago", "Valentina"] #Lista con 10 estudiantes
minuscula = [] #Lista con nombres en minuscula

for i in nombres: #Agrega los nombres en minuscula a una lista
    minuscula.append(i.lower())

opcion = input("Ingrese un nombre: ") #Pide un nombre y, si se encuentra en la lista, indica su posicion
if opcion.lower() in minuscula:
    print(f"El nombre {opcion} esta en la lista. Ocupa el lugar numero {minuscula.index(opcion.lower())+1}")
else:
    print("El nombre no se encuentra en la lista")

#Ejercicio 12
numeros = [] #Lista con numeros enteros

for i in range(8): #Pide 8 numeros y, si son enteros, los agrega a la lista
    eleccion = ""
    while not eleccion.isdecimal():
        eleccion = input("Por favor, ingrese un numero entero: ")
        if not eleccion.isdecimal():
            print("Error. Debe ingresar un numero entero.\n")
    numeros.append(eleccion)

a = 0 #Imprime por pantalla la lista de numeros en el orden ingresado
print("Usted ha ingresado los siguientes numeros: ")
for i in numeros:
    if a != 7:
        print(i,end=" ")
        a += 1
    else:
        print(i)
print("")

a = 0 #Imprime por pantalla la lista de numeros ordenada de menor a mayor
print("Los numeros ordenados del menor a mayor son: ")
for i in sorted(numeros):
    if a != 7:
        print(i,end=" ")
        a += 1
    else:
        print(i)
print("")

a = 0 #Imprime por pantalla la lista de numeros ordenada de mayor a menor
print("Los numeros ordenados del mayor a menor son: ")
for i in sorted(numeros, reverse=True):
    if a != 7:
        print(i,end=" ")
        a += 1
    else:
        print(i)
print("")

#Ejercicio 13
puntajes = [450, 1200, 875, 990, 300, 1500, 640] #Lista de puntajes

print(f"El puntaje mas alto fue {max(puntajes)} y el mas bajo fue {min(puntajes)}.\n") #Imprime por pantalla el puntaje mas alto y el mas bajo

a = 1 #Muestra la lista de puntajes ordenadas de mayor a menor en forma de ranking
print("Ranking: ")
for i in sorted(puntajes, reverse=True):
        print(f"{a}. {i}")
        a += 1

print(f"\nEl puntaje 990 esta en la posicion {sorted(puntajes, reverse=True).index(990)+1}.") #Imprime por pantalla la posicion del puntaje 990.