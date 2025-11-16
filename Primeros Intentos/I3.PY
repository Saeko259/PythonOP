#Manejo de matrices
#En python, las matrices son listas dentro de listas
matrizE = [[1,2], [2,1]]
#El resto se trabaja igual, por ejemplo, si yo quiero acceder al elemento en la fila 1, columna 0
print("El elemento en la fila 1, columna 0 es: ", matrizE[1][0])
#Metodo para leer matrices
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
matriz =[]
for i in range(filas):
    fila = []
    for j in range(columnas):
        x = input(f"Ingrese el valor [{i+1}][{j+1}]: ")
        fila.append(x)
    matriz.append(fila)
    
    
#Como son listas dentro de listas, puedo imprimir la matriz solamente iterando el numero de filas, 
for i in range(filas):
    print(matriz[i])
    print("")