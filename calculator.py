#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

import sys

class Calculator():
    """ Esta lista sirve para almacenar las operaciones que desee el usuario. """
    operaciones = []


    def __init__(self):
        self.__menu()


# Integrar funcionalidades de suma, multiplicación, división, y exponencial
    """ Se hace uso de la variable 'operacion' para almacenar el tipo de operación
        realizada y que se usará en el caso de querer el usuario almacenar los resultados"""
    def __calculator(self,opcion=0):
        result = -9E30
        if(opcion == 1 ):
            result = self.numero1 + self.numero2
            self.operacion = "SUMA"
        elif(opcion == 2):
            result = self.numero1 * self.numero2
            self.operacion = "MULTIPLICACIÓN"
        elif(opcion == 3):
            result = self.numero1 / self.numero2
            self.operacion = "DIVISIÓN"
        elif(opcion == 4):
            result = self.numero1 ** self.numero2 
            self.operacion = "POTENCIA"
        return result


# Permitir escoger el modo de operación de forma manual 
#(el usuario ha de introducir un número para que sepa qué operación realizar)
    def __menu(self):
        opcion_isok = False
        print("{:^150}".format("""  \n
                                    Suma ----------------------> 1 \n
                                    Multiplicación ------------> 2 \n
                                    División ------------------> 3 \n
                                    Exponencial ---------------> 4 \n
                                    Salir ---------------------> 5 \n
                                    Operaciones Almacenadas ---> 6 \n\n
                            """))

        while(opcion_isok is False):
            try:  
                opcion = int(input("""Introduzca el número correspondiente a la operación a realizar: \n """))
                if(opcion in range(1,7)):
                    opcion_isok = True
                    self.__setOperation(opcion)
                else:
                     print("La opción ({}) introducida no se encuentra soportada".format(opcion))
            except ValueError as e:
                print("\n Error !!! -El valor introducido es incorrecto. Inserte un número")
                self.__menu()


    def __setOperation(self,opcion):
        try:
            if(opcion == 5):
                print(" HASTA PRONTO. GRACIAS POR USAR CALCULATOR \n")
                sys.exit()
            elif(opcion == 6):
                self.__imprimirOperaciones()
                self.__menu()
                
            # Crear las sentencias necesarias para recoger dos números a través del terminal
            self.numero1 = float(input("Introduzca el primer número: "))
            self.numero2 = float(input("Introduzca el segundo número: "))
            # Realizar las operaciones e imprimir el valor por pantalla.
            result = self.__calculator(opcion)
            print("\n Resultado es:  {} \n".format(result))
            print("La operación se ha realizado correctamente\n")
            
            almacenar = input("¿Desea guardar la operación realizada?\n")
            if(almacenar.upper() == "SI"):
                nombre = input("Introduzca un nombre para salver los resultados: ")
                self.__guardarOperacion(nombre,result)
            self.__menu()
        except ValueError as e:
            print("\n Error !!! -El valor introducido es incorrecto. Inserte un número")
            self.__menu()
        except ZeroDivisionError as e:
            print("\n Error !!! - No puede dividir por 0")
            self.__menu()
        except Exception as e:
            print("La operación no se ha realizado correctamente")
            self.__menu()
    
    """ Esta función sirve para almacenar en un diccionario la operación realizada y poder ser consultada por
        el usuario si lo desea. """
    def __guardarOperacion(self,nombre,resultado):     
        op = {"nombre":nombre, "operacion":self.operacion, "numero1":self.numero1, "numero2":self.numero2, "resultado":resultado}
        (self.operaciones).append(op)
       
    """ Función destinada a imprimir las operaciones que han sido almacenadas por el usuario """
    def __imprimirOperaciones(self):
        for operacion in self.operaciones:
                print(operacion)
           
        
        
        

            

            
if __name__ == "__main__":
    calculator = Calculator()
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[4]:


Calculator()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


Calculator()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




