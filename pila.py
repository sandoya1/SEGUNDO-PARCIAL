#EJERCICIO EN CLASE 13/08/2021
#TEMA: PILAS Y COLAS
#ISAIAS RAFAEL SANDOYA VARGAS 

class Pila:
    def __init__(self,tamanio=1):
        self.lista=[]
        self.size=tamanio
        self.tope=0

    def push(self,dato):
        if self.top < self.size:
            self.lista = self.lista + [dato]
            self.top += 1
        else:
            print("La lista esta llena")

    def pop(self):
        if self.empty():
            return None
        else:
            top = self.lista[-1]
            self.lista = self.lista[:-1]
            self.top -= 1
            return top

    def show(self):
        for top in range(self.top-1,-1,-1):
                print("[{}]".format(self.lista[top]))

        def longuitud(self):
            return self.top

        def show(self):
            for top in range(self.top-1,-1,-1):
                print("[{}]".format(self.lista[top]))

    def empty(self):
        if self.top==0:
            return True
        else:
            return False

pila1 = Pila(3)
pila1.push(8)
pila1.push(10)
pila1.push(12)
pila1.push(4)
dato = pila1.pop()

pila1.show()
print(pila1.longuitud())

#if dato: print("El dato eliminado es; {}",format(dato))
#else: print("La lista esta vacia")
#if dato: print("El dato eliminado es; {}",format(dato))
#else: print("La lista esta vacia")
#if dato: print("El dato eliminado es; {}",format(dato))
#else: print("La lista esta vacia")
#if dato: print("El dato eliminado es; {}",format(dato))
#else: print("La lista esta vacia")

num = None
if num: print("Tiene valor")
