#Ejercicio 1
print("Hola Mundo!")

#Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre + " " + apellido}, tengo {edad} años y vivo en {residencia}.")

#Ejercicio 4
radio = int(input("Ingrese la longitud del radio: "))
import math
area = int(math.pi*radio**2)
perimetro = int(2*math.pi*radio)
print(f"El circulo de radio {radio} tiene un area de {area} centimetros aproximados, y {perimetro} centimetros aproximados de perimetro.")

#Ejercicio 5
segundos = int(input("Ingrese una cantidad de segundo/s: "))
horas = int(segundos/60)
resto = segundos - horas*60
print(f"{segundos} segundo/s equivalen a {horas} hora/s con {resto} segundo/s.")

#Ejercicio 6
numero = int(input("Ingrese un numero: "))
for i in range(1,11):
    m = i*numero
    print(f"{i} por {numero} es igual a {m}.")

#Ejercicio 7
numero = int(input("Ingrese un numero entero mayor a cero: "))
otro_numero = int(input("Ingrese otro numero entero mayor a cero: "))
print(f"El resultado de sumar {numero} con {otro_numero} es {numero + otro_numero}")
print(f"El resultado de dividir {numero} con {otro_numero} es {numero // otro_numero}")
print(f"El resultado de multiplicar {numero} con {otro_numero} es {numero * otro_numero}")
print(f"El resultado de restar {numero} con {otro_numero} es {numero - otro_numero}")

#Ejercicio 8
altura = float(input("Ingrese su altura (en metros): "))
peso = float(input("Ingrese su peso (en kilogramos): "))
imc = int(peso/(altura**2))
print(f"Su Indice de Masa Corporal es igual a {imc}")

#Ejercicio 9
c = int(input("Ingrese la temperatura (en grados Celsius): "))
f = (9/5) * c + 32
print(f"{c} grados Celsius equivalen a {f} grados Fahrenheit.")

#Ejercicio 10
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
n3 = int(input("Ingrese otro numero: "))
p = (n1+n2+n3)/3
print(f"El promedio de los numeros ingresados es igual a {p}.")