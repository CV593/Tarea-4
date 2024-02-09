from collections import deque
from queue import PriorityQueue
import time

class Cola:
    def __init__(self):
        #se crea una cola en forma de una lista
        self.cola = deque()
        #Agregar elementos a la cola
    def mostrar(self):
        return self.cola
    def enqueue(self, elemento):
        self.cola.append(elemento)
        #Ver el primer elemento e la cola y eliminarlo
    def dequeue(self):
        if len(self.cola) < 1:
            return None
        #se le pone index 0 ya que queremos el primer elemento
        return self.cola.popleft()
    #ver el primer elemento de la cola
    def front(self):
        if len(self.cola) < 1:
            return None
        #se le pone index 0 ya que queremos el primer elemento
        return self.cola[0]
    # Implementación de una Cola (Queue)
    def simular_linea(self):
        if len(self.cola) > 0:
            queue = deque(self.cola)
            while queue:
                print(f"Atendiendo al cliente {queue.popleft()}")
                if len(queue) > 0:
                    print(f"Clientes restantes en la cola: {len(queue)}")
                    time.sleep(2)
                else:
                    print("Se han atendido a todos los clientes")
                
        else:
            raise IndexError("La pila está vacía")
# Crear una cola
cola = Cola()
# Agregar elementos a la cola
n = int(input("Cuantos Clientes Desea Ingresar? \t"))
for i in range(n):
    cola.enqueue(input(f"Ingrese el Nombre del Cliente {i+1}: \t"))
# Mostrar los elementos de la cola
print(cola.mostrar()) 
# Ver el primer elemento sin eliminarlo
print(cola.front()) 
# Sacar el primer elemento de la cola
print(cola.dequeue()) 
#ver el funcionamiento de la linea
cola.simular_linea()
