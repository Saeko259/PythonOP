import random

#Funcion Para generar cartones individuales
def GenerarCarton():
    #En esta variable se guarda el carton como tal
    carton = []
    rangos = [ range(1,16), range (16,31), range(31,45), range (46,60), range (61,75) ]
    for idx in rangos:
        nums = random.sample(idx,5)
        fila = []
        for numero in nums:
            #Cada numero realmente es una lista de dos elementos, el primero siendo el numero, y el segundo siendo un 0 para luego poder cambiarlo 
            nmb = []
            nmb.append(numero)
            nmb.append(0)
            fila.append(nmb)
        carton.append(fila)
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
        
def ImprimirCartones(PackCartones,NombresP):
    #Vamos de 4 en 4, con todos los cartones que hayan
    for idx in range(0, len(PackCartones), 4):
        #Vamos de 4 en 4 cartones
        CartonesActuales = PackCartones[idx: idx+4]
        #Fila general
        for fila in range (5):
            if ((fila == 0) & (idx == 0)):
                for i in range(35):
                    print("__", end= "")
                print()
            #Cada uno de los cartones de los que estamos trabajando actualmente
            for cartones in CartonesActuales:
                if ( CartonesActuales.index(cartones) %4 == 0):
                    print("| ", end ="")
                #Imprimimos las 5 columas de la fila en la que estemos
                for columna in range(5):
                    print(f"{cartones[fila][columna][0]:3d}", end ="")
                #Espaciado entre matrices
                print("  ", end ="")
            print ("|")
        print("|")
        

        