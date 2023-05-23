
class Model:
    # Constructor - Inicialización del Objeto instanciado
    def __init__(self, controller):
        # print("init Model")
        self.controller = controller
        self.filereg = 'db/regiones.csv'
        self.filepartpol = 'db/partidos.csv'
        self.filevotacion = 'db/votacion.csv'

    def main(self):
        # print("main of Model")
        pass

    def writeRegionesGeograficas(self, info):
        if info != None:
            # print("RegionesGeograficas of Model")
            f = open(self.filereg, 'w', encoding='UTF-8')

            try:
                for reg in info.values():
                    registro = ""
                    registro = str(reg["Codigo"]) + ";" + reg["Nombre"] + "\n"
                    str(registro)
                    f.write(registro)
            except:
                print("Error al escribir el Archivo")
            finally:
                f.close()
                print("Archivo Generado")

    def writePartidosPoliticos(self, info):
        if info != None:
            # print("Partidos Políticos of Model")
            f = open(self.filepartpol, 'w', encoding='UTF-8')

            try:
                for reg in info.values():
                    registro = ""
                    registro = str(reg["Lista"]) + ";" + \
                        reg["Nombre"] + ";" + reg["Abreviatura"] + "\n"
                    str(registro)
                    f.write(registro)
            except:
                print("Error al escribir el Archivo")
            finally:
                f.close()
                print("Archivo Generado")

    def writeArchivoVotacion(self, info):
        if info != None:
            f = open(self.filevotacion, 'w', encoding='UTF-8')

            try:
                for reg in info.values():
                    registro = ""
                    registro = str(reg["Lista"]) + ";" + \
                        reg["Nombre"] + ";" + reg["Abreviatura"] + "\n"
                    str(registro)
                    f.write(registro)
            except:
                print("Error al escribir el Archivo")
            finally:
                f.close()
                print("Archivo Generado")

    def readPartidosPoliticos(self):
        pass

    def readRegionesGeograficas(self):
        pass
