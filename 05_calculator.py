#!/usr/bin/env python
# coding: utf-8



# Crear las sentencias necesarias para recoger dos números a través del terminal
numero1 = float(input("Introduzca el primer número: "))
numero2 = float(input("Introduzca el segundo número: "))



# Integrar funcionalidades de suma, multiplicación, división, y exponencial
def calculator(opcion=0):
    result = -9E30
    if(opcion == 1 ):
        result = numero1 + numero2
    elif(opcion == 2):
        result = numero1 * numero2
    elif(opcion == 3):
        result = numero1 / numero2
    elif(opcion == 4):
        result = numero1 ** numero2
    else:
        print("La opción ({}) introducida no se encuentra soportada".format(opcion))
    return result




# Permitir escoger el modo de operación de forma manual 
#(el usuario ha de introducir un número para que sepa qué operación realizar)
opcion = int(input("""Introduzca el número correspondiente a la operación a realizar: \n
                    Suma -------------> 1
                    multiplicación ---> 2
                    división ---------> 3
                    exponencial ------> 4 \n\n"""))




# Realizar las operaciones e imprimir el valor por pantalla.
result = calculator(opcion)
if(result != -9E30):
    print(result)
else:
    print("La operación no se ha realizado correctamente")





