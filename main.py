from arbolb import Arbol_B
class main():
    def __init__(self):
        self.arbol = Arbol_B(3)
    
        def insertarRegistro(arbol, registro):
            arbol.insertar(registro)

        insertarRegistro(self.arbol, {"name":"diego", "dpi":"12345678", "dateBirth": "02/01/1990", "address":"guatemala"})
        insertarRegistro(self.arbol, {"name":"abdiel","dpi":"2825347762693","datebirth":"1969-10-08T04:11:28.716Z","address":"waterloo"})
        insertarRegistro(self.arbol, {"name":"abdiel","dpi":"2353406783042","datebirth":"1978-08-13T02:57:59.580Z","address":"cuyahoga falls"})
        self.arbol.mostrar()

if __name__ == '__main__':
    main()