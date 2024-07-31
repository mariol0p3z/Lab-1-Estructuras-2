from nodo import Nodo
class Arbol_B:
    def __init__(self, grado):
        self.raiz = Nodo(True)
        self.grado = grado

    def mostrar(self):
        self.raiz.mostrar()

    def insertar(self, k):
        raiz = self.raiz
        if len(raiz.llaves) == (2*self.grado) - 1:
            tmp = Nodo()
            self.raiz = tmp
            tmp.hijos.append(raiz)
            self.dividirNodo(tmp, 0)
            self.insertarNodo(tmp,k)
        else:
            self.insertarNodo(raiz, k)

    def insertarNodo(self,x, k):
        i = len(x.llaves) -1
        if x.Eshoja:
            x.llaves.append(None)
            while i >= 0 and x.llaves[i]['dpi'] > k['dpi']:
                x.llaves[i + 1] = x.llaves[i]
                i -= 1
            x.llaves[i+1] = k
        else:
            while i >= 0 and x.llaves[i]['dpi'] > k['dpi']:
                i -= 1
            i += 1
            if len(x.hijos[i].llaves) == (2*self.grado) - 1:
                self.dividirNodo(x, i)
                if x.llaves[i]['dpi'] < k['dpi']:
                    i += 1
            self.insertarNodo(x.hijos[i], k)
    
    def dividirNodo(self,x, i):
        t = self.grado
        y = x.hijos[i]
        z = Nodo(y.Eshoja)
        x.llaves.insert(i, y.llaves[t-1])
        z.llaves = y.llaves[t:(2*t) -1]
        y.llaves = y.llaves[0:(t-1)]
        if not y.Eshoja:
            z.hijos = y.hijos[t:(2*t)]
            y.hijos = y.hijos[0:t]
        x.hijos.insert(i + 1, z)

    def buscar(self, k, x = None):
        if x is None:
            x = self.raiz
        i = x.buscarLlaves(k)
        if i < len(x.llaves) and x.llaves[i]['dpi'] == k['dpi']:
            return x,i
        if x.Eshoja:
            return None
        return self.buscar(k, x.hijos[i])

    def buscar_por_nombre_y_dpi(self, dpi, nombre, x = None):
        if x is None:
            x = self.raiz
        i = x.buscarLlaves({'dpi':dpi})
        if i < len(x.llaves) and x.llaves[i]['dpi'] == dpi:
            if x.llaves[i]['name'] == nombre:
                return x.llaves[i]
            else:
                return None
        if x.Eshoja:
            return None
        return self.buscar_por_nombre_y_dpi(dpi, nombre, x.hijos[i])
    
    def buscarNombre(self, nombre, x = None):
        if x is None:
            x = self.raiz
        resultados = []
        for llave in x.llaves:
            if llave['name'] == nombre:
                resultados.append(llave)
        if not x.Eshoja:
            for hijo in x.hijos:
                resultados.extend(self.buscarNombre(nombre, hijo))
        return resultados

    def eliminar(self, k):
        self.eliminarNodo(self.raiz, k)
    
    def eliminarNodo(self, x, k):
        t = self.grado
        i = 0
        while i < len(x.llaves) and k > x.llaves[i]:
            i += 1
        if i < len(x.llaves) and x.llaves[i] == k:
            if x.esHoja:
                x.llaves.pop[i]
            else:
                self.eliminarNodoPadre(x, i)
        else:
            if x.esHoja:
                return
            bandera = i(i== len(x.llaves))
            if len(x.hijos[i].llaves) < t:
                self.llenar(x, i)
            if bandera and i > len(x.llaves):
                self.eliminarNodo(x.hijos[i-1], k)
            else:
                self.eliminarNodo(x.hijos[i], k)
    
    def eliminarNodoPadre(self, x, i):
        k = x.llaves[i]
        if len(x.hijos[i].llaves) >= self.grado:
            ant = self.obtenerAnterior(x,i)
            x.llaves[i] = ant
            self.eliminarNodo(x.hijos[i], ant)
        elif len(x.hijos[i+1].llaves) >= self.grado:
            sig = self.obtenerSiguiente(x, i)
            x.llaves[i] = sig
            self.eliminarNodo(x.hijos[i+1], sig)
        else:
            self.unirNodo(x, i)
            self.eliminarNodo(x.hijos[i], k)

    def obtenerAnterior(self, x, i):
        tmp = x.hijos[i]
        while not tmp.esHoja:
            tmp = tmp.hijos[len(tmp.hijos) - 1]
        return tmp.llaves[len(tmp.llaves) -1]

    def obtenerSiguiente(self, x, i):
        tmp = x.hijos[i + 1]
        while not tmp.esHoja:
            tmp = tmp.hijos[0]
        return tmp.llaves[0]

    def llenar(self, x, i):
        if i != 0 and len(x.hijos[i-1].llaves) >= self.grado:
            self.prestarNodoAnt(x, i)
        elif i != len(x.hijos) - 1 and len(x.hijos[i+1].llaves) >= self.grado:
            self.prestarNodoSig(x, i)
        else:
            if i != len(x.hijos) - 1:
                self.unir(x,i)
            else:
                self.unir(x, i -1)
    
    def prestarNodoAnt(self, x, i):
        nodo_hijo = x.hijos[i]
        nodo_hermano = x.hijos[i - 1]
        for j in range(len(nodo_hijo.llaves)-1, -1, -1):
            nodo_hijo.llaves[j+1] = nodo_hijo.llaves[j]
        if not nodo_hijo.esHoja:
            for j in range(len(nodo_hijo.hijos) -1, -1,-1):
                nodo_hijo.hijos[j+1] = nodo_hijo.hijos[j]
        nodo_hijo.llaves[0] = x.llaves[i -1]
        if not x.esHoja:
            nodo_hijo.hijos[0] = nodo_hermano.hijos[len(nodo_hermano.hijos) -1]
        x.llaves[i - 1] = nodo_hijo.llaves.pop()
        if not nodo_hermano.esHoja:
            nodo_hermano.hijos.pop()
        
    def prestarNodoSig(self, x, i):
        nodo_hijo = x.hijos[i]
        nodo_hermano = x.hijos[i+1]
        nodo_hijo.llaves.append(x.llaves[i])
        if not nodo_hijo.esHoja:
            nodo_hijo.hijos.append(nodo_hermano.hijos[0])
        x.llaves[i] = nodo_hermano.llaves.pop(0)
        if not nodo_hermano.esHoja:
            nodo_hermano.hijos.pop(0)
        
    def unir(self, x,i):
        nodo_hijo = x.hijos[i]
        nodo_hermano = x.hijos[i + 1]
        nodo_hijo.llaves.append(x.llaves.pop(i))
        for j in range(len(nodo_hermano.llaves)):
            nodo_hijo.llaves.append(nodo_hermano.llaves[j])
        if not nodo_hijo.esHoja:
            for j in range(len(nodo_hermano.hijos)):
                nodo_hijo.hijos.append(nodo_hermano.hijos[j])
        x.hijos.pop(i + 1)