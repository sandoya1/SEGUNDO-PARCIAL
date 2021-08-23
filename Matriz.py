#EJERCICIO EN CLASE 20/08/2021
#TEMA: MATRIZ
#ISAIAS RAFAEL SANDOYA VARGAS 

class Matriz:
    def __init__(self,matriz):
        self.matriz=matriz
    def ingresar(self,dato):
        pass
    def presentar (self):
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                # print(columna[col],end=" ")
                print(self.matriz[fila][col],end=" ")
            print()

# columnas   0  1  2    0  1  2    0  1  2
numeros=[[10,20,30],[60,80,90],[25,35,55]]
# filas
mat=Matriz(numeros)
mat.presentar()
# print(numeros[0],numeros[0][1])
