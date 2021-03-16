import numpy as np
import re
import types
from functools import reduce

class MyMatrix():

    def __init__(self, matriz): 
        self.matriz = matriz
        self.dimension = self.get_dimension(0, self.matriz)
        self.straight = self.get_straight(np.array(self.matriz))
        self.compute = self.get_compute(self.matriz)
        
    #Creación de un nuevo método para obtener la dimensión de la matriz
    def get_dimension(self, ndim, m):
        if not isinstance(m, list):
            return ndim

        ndim += 1
        return self.get_dimension(ndim, m[0])

    #Devuelve true o false según el siguiente criterio: -True: Si el arreglo o matriz
    # contiene la misma cantidad de elementos en cada una de sus dimensiones (Matriz uniforme). 
    # -False: Caso contrario
        
    def get_straight(self, m):
        if self.dimension == 1:
            return True
        s =  m.shape
        if self.dimension == len(s):
            return True
        else:
            return False
         
    #Devuelve el número entero resultado de la suma de todos los números
    #incluídos en la matriz sin importar el tamaño o dimensión.
    def get_compute(self, m):
        try:
            f = reduce(lambda x,y: x+y, m)
        
            if f != m:
                return self.get_compute(f)
            
            return m
        except:
            return m

class MyArray:
    
    def __init__(self, cadena):
        self.cadena = cadena.replace(" ", "")
        self.compute = self.get_compute()
        self.operation = self.get_operation()

    def get_operation(self):
        pattern = re.compile("(?:[0-9 ()]+[*+/-])+[0-9 ()]+")
        if pattern.search(self.cadena) != None and self.cadena.count('(') == self.cadena.count(')') and self.compute:
            return True    
        return False

    
    def get_compute (self):
        try:
            return eval(self.cadena)
        except:
            return False

a = [1,2]
b = [[1,2],[2,4]] 
c = [[1,2],[2,4],[2,4]] 
d = [[[3,4],[6,5]]] 
e = [[[1, 2, 3]], [[5, 6, 7],[5, 4, 3]], [[3, 5, 6], [4, 8, 3], [2, 3]]]
f = [[[1, 2, 3], [2, 3, 4]], [[5, 6, 7], [5, 4, 3]], [[3, 5, 6], [4, 8, 3]]]
#Llamamos al método
print("Dimensión(a) = " + str(MyMatrix(a).dimension))
print("Dimensión(b) = " + str(MyMatrix(b).dimension))
print("Dimensión(c) = " + str(MyMatrix(c).dimension))
print("Dimensión(d) = " + str(MyMatrix(d).dimension))
print("Dimensión(e) = " + str(MyMatrix(e).dimension))
print("Dimensión(f) = " + str(MyMatrix(f).dimension))

#o.straight(f)
print("Straight(a) = " + str(MyMatrix(a).straight))
print("Straight(b) = " + str(MyMatrix(b).straight))
print("Straight(c) = " + str(MyMatrix(c).straight))
print("Straight(d) = " + str(MyMatrix(d).straight))
print("Straight(e) = " + str(MyMatrix(e).straight))
print("Straight(f) = " + str(MyMatrix(f).straight))

#o.compute(f)
print("Suma(a) = " + str(MyMatrix(a).compute))
print("Suma(b) = " + str(MyMatrix(b).compute))
print("Suma(c) = " + str(MyMatrix(c).compute))
print("Suma(d) = " + str(MyMatrix(d).compute))
print("Suma(e) = " + str(MyMatrix(e).compute))
print("Suma(f) = " + str(MyMatrix(f).compute))

Operacion1 = "Hello world" 
Operacion2 = "2 + 10 / 2 - 20" 
Operacion3 = "(2 + 10) / 2 - 20" 
Operacion4 = "(2 + 10 / 2 - 20"

print("Operación(a) = " + str(MyArray(Operacion1).operation))
print("Operación(b) = " + str(MyArray(Operacion2).operation))
print("Operación(c) = " + str(MyArray(Operacion3).operation))
print("Operación(d) = " + str(MyArray(Operacion4).operation))

#o.straight(f)
print("Resultado(a) = " + str(MyArray(Operacion1).compute))
print("Resultado(b) = " + str(MyArray(Operacion2).compute))
print("Resultado(c) = " + str(MyArray(Operacion3).compute))
print("Resultado(d) = " + str(MyArray(Operacion4).compute))
