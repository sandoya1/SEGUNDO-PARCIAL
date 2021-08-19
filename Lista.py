#EJERCICIO EN CLASE 16/08/2021
#TEMA: LISTA
#ISAIAS RAFAEL SANDOYA VARGAS 

class lista:
    def __init__(self,tamanio=3):
        self.lista = []
        self.longuitud = 0
        self.size = tamanio

    def append(self,dato):
        if self.longuitud < self.size:
            self.lista += [dato]
            self.longuitud += 1
        else:
            print("Lista esta llena")
    
    def obtenerEliminado(self,pos):
        self.mostrar()
        if pos < 0 or pos >= self.longuitud:
            return None
        else:
            eliminado = self.lista[pos]
            #self.lista = self.lista[:pos] + self.lista[pos+1:]
            listaAux = []
            for ind in range(pos):
                listaAux += [self.lista[ind]]
            for indice in range(pos+1,self.longuitud):
                listaAux += [self.lista[indice]]
            self.longuitud -=1
            self.lista = listaAux

            return [self.lista,eliminado]

    def mostrar(self):
        print("{:3}{:9} {}".format("","Lista","Posicion"))
        for pos,ele in enumerate(self.lista):
            print("[{:10}] {:4}".format(ele,pos))

lista1 = lista()
lista1.append("Daniel")
lista1.append(52)
lista1.append(True)
lista1.append("Milagro")
lista1.mostrar()
posicion = int(input("Ingrese el valor para obtener el valor del elemento: "))
resp = lista1.obtenerEliminado(posicion)
if resp == None:
    print("Posicion no valida, verifique la lista....!!! ")
else:
    print("El elemento de la posicion:{} es:{}".format(posicion, resp))
