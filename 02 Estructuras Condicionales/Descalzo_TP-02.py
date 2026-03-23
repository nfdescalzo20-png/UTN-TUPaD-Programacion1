#Ejercicio 1
try:
    edad = int(input("Por favor, ingrese su edad: "))
    if edad > 18:
        print("Es mayor de edad.")
    else:
        pass
except:
    print("Por favor, ingrese un número.")

#Ejercicio 2
try:
    nota = int(input("Por favor, ingrese su nota: "))
    if nota >= 6 and nota <= 10:
        print("Aprobado.")
    elif nota >= 1 and nota < 6:
        print("Desaprobado.")
    else:
        pass
except:
    print("Por favor, ingrese un número.")

#Ejercicio 3
try:
    numero = int(input("Por favor, ingrese un numero: "))
    if numero%2 == 0:
        print("Ha ingresado un número par.")
    else:
        print("Por favor, ingrese un número par.")
except:
    print("Por favor, ingrese un número.")

#Ejercicio 4
try:
    edad = int(input("Por favor, ingrese su edad: "))
    if edad < 12:
        print("Niño/a.")
    elif edad >= 12 and edad < 18:
        print("Adolescente.")
    elif edad >= 18 and edad < 30:
        print("Adulto/a joven.")
    elif edad >= 30:
        print("Adulto/a.")
    else:
        pass
except:
    print("Por favor, ingrese un número.")

#Ejercicio 5
contra = len(input("Ingrese una contraseña de entre 8 y 14 caracteres"))
if contra >= 8 and contra <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#Ejercicio 6
try:
    consumo = int(input("Por favor, ingrese el consumo mensual de energía eléctrica (en KWh): "))
    if consumo >= 0 and consumo < 150:
        print("Consumo bajo.")
    elif consumo >= 150 and consumo <= 300:
        print("Consumo medio.")
    elif consumo > 300:
        print("Consumo alto.")
        if consumo > 500: 
            print("Considere medidas de ahorro energético.")
        else:
            pass
    else:
        pass
except:
    print("Por favor, ingrese un número.")

#Ejercicio 7
frase = input("Por favor, ingrese una frase o palabra: ")
if frase[len(frase)-1] in "aeiouáéíóú":
    frase += "!"
    print(frase)
else:
    print(frase)

#Ejercicio 8
nombre = input("Por favor, ingrese su nombre: ")
numero = int(input("Si quiere su nombre en mayúsculas, ingrese 1. Si quiere su nombre en minúsculas, ingrese 2. Si quiere su nombre con la primera letra mayúscula, ingrese 3."))
if numero == 1:
    nombre = nombre.upper()
    print(nombre)
elif numero == 2:
    nombre = nombre.lower()
    print(nombre)
elif numero == 3:
    nombre = nombre.title()
    print(nombre)
else:
    pass

#Ejercicio 9
try:
    mag = int(input("Por favor, ingrese la magnitud del terremoto: "))
    if mag >= 0 and mag < 3:
        print("Muy leve.")
    elif mag >= 3 and mag < 4:
        print("Leve.")
    elif mag >= 4 and mag < 5:
        print("Moderado.")
    elif mag >= 5 and mag < 6:
        print("Fuerte.")    
    elif mag >= 6 and mag < 7:
        print("Muy Fuerte.")
    elif mag >= 7:
        print("Extremo.")
    else:
        pass
except:
    print("Por favor, ingrese un número.")

#Ejercicio 10
try:
    hemi = input("Por favor, ingrese el hemisferio en el que se encuentra (norte o sur): ")
    mes = input("Ahora, ingrese el mes del año en el que se encuentra: ")
    dia = int(input("Ahora, ingrese el día del año en el que se encuentra: "))
    if hemi == "norte":
        if mes in ("diciembre","enero","febrero","marzo"):
            if mes == "diciembre":
                if dia >= 21 and dia <= 31:
                    print("Invierno")
                else:
                    print("Otoño")
            elif mes == "marzo":
                if dia >= 1 and dia <= 20:
                    print("Invierno")
                else:
                    print("Primavera")
            else:
                print("Invierno")
        elif mes in ("abril","mayo","junio"):
            if mes == "junio":
                if dia >= 1 and dia <= 20:
                    print("Primavera")
                else:
                    print("Verano")                
            else:
                print("Primavera")
        elif mes in ("julio","agosto","septiembre"):
            if mes == "septiembre":
                if dia >= 1 and dia <= 20:
                    print("Verano")
                else:
                    print("Otoño")                
            else:
                print("Verano")
        elif mes in ("octubre","noviembre"):
            print("Otoño")
        else:
            pass                               
    elif hemi == "sur":
        if mes in ("diciembre","enero","febrero","marzo"):
            if mes == "diciembre":
                if dia >= 21 and dia <= 31:
                    print("Verano")
                else:
                    print("Primavera")
            elif mes == "marzo":
                if dia >= 1 and dia <= 20:
                    print("Verano")
                else:
                    print("Otoño")
            else:
                print("Verano")
        elif mes in ("abril","mayo","junio"):
            if mes == "junio":
                if dia >= 1 and dia <= 20:
                    print("Otoño")
                else:
                    print("Invierno")
            else:
                print("Otoño")
        elif mes in ("julio","agosto","septiembre"):
            if mes == "septiembre":
                if dia >= 1 and dia <= 20:
                    print("Invierno")
                else:
                    print("Primavera")
            else:
                print("Invierno")
        elif mes in ("octubre","noviembre"):
            print("Primavera")    
    else:
        pass
except:
    print("Por favor, ingrese un valor correcto.")