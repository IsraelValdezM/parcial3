#Definimos la clase Nodo para las listas enlazadas
class Nodo:

    #metodo constructor
    def __init__(self,valor):
        self.dato=valor
        self.next=None
    #metodo para obtener el valor del dato o elemento
    def obtenerDato(self):
        return self.dato
    #Metodo para obtener la referencia, puntero o apuntador
    def obtenerSiguiente(self):
        return self.next
    #Metodo para asignar valor al nodo atraves de un dato o elemento
    def setDato(self,val):
        self.dato=val
    #Metodo para asignar un valor a la referencia siguiente
    def setSiguiente(self,valor):
        self.next=valor