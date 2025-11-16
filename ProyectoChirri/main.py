from Funciones import * 
NumerosSacados= [[],[],[],[],[]]
NumP, FigG = InicioJuego()
PaqueteCartones = GenerarCartones(NumP)
VisualizacionSinNombres(PaqueteCartones)
nombres= NombresJugadores(NumP)
VisualizacionConNombres(PaqueteCartones,nombres)
ListaGanadores = []
while(len(ListaGanadores)== 0):
    try:
        if (input("Dale enter para Sacar una balota: ")  == ""):
            nact = NumeroBalota(NumerosSacados)
            print(f"El numero obtenido fue {nact}")
            VerificacionTablero(PaqueteCartones, NumerosSacados)
            BINGO(NumerosSacados)
            ListaGanadores = CondicionVictoria(FigG, PaqueteCartones)
            print("Ahora se visualizara el tablero actualizado: ")
            VisualizacionConNombres(PaqueteCartones,nombres)
    except ValueError:
        print("Valor Erroneo")

PantallaFin(ListaGanadores, nombres, PaqueteCartones)

    
    
