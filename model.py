

class Model:
    # Constructor - Inicialización del Objeto instanciado
    def __init__(self, controller):
        print("init Model")
        self.controller = controller
        self.filereg = 'db/regiones.csv'
        self.filepartpol = 'db/partidos.csv'

    def main(self):
        print("main of Model")

    def writeRegionesGeograficas(self, info):
        print("RegionesGeograficas of Model")
        f = open(self.filereg, 'w', encoding='UTF-8')

        print(info)

        try:
            for i in info.keys():
                for reg in info.values():
                    registro = ""
                    registro = str(i) + ";" + reg["Nombre"] + ";" + reg["Abreviatura"] + "\n"
                    str(registro)
                    registro.replace(",", "-")
                    f.write(registro)
        finally:
            f.close()

    def writePartidosPoliticos(self, info):
        print("Partidos Políticos of Model")
        f = open(self.filepartpol, 'w', encoding='UTF-8')

        print(info)

        try:
            for i in info.keys():
                for reg in info.values():
                    registro = ""
                    registro = str(i) + ";" + reg["Nombre"] + ";" + reg["Abreviatura"] + "\n"
                    str(registro)
                    registro.replace(",", "-")
                    f.write(registro)
        finally:
            f.close()
