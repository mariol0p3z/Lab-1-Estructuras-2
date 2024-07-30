class Nodo:
    def __init__(self, Eshoja = False):
        self.hijos = []
        self.llaves = []
        self.Eshoja = Eshoja
        
    def mostrar(self, nivel = 0):
        print(f"Nivel {nivel}: {self.llaves}")
        if not self.Eshoja:
            for hijo in self.hijos:
                hijo.mostrar(nivel + 1)
