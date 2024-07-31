class Nodo:
    def __init__(self, Eshoja = False):
        self.hijos = []
        self.llaves = []
        self.Eshoja = Eshoja
        
    def buscarLlaves(self, k):
        i = 0
        while i<len(self.llaves) and self.llaves[i]['dpi'] < k['dpi']:
            i += 1
        return i

    def mostrar(self, nivel = 0):
        print(f"Nivel {nivel}: {self.llaves}")
        if not self.Eshoja:
            for hijo in self.hijos:
                hijo.mostrar(nivel + 1)