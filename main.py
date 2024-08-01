from arbolb import Arbol_B
import json
import csv
class main():
    def __init__(self):
        self.arbol = Arbol_B(3)
        
        def leerArchivo(arbol: Arbol_B, nombre_archivo):
            with open(nombre_archivo, mode ='r', encoding='utf-8') as archivo:
                try:
                    for linea in archivo:
                        separacion = linea.split(";")
                        accion =  separacion[0]
                        dato = json.loads(separacion[1].lower())
                        if accion == "INSERT":
                            arbol.insertar(dato)
                        elif accion == "PATCH":
                            arbol.actualizar(dato.get("dpi"), dato.get("name"), dato)
                        elif accion == "DELETE":
                            arbol.eliminar({"name": dato.get("name"), "dpi": dato.get("dpi")})
                except FileNotFoundError:
                    print("Archivo no encontrado")
                finally:
                    archivo.close()

        def imprimirResultados(resultados):
            if resultados:
                for resultado in resultados:
                    print(json.dumps(resultado, indent = 4))
            else:
                print("No se encontraron resultados con el nombre especificado")

        def exportarSalida(resultados, nombre_archivo):
            if resultados:
                llaves = resultados[0].keys()
                with open(nombre_archivo, mode = 'w', newline='', encoding='utf-8') as archivo:
                    escritor = csv.DictWriter(archivo, fieldnames= llaves)
                    escritor.writeheader()
                    escritor.writerows(resultados)
                print(f"Resultados guardados en {nombre_archivo}")
            else:
                print("No hay resultados para guardar")

        leerArchivo(self.arbol, 'challenge.csv')
        prueba = self.arbol.buscarNombre("Edgar".lower())
        imprimirResultados(prueba)
        exportarSalida(prueba, 'Salidas/edgar.csv')


if __name__ == '__main__':
    main()