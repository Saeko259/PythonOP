from Funciones import * 
NumerosSacados= [[],[],[],[],[]]
#NumP= int(input("Ingrese el numero de jugadores: "))

NumP, FigG = InicioJuego()
nombres= NombresJugadores(NumP)
y = GenerarCartones(NumP)
for i in range(30):
    x = NumeroBalota(NumerosSacados)
    
print(NumerosSacados)
VerificacionTablero(y,NumerosSacados)
Visualizacion(y, nombres)


    
    
