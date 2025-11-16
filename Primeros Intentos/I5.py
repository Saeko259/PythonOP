#Pruebas con lista para aplicaciones en el bingo
Lista = [0,1,2,3,4]
#Accede a los elementos desde inicio, hasta stop -1 
x = Lista[1:3]

print(x)

Matriz1 = [[[1,0],[2,0],[3,0]], [ [4,0],[5,0],[6,0]], [[7,0],[8,0],[9,0]]]
Matriz2 = [[[1,0],[2,0],[3,0]], [ [4,0],[5,0],[6,0]], [[7,0],[8,0],[9,0]]]
Matriz3 = [[[1,0],[2,0],[3,0]], [ [4,0],[5,0],[6,0]], [[7,0],[8,0],[9,0]]]
Matriz4 = [[[1,0],[2,0],[3,0]], [ [4,0],[5,0],[6,0]], [[7,0],[8,0],[9,0]]]
Matriz5 = [[[1,0],[2,0],[3,0]], [ [4,0],[5,0],[6,0]], [[7,0],[8,0],[9,0]]]
Matriz6 = [[[1,0],[2,0],[3,0]], [ [4,0],[5,0],[6,0]], [[7,0],[8,0],[9,0]]]
ConjuntoMatrices = [ Matriz1, Matriz2, Matriz3, Matriz4, Matriz5, Matriz6]
#Metodo para imprimir las matrices una al lado de la otra
#Vamos avanzando de 4 en 4 en las  matrices
for idx in range(0, len(ConjuntoMatrices), 4):
    #Queremos ir de a 4 matrices, por esto, vamos aprovechando las iteraciones
    bloque = ConjuntoMatrices[idx: idx+4]
    #Las matrices son 3x3, por esto, vamos a imprimir cada fila
    for fila in range(3):
        #Accedemos a cada matriz individualmente
        for matriz in bloque:
            #Ahora vamos imprimiendo cada columna de esa fila de cada matriz
            for columna in range(3):
                #
                print(f"{matriz[fila][columna][0]:2d}", end ="")
            #Este espacio es la separacion entre el final y el inicio de cada matriz
            print("     ", end ="")
        print( )
    print( )