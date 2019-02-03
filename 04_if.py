#!/usr/bin/env python
# coding: utf-8


# Crear un script en el que guardéis en una variable un número
numero = int(input("Introduzca un número: "))


# Controlar el tamaño del número en 4 rangos (menor de 20, entre 20 y 39, entre 40 y 59, mayor de 60)
# En cada uno de los casos imprimir por pantalla el número que se haya introducido.

if (numero < 20 ):
    print( "El número introducido {} es menor de 20 ".format(numero))
elif (numero >= 20 and numero <= 39):
    print( "El número introducido ({}) se encuentra en el rango (20-39) ".format(numero))
elif (numero >= 40 and numero <= 59):
    print( "El número introducido ({}) se encuentra en el rango (40-59) ".format(numero))
else:
     print( "El número introducido ({}) es mayor o igual a 60 ".format(numero))
    
    



