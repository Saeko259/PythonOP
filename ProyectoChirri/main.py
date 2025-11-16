from Funciones import * 
NumerosSacados= [[],[],[],[],[]]
nombres = []
NumP, FigG = InicioJuego()
nombres= NombresJugadores(NumP)
y = GenerarCartones(NumP)
for i in range(75):
    x = NumeroBalota(NumerosSacados)
    
print(NumerosSacados)
VerificacionTablero(y,NumerosSacados)
Visualizacion(y, nombres)
print (CondicionVictoria(FigG, y))


    
    
