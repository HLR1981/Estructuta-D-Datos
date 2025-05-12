# COLA (FIFO)
from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()

    def encolar(self, elemento):
        print(f"Encolando: {elemento}")
        self.elementos.append(elemento)
        self.mostrar()

    def desencolar(self):
        if self.elementos:
            eliminado = self.elementos.popleft()
            print(f"Desencolando: {eliminado}")
        else:
            print("La cola está vacía")
        self.mostrar()

    def mostrar(self):
        print("Estado de la cola:", list(self.elementos))


# PILA (LIFO)
class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        print(f"Apilando: {elemento}")
        self.elementos.append(elemento)
        self.mostrar()

    def desapilar(self):
        if self.elementos:
            eliminado = self.elementos.pop()
            print(f"Desapilando: {eliminado}")
        else:
            print("La pila está vacía")
        self.mostrar()

    def mostrar(self):
        print("Estado de la pila:", self.elementos)


# DEMOSTRACIÓN
print("---- COLA ----")
cola = Cola()
# Encolando del 1 al 8
for i in range(1, 9):
    cola.encolar(str(i))
# Desencolando todos
for _ in range(8):
    cola.desencolar()

print("\n---- PILA ----")
pila = Pila()
# Apilando de la A a la H
for letra in "ABCDEFGH":
    pila.apilar(letra)
# Desapilando todos
for _ in range(8):
    pila.desapilar()