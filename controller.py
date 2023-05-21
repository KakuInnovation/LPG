# Importamos la clase Model del file model
from model import Model
# Importamos la clase View del file view
from view import View


class Controller:
    # Constructor - Inicialización del Objeto instanciado
    def __init__(self):
        #print("init Controller")
        self.model = Model(self)
        self.view = View(self)

    def main(self):
        #print("main Controller")
        self.view.main()
        self.model.main()

    def decargarPartidosPoliticos(self, info):
        #print("decargarPartidosPoliticos Controller")
        self.model.writePartidosPoliticos(info)

    def decargarRegionesGeograficas(self, info):
        #print("decargarRegionesGeograficas Controller")
        self.model.writeRegionesGeograficas(info)


# INICIO DE LA APP
if __name__ == '__main__':
    app = Controller()
    app.main()
