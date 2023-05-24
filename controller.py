# Importamos la clase Model del file model
from model import Model
# Importamos la clase View del file view
from view import View


class Controller:
    # Constructor - Inicialización del Objeto instanciado
    def __init__(self):
        self.model = Model(self)
        self.view = View(self)

    def main(self):
        self.view.main()
        self.model.main()

    def decargarPartidosPoliticos(self, info):
        self.model.writePartidosPoliticos(info)

    def decargarRegionesGeograficas(self, info):
        self.model.writeRegionesGeograficas(info)

    def decargarArchivoVotacion(self, info):
        self.model.writeArchivoVotacion(info)

    def readPartidosPoliticos(self):
        self.model.readPartidosPoliticos()

    def readegionesGeograficas(self):
        self.model.readPartidosPoliticos()

    def generarVotacion(self, repeticion):
        pass

    def ValidacionDNI(self, dni):
        cantidad = 0
        for element in self.Votos:
            if element["Dni"] == dni:
                cantidad += 1
        if cantidad <= 4:
            return False
        else:
            return True

    def ValidacionVotoProvinciaExistente(self, dni):
        for element in self.Votos:
            if element["Dni"] == dni:
                return element["Provincia"]
        return None



# INICIO DE LA APP
if __name__ == '__main__':
    # Instanciamos la clase Controller
    app = Controller()
# Invocamos al método main de la clase Controller
    app.main()
