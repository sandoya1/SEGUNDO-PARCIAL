class Cola:
    def __init__(self,tamaño):
        self.__lista=[]
        self.__tope=0
        self.size=tamaño

    def empty(self):
        return self.__tope==0

    def push(self,dato):
        if self.__tope < self.size:
            self.__lista= [dato]+self.__lista
            self.__tope+=1
        else: print("ERROR DE INGRESO: lista llena")
    
    def pop(self):
        if self.empty():
            return -1
        else:
            top= self.__lista[0]
            self.__tope-=1
            self.__lista= self.__lista[0]
            return top
    
    def show(self):
        for ele in range(0,self.__tope-1):
            print("[{}]".format(self.__lista[ele]))



pila = Cola(4)
pila.push(4)
pila.push(6)
print(pila.pop())
pila.show()
print(pila.pop())
pila.show()
print(pila.pop())
pila.show()
