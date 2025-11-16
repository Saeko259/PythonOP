#Manejo de listas
lista = [1,2,3,4,5]

print("El primer elemento de la lista es: ",lista[0])
#Agrega un elemento al final de la lista
lista.append("elemento")
lista.insert(2,"Elemento intruso")

#Cuenta los elementos de la lista
for i in range(0, len(lista)):
    print(i)
    
#Recorrer una lista con for
for i in lista:
    print(i)
    
#Eliminar el elemento especifico de la lista
lista.remove("elemento")
#Remueve el ultimo elemento y lo retorna
lista.pop()
#Remueve el elemento en esa posicion de la lista
lista.pop(2)

#Cantidad de elementos de la lista
len(lista)  
