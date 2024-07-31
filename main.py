from arbolb import Arbol_B
class main():
    def __init__(self):
        self.arbol = Arbol_B(3)
    
        def insertarRegistro(arbol, registro):
            arbol.insertar(registro)

        valores = [
        {"name": "diego", "dpi": "12345678", "dateBirth": "02/01/1990", "address": "guatemala"},
        {"name": "ana", "dpi": "87654321", "dateBirth": "15/03/1985", "address": "mexico"},
        {"name": "juan", "dpi": "23456789", "dateBirth": "10/07/1992", "address": "peru"},
        {"name": "maria", "dpi": "34567890", "dateBirth": "25/12/1988", "address": "chile"},
        {"name": "luis", "dpi": "45678901", "dateBirth": "05/05/1987", "address": "argentina"},
        {"name": "carlos", "dpi": "56789012", "dateBirth": "20/11/1990", "address": "colombia"},
        {"name": "laura", "dpi": "67890123", "dateBirth": "08/09/1986", "address": "uruguay"},
        {"name": "pedro", "dpi": "78901234", "dateBirth": "17/01/1995", "address": "venezuela"},
        {"name": "diego", "dpi": "54545646", "dateBirth": "01/01/1988", "address": "nicaragua"},
        {"name": "juan", "dpi": "89012345", "dateBirth": "30/08/1993", "address": "ecuador"}
        ]
        for val in valores:
            insertarRegistro(self.arbol, val)
        
        self.arbol.mostrar()

        print("*************************************************************************************************************************")
        print(self.arbol.buscarNombre("juan"))
        print("*************************************************************************************************************************")
        self.arbol.actualizar("23456789", "juan", {"address": "nueva direccion en peru", "dateBirth": "01/01/1991"})
        print("*************************************************************************************************************************")
        resultado = self.arbol.buscar_por_nombre_y_dpi("23456789", "juan")
        print(resultado)
        print("*************************************************************************************************************************")
        self.arbol.eliminar("89012345", "juan")
        print(self.arbol.buscarNombre("juan"))
        print("*************************************************************************************************************************")
        print(self.arbol.buscar_por_nombre_y_dpi("89012345", "juan"))
        print("*************************************************************************************************************************")
        self.arbol.mostrar()

if __name__ == '__main__':
    main()