# implementacion de una cola de atencion


class Cola:

    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def encolar(self, elemento):
        self.elementos.append(elemento)

    def desencolar(self):
        if self.esta_vacia() == True:
            return None
        return self.elementos.pop(0)

    def cantidad(self):
        return len(self.elementos)
