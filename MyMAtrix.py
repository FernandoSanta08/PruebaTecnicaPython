import numpy as np
import re
import types
from functools import reduce

class MyMatrix():

    #Constructor o inicializador de la clase Matriz

    def __init__(self, matriz): 
        self.matriz = matriz
        self.dimension = self.get_dimension(0, self.matriz)
        self.straight = self.get_straight(np.array(self.matriz))
        self.compute = self.get_compute(self.matriz)
        
    # Función recursiva que itera sobre la matriz y aumenta la dimensión por iteración.

    def get_dimension(self, ndim, m):
        if not isinstance(m, list):
            return ndim

        ndim += 1
        return self.get_dimension(ndim, m[0])

    # Función que valida aprovechando la dimensión y la función "Shape" de np
    # para facilitar la validación de una matriz uniforme
        
    def get_straight(self, m):
        if self.dimension == 1:
            return True
        s =  m.shape
        if self.dimension == len(s):
            return True
        else:
            return False
         
    # Función recursiva que reduce la matriz a un arreglo básico y suma sus valores.

    def get_compute(self, m):
        try:
            f = reduce(lambda x,y: x+y, m)
        
            if f != m:
                return self.get_compute(f)
            
            return m
        except:
            return m

class MyArray:
    
    #Constructor o inicializador del arreglo.

    def __init__(self, cadena):
        self.cadena = cadena.replace(" ", "")
        self.compute = self.get_compute()
        self.operation = self.get_operation()

    #Función que valida si la cadena o string recibido esta bien construido.

    def get_operation(self):
        pattern = re.compile("(?:[0-9 ()]+[*+/-])+[0-9 ()]+")
        if pattern.search(self.cadena) != None and self.cadena.count('(') == self.cadena.count(')') and self.compute:
            return True    
        return False

    #Función que ejecuta la operación en la cadena.
    
    def get_compute (self):
        try:
            return eval(self.cadena)
        except:
            return False

#Matrices de entrada. 

a = [1,2]
b = [[1,2],[2,4]] 
c = [[1,2],[2,4],[2,4]] 
d = [[[3,4],[6,5]]] 
e = [[[1, 2, 3]], [[5, 6, 7],[5, 4, 3]], [[3, 5, 6], [4, 8, 3], [2, 3]]]
f = [[[1, 2, 3], [2, 3, 4]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3]]]

#Llamamos al calculo de dimensión de la matriz.

print("Dimensión(a) = " + str(MyMatrix(a).dimension))
print("Dimensión(b) = " + str(MyMatrix(b).dimension))
print("Dimensión(c) = " + str(MyMatrix(c).dimension))
print("Dimensión(d) = " + str(MyMatrix(d).dimension))
print("Dimensión(e) = " + str(MyMatrix(e).dimension))
print("Dimensión(f) = " + str(MyMatrix(f).dimension))

# Llamado a la validación de matriz uniforme 

print("Straight(a) = " + str(MyMatrix(a).straight))
print("Straight(b) = " + str(MyMatrix(b).straight))
print("Straight(c) = " + str(MyMatrix(c).straight))
print("Straight(d) = " + str(MyMatrix(d).straight))
print("Straight(e) = " + str(MyMatrix(e).straight))
print("Straight(f) = " + str(MyMatrix(f).straight))

# Llamado a la suma de los valores de la matriz.
print("Suma(a) = " + str(MyMatrix(a).compute))
print("Suma(b) = " + str(MyMatrix(b).compute))
print("Suma(c) = " + str(MyMatrix(c).compute))
print("Suma(d) = " + str(MyMatrix(d).compute))
print("Suma(e) = " + str(MyMatrix(e).compute))
print("Suma(f) = " + str(MyMatrix(f).compute))

#Cadenas de entrada parte 2.
Operacion1 = "Hello world" 
Operacion2 = "2 + 10 / 2 - 20" 
Operacion3 = "(2 + 10) / 2 - 20" 
Operacion4 = "(2 + 10 / 2 - 20"

#lllamado a validación de operación
print("Operación(a) = " + str(MyArray(Operacion1).operation))
print("Operación(b) = " + str(MyArray(Operacion2).operation))
print("Operación(c) = " + str(MyArray(Operacion3).operation))
print("Operación(d) = " + str(MyArray(Operacion4).operation))

#llamado a la ejecución de la operación
print("Resultado(a) = " + str(MyArray(Operacion1).compute))
print("Resultado(b) = " + str(MyArray(Operacion2).compute))
print("Resultado(c) = " + str(MyArray(Operacion3).compute))
print("Resultado(d) = " + str(MyArray(Operacion4).compute))
