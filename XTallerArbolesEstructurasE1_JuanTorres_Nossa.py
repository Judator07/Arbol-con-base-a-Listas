####################################################################
#   Programa en Python para crear árboles haciendo uso de listas   #
#   Enlazadas. Los nodos son ingresados por teclado y posee        #
#   Metodos para obtener el peso del arbol, su orden y altura.     #
#                                                                  #
#                 Por: Juan Daniel Torres - 2240082                #
#                        Sebastian Nossa Agudelo                   #
#          Estructuras de datos y Análisis de algoritmos - E1      #
#                               2025-1                             #
####################################################################

#Clase Nodo
class Nodo:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = []

#Funcion recursiva para borrar todo desde adentro hacia afuera
def limpiar(obj):
    if isinstance(obj, list):
        for elem in obj:
            limpiar(elem)
        obj.clear()
        return

    if hasattr(obj, '__dict__'):
        for nombre, valor in list(obj.__dict__.items()):
            if nombre == 'prev':
                setattr(obj, 'prev', None)

            elif nombre == 'next' and isinstance(valor, list):
                limpiar(valor)

            else:
                if isinstance(valor, list) or hasattr(valor, '__dict__'):
                    limpiar(valor)

        obj.__dict__.clear()
        return

    return

#Clase Lista Doblemente Enlazada que se usará para árboles
class ListaDE:
    def __init__(self):
        self.head = None

    #Crear nodos en ListaDE
    def agregarLDE(self, prevnode, node):
        if prevnode == None or node == None:
            print("No se puede agregar nada porque no hay nodo anterior o se esta intentando insertar algo vacio")
        elif self.head == None:
            self.head = prevnode
            node.prev = prevnode
            prevnode.next.append(node)
        else:
            node.prev = prevnode
            prevnode.next.append(node)

    #Eliminar nodos en ListaDE
    def eliminarLDE(self, node):
        if node == None:
            print("No se puede borrar nada porque no hay nada")
        elif not node.next and not node.prev:
            self.head = None
            node = None
        elif not node.next:
            node.prev.next.remove(node)
            node = None
        elif node.prev == None:
            limpiar(node)
            self.head = None  
            node = None
        else:
            node.prev.next.remove(node)
            limpiar(node)
            node = None
    
    def getRoot(self):
        return self.head

    #Metodo recorrer arbol para obtener pesos
    def pesoRecorrido(self):
        self.contadorPeso = 0  
        self.soportePesoRecorrido(self.getRoot())  
        return self.contadorPeso  

    #Metodo recursivo que recorre los nodos del arbol
    def soportePesoRecorrido(self, nodo):
        if nodo is None:
            return  
        self.contadorPeso += 1  
        for hijo in nodo.next:  
            self.soportePesoRecorrido(hijo)

    #Obtener el orden del arbol
    def getOrder(self):
        x = self.soporteUnoOrdenRecorrido()
        x.sort()
        return x[-1]
    
    #Metodo recorrer arbol para obtener una lista del # de hijos de cada nodo
    def soporteUnoOrdenRecorrido(self): 
        self.contadorAux = [] 
        self.soporteDosOrdenRecorrido(self.getRoot())  
        return self.contadorAux

    #Metodo recursivo que recorre los nodos del arbol
    def soporteDosOrdenRecorrido(self, nodo):
        if nodo is None:
            return 
    
        num_hijos = len(nodo.next)
    
        self.contadorAux.append(num_hijos)
    
        for hijo in nodo.next:
            self.soporteDosOrdenRecorrido(hijo)

    #Obtener la altura del arbol
    def getHeight(self):
        return self.soporteAltura(self.getRoot())

    #Metodo recursivo que recorre los nodos del arbol
    def soporteAltura(self, nodo):
        if nodo is None:
            return 0
        elif not nodo.next:
            return 1
        else:
            alturas_hijos = [self.soporteAltura(hijo) for hijo in nodo.next]
            return 1 + max(alturas_hijos)

class Arbol:
    def __init__(self, dll):
        self.LDE = dll
    
#Prueba del codigo hecho anteriormente

#Creamos la lista doblemente enlazada que usara el arbol
test = ListaDE()

#Creamos los nodos del arbol
n1 = Nodo("A")
n2 = Nodo("B")
n3 = Nodo("C")
n4 = Nodo("D")
n5 = Nodo("E")
n6 = Nodo("F")
n7 = Nodo("G")
n8 = Nodo("H")
n9 = Nodo("I")

#Se agregaran los nodos a "test"
test.agregarLDE(n1,n2)
test.agregarLDE(n1,n3)
test.agregarLDE(n3,n4)
test.agregarLDE(n3,n5)
test.agregarLDE(n2,n8)
test.agregarLDE(n2,n7)
test.agregarLDE(n2,n6)
test.agregarLDE(n8,n9)

#Los resultados deberian ser los siguientes:
#Peso: 9
#Orden: 3
#Altura: 4
    
#Creamos el arbol para comprobar:
testTree = Arbol(test)

print(testTree.LDE.pesoRecorrido())
print(testTree.LDE.getOrder())
print(testTree.LDE.getHeight())

print()

#Efectivamente dan los resultados mencionados anteriormente
#Ahora se agregara un nuevo nodo para verificar si sigue funcionando

n10 = Nodo("J")
test.agregarLDE(n2,n10)
#Los resultados ahora deberian ser: Peso: 10 ; Orden: 4 ; Altura: 4 (Igual)
print(testTree.LDE.pesoRecorrido())
print(testTree.LDE.getOrder())
print(testTree.LDE.getHeight())
#Efectivamente dan los resultados propuestos anteriormente.

#Por otro lado, teniendo en cuenta que las indicaciones de la actividad dicen que los nodos se deben ingresar por teclado
#A continuación, se presenta un menu para poder realizar esto
print()
real = ListaDE()
almacenamiento = []

print("Crear arboles mediante listas enlazadas")
print("A continuacion usted creara los nodos que considere necesarios")
print("Al final de cada procedimiento se le dira como finalizar la operacion si asi usted lo desea.")
print("Tenga en cuenta que lo que usted ingrese sera el dato que almacene cada nodo.")
print("Tenga en cuenta que luego cuando usted decida el orden del arbol debera ingresar numeros, el primer nodo fue el primero que usted ingreso")
print("y asi sucesivamente.")
print()

verify = None
while verify!="OUT":
    verify = input("Ingrese la informacion del nodo (Si crea nodo): ")
    nX = Nodo(verify)
    almacenamiento.append(nX)
    verify = input("-->Escriba OUT para finalizar este procedimiento, sino es asi, se ignorara lo ingresado (no crea nodo): ")

print("")
print("A continuacion, usted debera poner primero el nodo padre y posteriormente el nodo hijo, porfavor no repita nodos de una manera incoherente para evitar errores")
print("Tenga en cuenta que cuando usted decida el orden del arbol debera ingresar numeros, por ejemplo, si usted ingresa 0, se refiere")
print("al primer nodo que usted ingreso anteriormente.")
print("El sistema crea almenos un nodo, si solo creo un nodo sera redireccionado a la siguiente seccion")
print("")

if len(almacenamiento) == 1:
    real.head = almacenamiento[0]
    pass
else:
    verify2 = None
    while verify2!="OUT":
        x1 = int(input("Ingrese el nodo padre (numero): "))
        x2 = int(input("Ingrese el nodo hijo (numero): "))
        if 0 <= x1 < len(almacenamiento) and 0 <= x2 < len(almacenamiento):
            real.agregarLDE(almacenamiento[x1], almacenamiento[x2])
            verify2 = input("Escriba OUT si quiere finalizar este proceso: ")
        else: 
            print("Indice fuera de rango, reinicie el programa e intente de nuevo.")
            verify2 = "OUT"

print("")
print("A continuacion, usted podra eliminar nodos, tenga en cuenta que si elimina un nodo elimina todos sus hijos y los hijos de sus hijos")
print("y asi sucesivamente.")
print("Tenga en cuenta que cuando usted decida si va a eliminar nodos del arbol debera ingresar numeros, por ejemplo, si usted ingresa 0, se refiere")
print("al primer nodo que usted ingreso anteriormente.")
print("Si despues de borrar ya no quedan nodos, evite intentar eliminar mas nodos puesto que intentar esto generara un error")
print("")

verify3 = None
aux = None
while verify3!="OUT":
    print("Desea borrar algun nodo?, escriba OUT si no es asi, de lo contrario escriba cualquier otra cosa (Si no hay nodos finaliza automaticamente)")
    x0 = input()
    if x0 != "OUT":
        print("Ingrese el nodo (numero)")
        x3 = int(input())
        real.eliminarLDE(almacenamiento[x3])
        if x3 == 0:
            verify3 = "OUT"
            aux = 0
            real.head = None
            almacenamiento.clear()
    else:
        verify3 = "OUT"

print("")
print("A continuacion, se presentan los resultados del arbol propuesto (Peso, Orden, Altura)")
print("")
realTree = Arbol(real)
if aux == 0:
    print("0")
    print("0")
    print("0")
else:
    print(realTree.LDE.pesoRecorrido())
    print(realTree.LDE.getOrder())
    print(realTree.LDE.getHeight())
print()
print("Si desea hacer más arboles porfavor corra el programa nuevamente. GRACIAS")

#NOTA: Los índices en almacenamiento no reflejan los nodos válidos después de eliminar.