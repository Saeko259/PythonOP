#Algoritmia 1
import random
x = int(input("Ingrese un numero entero:" ))
if ( x %2==0):
    print("El numero es par") 
else:
    print("El numero es impar")
#El for funciona de tal forma que es i < x, entonces si x=5, i toma los valores 1,2,3,4
for i in range(0, x):
    print(i)
    
c = 0
print("Empieza el while")
print(i)
#El while funciona con condiciones multiples separadas por parentesis
while (( x %2 == 0) & (i > 0) & (i <10)):
    print(c)
    c = c +1
    i = i +1
#Equivalente al switch-case 
match x:
    case 1:
        print("El numero es uno")
    case 2:
        print("El numero es dos")
    #Default
    case _:
        print("El numero no es ni uno ni dos")

#Generar un numero aleatorio entre 1 y 100
y = random.randint(1,100)
print("Resultado :", y)