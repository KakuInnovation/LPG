
class Model:
    # Constructor - Inicialización del Objeto instanciado
    def __init__(self, controller):
        #print("init Model")
        self.controller = controller
        self.filereg = 'db/regiones.csv'
        self.filepartpol = 'db/partidos.csv'

    def main(self):
        #print("main of Model")
        pass

    def writeRegionesGeograficas(self, info):
        #print("RegionesGeograficas of Model")
        f = open(self.filereg, 'w', encoding='UTF-8')

        try:
            for reg in info.values():
                registro = ""
                registro = str(reg["Numero"]) + ";" + reg["Nombre"] + "\n"
                str(registro)
                f.write(registro)
        finally:
            f.close()

    def writePartidosPoliticos(self, info):
        #print("Partidos Políticos of Model")
        f = open(self.filepartpol, 'w', encoding='UTF-8')

        try:
            for reg in info.values():
                registro = ""
                registro = str(reg["Numero"]) + ";" + \
                    reg["Nombre"] + ";" + reg["Abreviatura"] + "\n"
                str(registro)
                f.write(registro)
        finally:
            f.close()
