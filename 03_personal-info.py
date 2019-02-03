#!/usr/bin/env python
# coding: utf-8



# Crear un script que pregunte por el nombre, el apellido, el teléfono, la ciudad, y la edad. Cada valor ha de ser guardado en una variable diferente.

nombre = ""
apellido = ""
telefono = ""
ciudad = ""
edad = ""

while(nombre == ""):
    nombre = input("Introduzca su nombre:  ")

while(apellido == ""):
    apellido = input("Introduzca su apellido:  ")

while(telefono == ""):
    telefono = input("Introduzca su número de teléfono:  ")

while(ciudad == ""):
    ciudad = input("Introduzca su ciudad:  ")

while(edad == ""):
    edad = int(input("Introduzca su edad:  "))



# Imprimir, por pantalla, toda la infomarción coleccionada en una frase que combine la información 
#con coherencia (una oración que no sólo sean los datos recogidos).

centros = ["Madrid", "Barcelona", "Valencia", "Alicante", "A Coruña"]
centrodisponible = "no"
edadok = "no"

if (ciudad in centros):
    centrodisponible = "sí"

if ( edad > 20 and edad < 50):
    edadok = "si"
    

respuesta =  """Hola {}{}. Gracias por interesarse en nuestra formación. Actualmente {} disponemos de
            centro formativo en {}. Su edad ({} años) {} se beneficia de una beca del 40% de descuento.
            Uno de nuestros agentes se pondrá en contacto con Vd. en el número de teléfono facilitado, 
            {}. """.format(nombre, apellido,centrodisponible,ciudad,edad,edadok,telefono)

print(respuesta)






