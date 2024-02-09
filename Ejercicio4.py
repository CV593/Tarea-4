class ColaConPilas:
    def __init__(self):
        # Se crean dos pilas, una para la entrada y otra para la salida
        self.pila_entrada = []
        self.pila_salida = []
    def enqueue(self, elemento):
        # La operación enqueue se realiza en la pila de entrada
        self.pila_entrada.append(elemento)
    def dequeue(self):
        # Verificamos si la pila de salida está vacía
        if not self.pila_salida:
        #transferimos los elementos de la pila de entrada a la pila de salida invirtiendo el orden
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())
        # Si la pila de salida sigue vacía después de la transferencia, la cola está vacía
        if not self.pila_salida:
            raise IndexError("La cola está vacía")
        # Realizamos la operación dequeue en la pila de salida
        return self.pila_salida.pop()

cola = ColaConPilas()
n = int(input("Ingrese el número de clientes a ingresar: "))
for i in range(n):
    cola.enqueue(input(f"Ingrese el nombre del cliente en el índice {i+1}: \t"))
print("Clientes ingresados en la pila de entrada", cola.pila_entrada ," Clientes en la pila de salida ",cola.pila_salida)
print("\nRealizando operaciones dequeue:")
try:
    for _ in range(n):
        print("Dequeue:", cola.dequeue())
        print("Clientes ingresados en la pila de entrada", cola.pila_entrada ," Clientes en la pila de salida ",cola.pila_salida)
except IndexError as e:
    print(e)