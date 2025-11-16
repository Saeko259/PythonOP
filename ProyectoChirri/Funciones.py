import random

#Funcion Para generar cartones individuales
def GenerarCarton():
    #En esta variable se guarda el carton como tal
    carton = []
    rangos = [ range(1,16), range (16,31), range(31,45), range (46,60), range (61,75) ]
    for idx in rangos:
        nums = random.sample(idx,5)
        carton.append(nums)
    return carton
    
def GenerarCartones(NumP):
    cartones = []
    for idx in range(NumP):
        cartones.append(GenerarCarton())
    return cartones
    