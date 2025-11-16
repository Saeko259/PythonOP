#Asi se trabajan las funciones en python, def (para definir la funcion), el nombre de la funcion, y los parametros
def PrimeraFuncion():
    print("Esta es mi primera funcion")
    return
#Return siempre necesario
#Asi se invocan las funciones
PrimeraFuncion()
#Puedo tener una funcion que retorna varios valores, para esto, debo dividirlos con comas y ya
def Sumar(a,b):
    print(a+b)
    a= 2
    b = 4
    return a,b

a, b =Sumar(2,4)

print(a)
print(b)
#Los valores del parametro no se modifican de ninguna forma en el algoritmo principal a menos que yo lo asigne
def SumarB(a,b):
    a = 2
    b = 4
    print(a + b)
    return a,b
x = 0
y = 0 

print(x)
print(y)