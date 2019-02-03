#!/usr/bin/env python
# coding: utf-8


#Crear una lista que contenga varios strings.
l1 = ["Javier","Programacion Redes Cisco", "Digitaliza", "Python"]

#Crear una lista que contenga varios strings.
l2 = [18,23,45,67,21,33]

#Crear una lista que contenga varios strings.
l3 = [25,"Alicante", "Curso Programación",17.7,"Edad",23.0,"Fecha",39]



#Crear las sentencias necesarias para imprimir, por pantalla, la información de las listas.

for i,n in enumerate(l1):
    print("Lista Strings - Posición[{}] = " + n.format(i))
    
for i,n in enumerate(l2):
    print("Lista Integers - Posición[{}] = {}".format(i,n))
    
for n in range(len(l3)):
    print("Lista Variada - Posición[{}] = {}".format(n,l3[n]))



#Crear 3 sentencias para asignar, en cada una, el último valor de una lista diferente a una variable

last_l1 = l1.pop()
l1.append(last_l1) #restituyo el elemento extraido de la lista
last_l2 = l2[-1]
last_l3 = l3[len(l3)-1]



#Crear una sentencia para imprimir, por pantalla, un texto, y concatenar la información de las variables.

print("Los últimos elementos de las listas son: l1({}) - l2({}) - l3({}) ".format(last_l1, last_l2, last_l3))



# Crear un diccionario de vuestras películas/obras favoritas (clave: autor, valor:película)

libros = {"Rubén Garrote":"Reversing","Ernesto Ariganello":"Guía CCNA Security","Eduardo Arriols":"Chief Information Security Officer","Pablo Gonzalez":"Pentesting con Kali"}



# Crear sentencia para imprimir por pantalla todo el diccionario.
for l in libros:
    print("{} : {} ".format(l,libros[l]))



# Crear sentencia para imprimir por pantalla sólo las claves del diccionario
for autor in libros:
    print("{}".format(autor))


# Crear sentencia para imprimir por pantalla sólo los valores del diccionario.
for autor in libros:
    print("{}".format(libros[autor]))


