from Funciones import * 

y = GenerarCartones(5)   

# Recorremos en bloques de 4 cartones
for recorrido in range(0, len(y),4 ):
    
    bloque = y[recorrido : recorrido + 4]  # toma máximo 4 cartones
    
    # Imprimir filas (5 filas por cartón)
    for i in range(5):
        for k in bloque:  # cada cartón dentro del bloque
            for j in range(5):
                print(f"{k[i][j]:2d}", end=" ")
            print("   ", end="")  # espacio entre cartones
        print()  # salto de línea entre cada fila del bloque
    
    print()  # espacio entre bloques

    
    
