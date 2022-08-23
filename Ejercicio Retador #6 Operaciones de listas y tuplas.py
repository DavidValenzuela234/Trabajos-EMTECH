#Ejercicio Retador 6 Operaciones de listas y tuplas

Sumatoria_Total_JAL = 0
Sumatoria_Total_BJX = 0
Sumatoria_Total_GDL = 0

Numero_Vuelos_JAL = 0
Numero_Vuelos_BJX = 0
Numero_Vuelos_GDL = 0

Destinos = ("BJX", "GDL", "JAL")
Pasajeros = []
Destino_Pasajero = []
Edad_Pasajero = []
Nombre = ""
Edad_Destino = []


Edades_Promedio_JAL = []
Edades_Promedio_BJX = []
Edades_Promedio_GDL = []



while Nombre != "X":
    Nombre = input("Ingresa tu nombre: ")
    
    if(Nombre != "X"):
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

        Pasajeros.append((Nombre, Edad, Destino))
        Edad_Destino.append((Destino, Edad))

        print("")


#Imprimir en Pantalla
print("")

print("--------------EDADES PROMEDIO POR DESTINO---------------------")
print("La edad promedio del vuelo JAL es: ",Edades_Promedio_JAL)
print("La edad promedio del vuelo GDL es: ",Edades_Promedio_GDL)
print("La edad promedio del vuelo BJX es: ",Edades_Promedio_BJX)

print("")

print("--------------NUMERO DE PERSONAS POR VUELOS---------------------")
print("La numero de personas en el vuelo JAL es: ",Numero_Vuelos_JAL)
print("La numero de personas en el vuelo GDL es: ",Numero_Vuelos_GDL)
print("La numero de personas en el vuelo BJX es: ",Numero_Vuelos_BJX)

print("")
print("Edades de los pasajeros: ", Edad_Pasajero)
print("Destinos de los pasajeros: ", Destino_Pasajero)
print("Datos de los pasajeros: ", Pasajeros)

print("Edades y destino de los pasajeros: ", Edad_Destino)

