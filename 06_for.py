#!/usr/bin/env python
# coding: utf-8



# Crear una lista con nombres de persona e incluir, como mínimo, 5 nombres 
#(como mínimo, uno ha de tener la vocal "a")
nombres = ["Luis", "Roberto","Anabel","Diana","Joaquín"]



#Crear una lista llamada "selected"
selected = []



#Recorrer, mediante un for, la lista de los nombres e imprimir un texto
#con el nombre recorrido en dicha iterración. Asimismo, si el nombre de esa iteración 
#contine una "a", añadirlo a la lista llamada "selected"
for n in nombres:
    print(n)
    if('a' in n):
        selected.append(n)



# Finalmente, imprimir por pantalla la lista "selected"
print(selected)






