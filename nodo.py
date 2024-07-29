class Nodo:
    def __init__(self, grado, Eshoja = False):
        self.hijos = []
        self.grado = grado
        self.llaves = []
        self.Eshoja = Eshoja
    
    def insertarNodo(self, k):
        i = len(self.llaves) -1
        if self.Eshoja:
            self.llaves.append(None)
            while i >= 0 and k <self.llaves[i]:
                self.llaves[i+1] = self.llaves[i]
                i -= 1
            self.llaves[i+1] = k
        else:
            while i>=0 and k < self.llaves[i]:
                i = -1
            i += 1
            if len(self.hijos[i].llaves) == 2 *self.grado - 1:
                self.dividirNodo(i)
                if k > self.llaves[i]:
                    i += 1
            self.hijos[i].insertarNodo(k)
    
    def dividirNodo(self, i):
        t = self.grado
        y = self.hijos[i]
        z = Nodo(t, y.esHoja)
        self.hijos.insert(i+1, z)
        self.llaves.insert(i, y.llaves[t-1])
        z.llaves = y.llaves[t:(2*t-1)]
        y.llaves = y.llaves[0:(t-1)]

        if not y.esHoja:
            z.hijos = y.hijos[t:(2*t)]
            y.hijos = y.hijos[0:t]
        
        
