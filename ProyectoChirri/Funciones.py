import random

#Funcion Para generar cartones individuales
def GenerarCarton():
    #En esta variable se guarda el carton como tal
    carton = []
    rangos = [ range(1,16), range (16,31), range(31,45), range (46,60), range (61,75) ]
    for idx in rangos:
        nums = random.sample(idx,5)
        columna = []
        for numero in nums:
            #Cada numero realmente es una lista de dos elementos, el primero siendo el numero, y el segundo siendo un 0 para luego poder cambiarlo 
            nmb = []
            nmb.append(numero)
            nmb.append(0)
            columna.append(nmb)
        carton.append(columna)
    return carton
    
def GenerarCartones(NumP):
    cartones = []
    for idx in range(NumP):
        cartones.append(GenerarCarton())
    return cartones

#Funcion de prueba para ver la logica en imprimir los cartones de manera individual
#Podria usarse para mostrarse el carton ganador (Posible)
def ImprimirCarton(CartonI):
    for idx in range(0, len(CartonI), 5):
        #Accedo a los numeros en bloques de 5 en 5                                                                                                                                 
        bloque = CartonI[idx: idx +5]
        for numero in bloque:
            print(f"{numero[0]:3d}", end="")
        print()
        
def VisualizacionSinNombres(PackCartones):
    print("             CARTONES GENERADOS")
      #Vamos de 4 en 4, con todos los cartones que hayan
    for idx in range(0, len(PackCartones), 4):
        #Vamos de 4 en 4 cartones
        CartonesActuales = PackCartones[idx: idx+4]
        
        for idj in range(idx,idx+len(CartonesActuales)):
            
            print(idj+1, end ="                    ")
        print()    
        #columna general
        for columna in range (5):
            if (columna == 0):
                    for idx in range (10 * len(CartonesActuales)):
                        print("__", end ="")
                    print()
            #Cada uno de los cartones de los que estamos trabajando actualmente
            for cartones in CartonesActuales:
                #Imprimimos las 5 columas de la fila en la que estemos
                for fila in range(5):
                    
                    if ( fila %5 == 0):
                        print("| ", end ="")
                    if (cartones[fila][columna][1] == 1):
                        print(f"\033[32m{cartones[fila][columna][0]:3d}\033[0m", end="")
                    else: 
                        print(f"{cartones[fila][columna][0]:3d}", end ="")
                #Espaciado entre matrices
                print(" | ", end ="")
            print ()
            if (columna == 4):
                    for j in range (10 * len(CartonesActuales)):
                        print("__", end ="")
                    
        print()      
        
def VisualizacionConNombres(PackCartones,NombresP):
    print("____________________________________________________________________________________________")
    print("             CARTONES ACTUALIZADOS")
    #Vamos de 4 en 4, con todos los cartones que hayan
    for idx in range(0, len(PackCartones), 4):
        #Vamos de 4 en 4 cartones
        CartonesActuales = PackCartones[idx: idx+4]
        #columna general
        for idj in range(idx,idx+len(CartonesActuales)):
            
            print(f"{NombresP[idj]}", end ="              ")
        print()    
        for columna in range (5):
            if (columna == 0):
                    for idx in range (10 * len(CartonesActuales)):
                        print("__", end ="")
                    print()
            #Cada uno de los cartones de los que estamos trabajando actualmente
            for cartones in CartonesActuales:
                #Imprimimos las 5 columas de la fila en la que estemos
                for fila in range(5):
                    
                    if ( fila %5 == 0):
                        print("| ", end ="")
                    if (cartones[fila][columna][1] == 1):
                        print(f"\033[32m{cartones[fila][columna][0]:3d}\033[0m", end="")
                    else: 
                        print(f"{cartones[fila][columna][0]:3d}", end ="")
                #Espaciado entre matrices
                print(" | ", end ="")
            print ()
            if (columna == 4):
                    for j in range (10 * len(CartonesActuales)):
                        print("__", end ="")
                    
        print()
        

def NombresJugadores(NumP):
    print("____________________________________________________________________________________________")
    print("Ahora ingrese los nombres de los jugadores!!")
    ListaNombres = []
    for idx in range(NumP):
        nombre = str(input(f"Ingrese el nombre del jugador #{idx+1}: "))
        if (len(nombre) > 15):
            nombre = nombre[0:15]
            ListaNombres.append(nombre)
        else:
            ListaNombres.append(nombre)
    return ListaNombres

#Esta funcion maneja la parte inicial del juego
def InicioJuego():
    NumP = -1
    FigG = -1
    print("BIENVENIDO AL PROGRAMA INTERACTIVO DE BINGO")
    print("Antes de comenzar el juego te pediremos que ingreses dos cosas:")
            
    try: 
        NumP = int(input("1. Ingrese el numero de jugadores: "))
    except ValueError:
        print(" Debe ingresar un numero entero")
    while ( NumP < 0 ):
        NumP= int(input("Ingresaste un valor erroneo, porfavor ingresa un numero de Jugadores Valido: "))
    print("2.Digita alguna de las siguientes opciones para escoger la figura ganadora:")
    print("     1. 'O': Primera y última fila, y primera y última columna.")
    print("     2. 'X': Las dos diagonales del cartón")
    print("     3. 'Cartón Completo': Todas las filas y columnas")
    try:
        FigG = int(input("Opcion deseada: "))
    except ValueError:
        print(" Debe ingresar un numero entero")
    while((FigG <0 )| (FigG >3)):
        FigG = int(input("Ingrese porfavor un valor valido:"))
    print("____________________________________________________________________________________________")
    return NumP,FigG

#Se encarga de sacar un numero aleatorio asegurandose de que no se repita
def NumeroBalota(NumerosSacados):
    NumeroActual = random.randint(1,75)
    #Debemos revisar de manera constante si el numero se repite, por esto haremos lo siguiente
    repetido = 1
    while (repetido == 1): 
        repetido = 0
        for letra in NumerosSacados:
            for idx in letra:
                if( idx == NumeroActual):
                    NumeroActual = random.randint(1,75)
                    #Vuelve a buscar si el nuevo numero no se obtuvo antes
                    repetido= 1
    if((NumeroActual >=1) and (NumeroActual<16) ):
        NumerosSacados[0].append(NumeroActual)
    elif((NumeroActual >=16) and (NumeroActual<31)):
        NumerosSacados[1].append(NumeroActual)
    elif((NumeroActual >=31) and (NumeroActual<46)):
        NumerosSacados[2].append(NumeroActual)
    elif((NumeroActual >=46) and (NumeroActual<61)):
        NumerosSacados[3].append(NumeroActual)
    elif((NumeroActual >=61) and (NumeroActual<76)):
        NumerosSacados[4].append(NumeroActual)
    #Organizamos el arreglo de los numeros obtenidos
    for letras in NumerosSacados:
        letras.sort()
    return NumeroActual    

#Verifica si en los cartones hay alguno de los numeros obtenidos
def VerificacionTablero(Cartones, NumerosSacados):
    for letras in NumerosSacados:
        for numero in letras:
            for carton in Cartones:
                for filas in range(5):
                    for columnas in range(5):
                        if (carton[filas][columnas][0] == numero):
                            carton[filas][columnas][1] = 1
                            
def CondicionVictoria(FigG,PaqueteCartones):
    ListaGanadores = []
    match FigG:
        case 1:
            for carton in PaqueteCartones:
                contador = 0   
                #Revisamos la primera fila
                for idx in range(5):
                    if (carton[idx][0][1] == 1):
                        contador += 1
                #Revisamos la ultima fila
                for idx in range(5):
                    if (carton[idx][4][1] == 1):
                        contador += 1
                #Revisamos los tres items faltantes de la primera columna
                for idx in range(1,4):
                    if (carton[0][idx][1] == 1):
                        contador += 1
                #Revisamos los tres items faltantes de la ultima columna
                for idx in range(1,4):
                    if (carton[4][idx][1] == 1):
                        contador += 1
                if ( contador == 16):
                    ListaGanadores.append(PaqueteCartones.index(carton))
        case 2:
            for carton in PaqueteCartones:
                contador = 0   
                #Revisamos la diagonal principal
                for idx in range(5):
                    if (carton[idx][idx][1] == 1):
                        contador += 1
                #Revisamos la diagonal inversa 
                for idx in range(5):
                    fila = 4 - idx
                    if (carton[idx][fila][1] == 1):
                        contador += 1
                if ( contador == 10):
                    ListaGanadores.append(PaqueteCartones.index(carton))
        case 3:
            for carton in PaqueteCartones:
                contador = 0   
                for filas in range(5):
                    for columnas in range(5):
                        if (carton[filas][columnas][1] == 1):
                            contador += 1
                if ( contador == 25):
                    ListaGanadores.append(PaqueteCartones.index(carton))
    return ListaGanadores

def BINGO(NumerosSacados):
    print("____________________________________________________________________________________________")
    for letra in NumerosSacados:
        c = 0
        for numeros in letra:
            if ((NumerosSacados.index(letra) == 0) and (c == 0) ):
                print("B: ", end ="")
                c= c+1
            elif ((NumerosSacados.index(letra) == 1) and (c == 0) ):
                print("I: ", end ="")
                c= c+1
            elif ((NumerosSacados.index(letra) == 2) and (c == 0) ):
                print("N: ", end ="")
                c= c+1
            elif ((NumerosSacados.index(letra) == 3) and (c == 0) ):
                print("G: ", end ="")
                c= c+1
            elif ((NumerosSacados.index(letra) == 4) and (c == 0) ):
                print("O: ", end ="")
                c= c+1
            print(f"{numeros:2d}", end = ", ")
        print()
    print("____________________________________________________________________________________________")
    return

def PantallaFin(ListaGanadores, ListaNombres,PaqueteCartones):
    for idx in ListaGanadores:
        print(f"El carton ganador fue el del jugador {ListaNombres[idx]} ")
        for columna in range (5):
            if (columna == 0):
                    for idj in range (10):
                        print("__", end ="")
                    print()
            #Cada uno de los cartones de los que estamos trabajando actualmente
            cartones = PaqueteCartones[idx]
            #Imprimimos las 5 columas de la fila en la que estemos
            for fila in range(5):  
                if ( fila %5 == 0):
                    print("| ", end ="")
                if (cartones[fila][columna][1] == 1):
                    print(f"\033[32m{cartones[fila][columna][0]:3d}\033[0m", end="")
                else: 
                    print(f"{cartones[fila][columna][0]:3d}", end ="")       
            print(" |", end= "")
            print()
        
        
        