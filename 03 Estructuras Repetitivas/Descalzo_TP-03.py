#Ejercicio 1
cliente = "" #Variables iniciales
cantidad = ""
total_sin = 0
total_con = 0
ahorro = 0
promedio = 0

while not cliente.isalpha(): #Validacion de nombre
    cliente = input("Por favor, ingrese su nombre (solo letras): ")
    print(f"Cliente: {cliente}")
    if not cliente.isalpha():
        print("Error: Ingrese un nombre válido.")

while not cantidad.isdigit(): #Validacion de cantidad
    cantidad = input("Por favor, ingrese la cantidad de productos (solo numeros): ")
    print(f"Cantidad de productos: {cantidad}")
    if not cantidad.isdigit():
        print("Error: Ingrese un numero válido.")

for producto in range(1,int(cantidad)+1): #Informacion de cada producto
    precio = ""
    descuento = ""

    while not precio.isdigit(): #Validacion de precio
        precio = input(f"Por favor, ingrese el precio del producto {producto}: ")
        if not precio.isdigit():
            print("Error: Ingrese un numero válido.")

    total_sin += int(precio) #Suma el precio a la variable con el total sin descuento

    while not descuento in ("S","s","N","n"): #Validacion de descuento
        descuento = input(f"Por favor, ingrese si el producto {producto} tiene descuento (S/N): ")
        if not descuento in ("S","s","N","n"):
            print("Error: Ingrese una de las opciones validas.")

    if descuento in ("S","s"): #Suma el precio a la variable con el total con descuento, de corresponder
        total_con += int(precio)*(90/100)
    else:
        total_con += int(precio)
    
    print(f"Producto {producto} - Precio: {precio} Descuento (S/N): {descuento}") #Imprime informacion sobre cada producto

ahorro = total_sin - total_con #Ahorro total

promedio = total_sin/int(cantidad) #Promedio por producto

print(f"\nTotal sin descuentos: ${total_sin}\n" #Imprime totales
      f"Total con descuentos: ${total_con}\n"
      f"Total con descuentos: ${total_con}\n"
      f"Ahorro: ${ahorro}\n"
      f"Promedio por producto: ${promedio:.2f}"
      )

#Ejercicio 2
usuario_correcto = "alumno" #Variables iniciales
clave_correcta = "python123"
intento = 0
seleccion = 0

while intento < 3: #Intentos para ingresar
    intento += 1
    usuario = input("Ingrese su nombre de usuario: ")
    clave = input("Ingrese su clave: ")
    
    if usuario == usuario_correcto and clave == clave_correcta: #Validacion de credenciales
        print(f"Intento {intento}/3 - Usuario: {usuario}\n"
              f"Clave: {clave}\n"
              "Acceso concedido\n"
              "\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir"
              )
        
        while seleccion != 4:
            seleccion = input("Elija una opcion: ")
            print(f"Opción: {seleccion}")
            if seleccion.isdigit() and int(seleccion) in range(1,5): #Validacion de opcion elegida

                if int(seleccion) == 1: #Estado de inscripcion (Opcion 1)
                    print("Inscripto")

                elif int(seleccion) == 2: #Cambiar clave (Opcion 2)
                    while len(nueva_clave) < 6:
                        nueva_clave = input("Ingrese su nueva clave: ")
                        if len(nueva_clave) < 6:
                            print(f"Nueva clave: {nueva_clave}")
                            print("Error: mínimo 6 caracteres")
                        else:
                            clave_correcta = nueva_clave
                            print(f"Nueva clave: {clave_correcta}")

                elif int(seleccion) == 3: #Mensaje motivacional (Opcion 3)
                    print("Da lo mejor de ti, siempre.")

                elif int(seleccion) == 4: #Salir (Opcion 4)
                    break

            elif seleccion.isdigit() and not int(seleccion) in range(1,5):
                print("Error: opción fuera de rango.")

            else:
                print("Error: ingrese un numero válido.")
        break

    else:
        print(f"Intento {intento}/3 - Usuario: {usuario}\n"
              f"Clave: {clave}\n"
              "Error: credenciales inválidas.\n"
              )
        if intento == 3:
           print("Limite de intentos excedido.") 

#Ejercicio 3
nombre = "" #Variables iniciales
seleccion = 0
dia = ""
paciente = ""
lunes = "Libre Libre Libre Libre"
Ocupados_lunes = 0
martes = "Libre Libre Libre"
Ocupados_martes = 0

while not nombre.isalpha(): #Validacion de nombre
    nombre = input("Por favor, ingrese su nombre (solo letras): ")
    print(f"Nombre: {nombre}")
    if not nombre.isalpha():
        print("Error: Ingrese un nombre válido.")

print("1. Reservar Turno\n"
    "2. Cancelar turno (por nombre)\n"
    "3. Ver agenda del día\n"
    "4. Ver resumen general\n"
    "5. Cerrar sistema.\n")

while seleccion != 5: #Menu repetitivo hasta salir
    seleccion = input("Elija una opcion: ")

    if seleccion.isdigit() and int(seleccion) in range(1,6):

        if int(seleccion) == 1: #Reservar turno (Opcion 1)

            while not paciente.isalpha(): #Validacion de nombre
                paciente = input("Ingrese el nombre del paciente (solo letras): ")
                print(f"Paciente: {paciente}")
                if not paciente.isalpha():
                    print("Error: Ingrese un nombre válido.\n")
                    
            while not dia in range(1,3): #Validacion de dia
                dia = ""
                while not dia.isdigit():
                    dia = input("Ingrese el dia de la reserva (1=Lunes, 2=Martes)")
                    if not dia.isdigit():
                        print("Error: Ingrese un número válido.\n")   
                dia = int(dia)
                if not dia in range (1,3):
                    print("Error. Opcion fuera de rango.\n") 
            
            if dia == 1: #Verificacion de que el paciente no este registrado
                dia = ""
                print("Dia: Lunes\n")
                x = 0      
                for n in lunes.split():
                    if paciente == n:
                        print("El paciente ya se encuentra agendado para ese dia.\n")
                        x += 1
                    elif not paciente == n and x == 0 and "Libre" == n:
                        lunes = lunes.replace(n,paciente,1)
                        x += 1
                paciente = ""
            elif dia == 2:
                dia = ""
                print("Dia: Martes\n")
                x = 0  
                for n in martes.split():
                    if paciente == n:
                        print("El paciente ya se encuentra agendado para ese dia.\n")
                        x += 1
                    elif not paciente == n and x == 0 and "Libre" == n:
                        martes = martes.replace(n,paciente,1)
                        x += 1
                paciente = ""

        elif int(seleccion) == 2: #Cancelar turno (Opcion 2)

            while not dia in range(1,3): #Validacion de dia
                dia = ""
                while not dia.isdigit():
                    dia = input("Ingrese el dia de la reserva (1=Lunes, 2=Martes)")
                    if not dia.isdigit():
                        print("Error: Ingrese un número válido.\n")   
                dia = int(dia)
                if not dia in range (1,3):
                    print("Error. Opcion fuera de rango.\n")       

            while not paciente.isalpha(): #Validacion de nombre
                paciente = input("Ingrese el nombre del paciente (solo letras): ")
                print(f"Paciente: {paciente}")
                if not paciente.isalpha():
                    print("Error: Ingrese un nombre válido.\n")
            
            if dia == 1: #Verificacion de que el paciente este registrado
                print("Dia: Lunes\n")  
                dia = ""
                x = 0                 
                for n in lunes.split():
                    if paciente == n:
                        lunes = lunes.replace(paciente,"Libre")
                        x += 4
                    elif paciente != n and x == 3:
                        print("El paciente no se encuentra registrado para ese dia.\n")
                    else:
                        x += 1
                paciente = ""
            elif dia == 2:
                print("Dia: Martes\n")
                dia = ""
                x = 0   
                for n in martes.split():
                    if paciente == n:
                        martes = martes.replace(paciente,"Libre")
                        x += 3
                    elif paciente != n and x == 2:
                        print("El paciente no se encuentra registrado para ese dia.\n")
                    else:
                        x += 1   
                paciente = ""       

        elif int(seleccion) == 3: #Ver agenda del dia (Opcion 3)

            while not dia in range(1,3): #Validacion de dia
                dia = ""
                while not dia.isdigit():
                    dia = input("Ingrese el dia de la reserva (1=Lunes, 2=Martes)")
                    if not dia.isdigit():
                        print("Error: Ingrese un número válido.\n")   
                dia = int(dia)
                if not dia in range (1,3):
                    print("Error. Opcion fuera de rango.\n")         

            if dia == 1: #Mostrar los turnos del dia en orden
                print("Dia: Lunes\n")
                dia = ""
                a = 0
                for n in lunes.split():
                    a += 1
                    print(f"Turno {a} = {n}")
            elif dia == 2:
                print("Dia: Martes\n")
                dia = ""
                a = 0
                for n in martes.split():
                    a += 1
                    print(f"Turno {a} = {n}")

        elif int(seleccion) == 4: #Resumen general (Opcion 4)

            for t in lunes.split():
                if t != "Libre":
                    Ocupados_lunes += 1
            print("Dia: Lunes\n"
                  f"Turnos Ocupados: {Ocupados_lunes}\n"
                  f"Turnos disponibles: {4 - Ocupados_lunes}\n"
                  )

            for t in martes.split():
                if t != "Libre":
                    Ocupados_martes += 1
            print("Dia: Martes\n"
                  f"Turnos Ocupados: {Ocupados_martes}\n"
                  f"Turnos disponibles: {3 - Ocupados_martes}\n"
                  )
            
            if Ocupados_lunes > Ocupados_martes:
                print("Hay mas turnos ocupados el dia lunes que el dia martes.\n")
            elif Ocupados_martes > Ocupados_lunes:
                print("Hay mas turnos ocupados el dia martes que el dia lunes.\n")
            elif Ocupados_martes == Ocupados_lunes:
                print("La cantidad de turnos ocupados en lunes y martes es la misma.\n")
                                 
            Ocupados_lunes = 0
            Ocupados_martes = 0            

        elif int(seleccion) == 5: #Cerrar sistema (Opcion 5)
            seleccion = int(seleccion)
            pass

    elif seleccion.isdigit() and not int(seleccion) in range(1,6):
        print("Error: opción fuera de rango.\n")
    else:
        print("Error: ingrese un numero válido.\n")

#Ejercicio 4
energia = 100 #Variables
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
agente = ""
opcion = ""
numero = ""
forzar = 0

while not agente.isalpha(): #Validacion de nombre
    agente = input("Ingrese el nombre del agente (solo letras): ")
    print(f"Agente: {agente}")
    if not agente.isalpha():
        print("Error: Ingrese un nombre válido.")

while True: #Menu

    print(f"Energia = {energia}\n" #Estado
      f"Tiempo = {tiempo}\n"
      f"Cerraduras abiertas = {cerraduras_abiertas}\n")
    
    if cerraduras_abiertas < 3 and 0 < energia and 0 < tiempo:
        print("1. Forzar cerradura\n"
            "2. Hackear Panel\n"
            "3. Descansar\n"
            )
        while not opcion in range(1,4): #Validacion de opcion
            opcion = ""
            while not opcion.isdigit():
                opcion = input("Elija una opcion valida.\n")
                if not opcion.isdigit():
                        print("Error: Ingrese un número válido.\n")   
            opcion = int(opcion)
            if not opcion in range (1,4):
                print("Error. Opcion fuera de rango.\n")                   

        if opcion == 1: #Forzar Cerradura
            print("Forzar cerradura\n")
            energia -= 20
            tiempo -= 2
            forzar += 1
            opcion = ""
            if not alarma and energia < 40:
                print("Riesgo de alarma\n")

                while not numero in range(1,4): #Validacion de opcion
                    numero = ""
                    while not numero.isdigit():
                        numero = input("Seleccione un numero del 1 al 3.")
                        if not numero.isdigit():
                                print("Error: Ingrese un número válido.\n")
                    numero = int(numero)
                    if not numero in range (1,4):
                        print("Error. Opcion fuera de rango.\n")    

                if numero == 3: #Resultado de opcion seleccionada.
                    alarma = True
                    print("Alarma activada.\n")
                else:
                    print("Felicidades, no se activo la alarma.\n") 

            if not alarma and forzar < 3: #Resultado de forzar cerradura
                print("Felicidades. Usted ha abierto una cerradura.\n")
                cerraduras_abiertas += 1
            elif not alarma and forzar >= 3:
                print("Usted ha elegido Forzar cerradura 3 veces seguidas. La alarma se ha activado.\n")
                alarma = True
            elif alarma:
                print("La alarma esta activada. No se ha podido abrir la cerradura.\n")

        elif opcion == 2: #Hackear Panel (Opcion 2)
            print("Hackear Panel\n")
            energia -= 10
            tiempo -= 3
            forzar = 0
            opcion = ""
            for n in range(1,5):

                letra = ""
                while not letra.isalpha() or len(letra) != 1: #Prueba que solo se ingrese 1 letra
                    letra = input("Ingrese una letra: ")
                    if not letra.isalpha() or len(letra) != 1:
                        print("Error. Elija solo una letra.\n")

                codigo_parcial += letra #Agrega letra al codigo    

                if len(codigo_parcial) >= 8: #Evalua si el codigo cumple con la extension minima
                    print("Felicidades. Usted ha abierto una cerradura.\n")
                    cerraduras_abiertas += 1
                    codigo_parcial = ""
                else:
                    pass
        
        elif int(opcion) == 3: #Descansar (Opcion 3)
            print("Descansar\n")
            tiempo -= 1
            forzar = 0
            opcion = ""
            if energia <= 100:
                if not alarma and 85 <= energia:
                    energia += 15-(energia-85)
                elif not alarma and energia < 85:
                    energia += 15
                else:
                    energia -= 10
    
    if (cerraduras_abiertas == 3) or (alarma and tiempo <= 3) or (energia <= 0) or (tiempo <= 0): #Evaluacion de condiciones
        break

if cerraduras_abiertas == 3:
    print("La boveda ha sido abierta con exito.")
elif (alarma and tiempo <= 3) or (energia <= 0) or (tiempo <= 0):
    print("Sistema bloqueado. Usted ha perdido.")

#Ejercicio 5
gladiador = "" #Variables iniciales
opcion = ""
turno = 0
vida_gladiador = 100
vida_enemigo = 100
pociones = 3
daño_ataque_pesado = 15
daño_enemigo = 12
turno_gladiador = True

print("--- BIENVENIDO A LA ARENA ---") #Presentacion inicial

while not gladiador.isalpha(): #Nombre del gladiador
    gladiador = input("Ingrese su nombre (solo letras): ")
    print(f"Nombre del Gladiador: {gladiador}")
    if not gladiador.isalpha():
        print("Error: Solo se permiten letras.")

while 0 < vida_gladiador and 0 < vida_enemigo: #Ciclo de combate
    if turno == 0:
        print("=== INICIO DEL COMBATE ===")
        turno += 1
    else:
        print("=== NUEVO TURNO ===")
    print(f"{gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:\n"
          "1. Ataque Pesado\n"
          "2. Ráfaga Veloz\n"
          "3. Curar"
          )
    
    while not opcion in range(1,4): #Validacion de opciones
        opcion = ""
        while not opcion.isdigit():
            opcion = input("Elija una opcion: ")
            print(f"Opción: {opcion}")
            if not opcion.isdigit():
                print("Error: Ingrese un número válido.")
        opcion = int(opcion)
        if not opcion in range (1,4):
            print("Error. Opcion fuera de rango.")
        
    
    if int(opcion) == 1: #Ataque Pesado (Opcion 1)
        opcion = ""
        if 20 <= vida_enemigo:
            daño = daño_ataque_pesado
            vida_enemigo -= daño
        else:
            daño = daño_ataque_pesado*1.5
            vida_enemigo -= daño
        print(f"¡Atacaste al enemigo por {daño} puntos de daño!")

    elif int(opcion) == 2: #Ráfaga Veloz (Opcion 2)
        opcion = ""
        print(">> ¡Inicias una ráfaga de golpes!")
        for n in range(1,4):
            vida_enemigo -= 5
            print(">Golpe conectado por 5 de daño.")
    
    else: #Curar (Opcion 3)
        opcion = ""
        if pociones > 0:
            vida_gladiador += 30
            pociones -= 1
        else:
            print("¡No quedan pociones!")
    
    vida_gladiador -= daño_enemigo #Turno del enemigo
    print(">> ¡El enemigo te atacó por 12 puntos de daño!")

if vida_gladiador <= 0: #Evaluacion del resultado
    print("DERROTA. Has caído en combate.")
else:
    print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")