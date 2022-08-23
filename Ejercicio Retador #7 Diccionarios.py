#Ejercicio Retador 7 Diccionarios


Edad_Pasajero = []
Destinos = ("BJX", "GDL", "JAL")
Pasajeros = []
Datos_Pasajeros = {}
Id_Nombre = {}
Destino_Pasajero = []
Nombre = ""
Nombre_Cliente = []
Edad_Destino = []
Opcion = 5
Id_Cliente = []
Id = 0
Cliente_Preferente = []
Es_Preferente = []
Preferentes = ""
Lista_Preferentes = []

Sumatoria_Total_JAL = 0
Sumatoria_Total_BJX = 0
Sumatoria_Total_GDL = 0

Numero_Vuelos_JAL = 0
Numero_Vuelos_BJX = 0
Numero_Vuelos_GDL = 0

Edades_Promedio_JAL = []
Edades_Promedio_BJX = []
Edades_Promedio_GDL = []


while Opcion > 4:
    print("------------------------ MENU ----------------------------")
    print("")

    print("1.- Añadir Clientes")
    print("2.- Lista de Todos Los Clientes")
    print("3.- Listar Clientes Preferentes")
    print("4.- Salir")

    print("")

    Opcion = int(input("Elige la opcion deseada: "))
    print("")
   
    if Opcion == 1:

        while Nombre != "X":

            print("------------------------ AGREGAR CLIENTES ----------------------------")
            print("")

            Nombre = input("Ingresa tu nombre: ")
            
            if Nombre != "X":
                Id = input("Ingresa tu ID de tu INE: ")

                Edad = int(input("Ingresa tu edad: "))
                Edad_Pasajero.append(Edad)
                

                Destino = input("Ingresa el codigo IATA de tu destino: ")
                if Destino == "JAL":
                    Numero_Vuelos_JAL += 1
                    Sumatoria_Total_JAL += Edad
                    Edades_Promedio_JAL = Sumatoria_Total_JAL/Numero_Vuelos_JAL
                
                elif Destino == "BJX":
                    Numero_Vuelos_BJX += 1
                    Sumatoria_Total_BJX += Edad
                    Edades_Promedio_BJX = Sumatoria_Total_BJX/Numero_Vuelos_BJX
                    
                elif Destino == "GDL":
                    Numero_Vuelos_GDL += 1
                    Sumatoria_Total_GDL += Edad
                    Edades_Promedio_GDL = Sumatoria_Total_GDL/Numero_Vuelos_GDL
                    

                
                else:
                    print("")
                    print("Escriba el destino correcto")
                    Numero_Vuelos_GDL = "0"
                    Sumatoria_Total_GDL = "0"
                    Numero_Vuelos_JAL = "0" 
                    Sumatoria_Total_JAL = "0"
                    Numero_Vuelos_BJX = "0" 
                    Sumatoria_Total_BJX = "0"

                Destino_Pasajero.append((Destino))

                

                Edad_Destino.append((Destino, Edad))

                Preferentes = input ("Cliente preferente?: Escribe True o False: ")
                if Preferentes == "True":
                    Cliente_Preferente.append(Preferentes)

                elif Preferentes == "False":
                    Cliente_Preferente.append(Preferentes)

                    for Cliente in Cliente_Preferente:
                        if Cliente == "True":
                            Es_Preferente.append(Cliente)
                
                Pasajeros.append((Id, Nombre, Edad, Destino, Preferentes))
                Datos_Pasajeros[Id] = Nombre, Edad, Destino, Preferentes
                Id_Nombre[Id] = Nombre

                
                Opcion = 5

                print("")

    elif Opcion == 2:
        print("------------------------ LISTA DE TODOS LOS CLIENTES CON SU ID Y NOMBRE----------------------------")
        print("")
        print(Id_Nombre)
        print("")

    elif Opcion == 3:
        print("------------------------ LISTA DE CLIENTES PREFERENTES----------------------------")
        print("")

        for Buscar in Pasajeros:
            if Buscar[4] == "True":
                Lista_Preferentes.append(Buscar)
        
        for Buscar in Lista_Preferentes:
            print("ID: ",Buscar[0], "Nombre del Cliente",Buscar[1])

        print("")


        print("Clientes Preferentes: ", Es_Preferente )

    elif Opcion == 4:
        exit()
        



print("Prefencia de todos los clientes: ", Cliente_Preferente)

print("Datos de los pasajeros: ", Pasajeros)
print("Datos de los pasajeros: ", Datos_Pasajeros)