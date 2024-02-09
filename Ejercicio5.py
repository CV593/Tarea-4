from collections import deque
# Revierte solo la mitad de una cola
class Cola:
    def __init__(self):
        # Se crea una cola en forma de una lista
        self.cola = deque()
    def mostrar(self):
        return self.cola
    def enqueue(self, elemento):
        self.cola.append(elemento)
    def revertir_mitad(self):
        if self.cola:
            # Mira la cantidad entera de la mitad de la cola
            mitad = len(self.cola) // 2
            # Llenar la pila con la mitad de la cola
            pila = [self.cola.popleft() for _ in range(mitad)]
            # Revertir la mitad de la cola usando la pila
            self.cola.extend(reversed(pila))
        else:
            raise IndexError("La Cola está vacía")

cola = Cola()
# Agregar elementos a la cola
n = int(input("Cuantos numeros desea ingresar? \t"))
for i in range(n):
    cola.enqueue(input(f"Ingrese el numero a ingresar en el índice {i+1}: \t"))
print("Cola original:", cola.mostrar())
# Revertir la mitad de la cola
cola.revertir_mitad()
print("Cola con la mitad revertida:", cola.mostrar())