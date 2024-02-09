from collections import deque
import time
class Clientes:
    def __init__(self):
        # Definimos un atributo tipo lista
        self.items = []
    #Funcion para imprimir los elementos
    def mostrar(self):
        return self.items   
    # Creamos una función para agregar datos a la pila
    def agregar(self, x):
        self.items.append(x)
    # Creamos una función para eliminar el último dato de la pila
    def eliminar(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")
    # Creamos una función para ver el último dato de la pila sin eliminarlo
    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            raise IndexError("La pila está vacía")
    # Implementación de una Cola (Queue)
    def simular_linea(self):
        if len(self.items) > 0:
            queue = deque(self.items)
            while queue:
                print(f"Atendiendo al cliente {queue.popleft()}")
                if len(queue) > 0:
                    print(f"Clientes restantes en la cola: {len(queue)}")
                    time.sleep(2)
                else:
                    print("Se han atendido a todos los clientes")
        else:
            raise IndexError("La pila está vacía")
    # Revierte todos los elementos de la lista
    def revertir(self):
        if self.items:
            pila = []
            for e in self.items:
                pila.append(e)
            lista_revertida = []
            while pila:
                lista_revertida.append(pila.pop())
            return lista_revertida
        else:
            raise IndexError("La pila está vacía")

cliente = Clientes()

n = int(input("Cuantos Clientes Desea Ingresar? \t"))
for i in range(n):
    cliente.agregar(input(f"Ingrese el Nombre del Cliente {i+1}: \t"))

print(f"Los Clientes ingresados son: {'  '.join(map(str, cliente.mostrar()))}")
print(f"El ultimo dato de la fila es: {cliente.eliminar()} y se borro")
print(f"Ahora el ultimo dato de la fila es: {cliente.peek()}")
cliente.simular_linea()
print(f"La lista revertida es {'  '.join(map(str, cliente.revertir()))}")
