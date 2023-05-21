class View:
    # Constructor - Inicialización del Objeto instanciado
    def __init__(self, controller):
        print("init View")
        self.controller = controller
        self.salirAlMenuPrincipal = ""
        self.deDondeVengo = ""
        self.listaATrabajar = []

# Diccionario de opciones y Funciones asociadas opciones del ABM
        self.opcionesABM = {
            "1": {"Descripcion": "Alta", "Funcion": self.ParametrizacionAlta},
            "2": {"Descripcion": "Baja", "Funcion": self.ParametrizacionBaja},
            "3": {"Descripcion": "Modificar", "Funcion": self.ParametrizacionModificar},
            "4": {"Descripcion": "Ver", "Funcion": self.ParametrizacionVer}
        }

# Diccionario de opciones y Funciones asociadas Menu Parametizacion
        self.opcionesMenuParametrizacion = {
            "1": {"Descripcion": "Partidos Politicos", "Funcion": self.MenuGenerico, "Menu": self.opcionesABM},
            "2": {"Descripcion": "Regiones Geograficas", "Funcion": self.MenuGenerico, "Menu": self.opcionesABM}
        }

# Diccionario de opciones y Funciones asociadas Menu Descarga Archivos
        self.opcionesMenuDescargaArchivos = {
            "1": {"Descripcion": "Partidos Politicos", "Funcion": self.DecargarPartidosPoliticos},
            "2": {"Descripcion": "Regiones Geograficas", "Funcion": self.DecargarRegionesGeograficas}
        }

        self.opcionesMenuPrincipal = {
            "1": {"Descripcion": "Parametrizacion", "Funcion": self.MenuGenerico, "Menu": self.opcionesMenuParametrizacion},
            "2": {"Descripcion": "Descarga de Archivos", "Funcion": self.MenuGenerico, "Menu": self.opcionesMenuDescargaArchivos}
        }

# Diccionario de partidos politicos la clave es el numero y el resto son sus datos (nombre abreviatura)
        self.listaPartidosPoliticos = {
            1: {"Nombre": "FRENTE DE TODOS", "Abreviatura": "FDT", "Numero": 1},
            2: {"Nombre": "JUNTOS POR EL CAMBIO", "Abreviatura": "JXC", "Numero": 2},
            3: {"Nombre": "LIBERTRAIOS", "Abreviatura": "LIB", "Numero": 3},
            4: {"Nombre": "PERONISMO FEDERAL", "Abreviatura": "PFE", "Numero": 4},
            5: {"Nombre": "FRENTE DE IZQUIERDA", "Abreviatura": "FDI", "Numero": 5},
            6: {"Nombre": "LIBRES DEL SUR", "Abreviatura": "LBS", "Numero": 6},
        }

# Diccionario de provincias la clave es un numero autoincremental y su nombre
        self.listaProvincias = {
            1: {"Nombre": "CABA", "Numero": 1},
            2: {"Nombre": "BUENOS AIRES", "Numero": 2},
            3: {"Nombre": "CATAMARCA", "Numero": 3},
            4: {"Nombre": "CHACO", "Numero": 4},
            5: {"Nombre": "CHUBUT", "Numero": 5},
            6: {"Nombre": "CORDOBA", "Numero": 6},
            7: {"Nombre": "CORRIENTES", "Numero": 7},
            8: {"Nombre": "ENTRE RIOS", "Numero": 8},
            9: {"Nombre": "FORMOSA", "Numero": 9},
            10: {"Nombre": "JUJUY", "Numero": 10},
            11: {"Nombre": "LA PAMPA", "Numero": 11},
            12: {"Nombre": "LA RIOJA", "Numero": 12},
            13: {"Nombre": "MENDOZA", "Numero": 13},
            14: {"Nombre": "MISIONES", "Numero": 14},
            15: {"Nombre": "NEUQUEN", "Numero": 15},
            16: {"Nombre": "RIO NEGRO", "Numero": 16},
            17: {"Nombre": "SALTA", "Numero": 17},
            18: {"Nombre": "SAN JUAN", "Numero": 18},
            19: {"Nombre": "SAN LUIS", "Numero": 19},
            20: {"Nombre": "SANTA CRUZ", "Numero": 20},
            21: {"Nombre": "SANTA FE", "Numero": 21},
            22: {"Nombre": "SANTIAGO DEL ESTERO", "Numero": 22},
            23: {"Nombre": "TIERRA DEL FUEGO", "Numero": 23},
            24: {"Nombre": "TUCUMAN", "Numero": 24}
        }

        self.datosDeCadaLista = {
            "Partidos Politicos": {"ElementosSolicitar": ["Nombre", "Abreviatura", "Numero"], "Lista": self.listaPartidosPoliticos},
            "Regiones Geograficas": {"ElementosSolicitar": ["Nombre", "Numero"], "Lista": self.listaProvincias}
        }

    def main(self):
        print("main of View!\n")

        while True:
            # definimos esta variable como global para que pueda ser consumida por cualquier Funcion
            # global salirAlMenuPrincipal
            # global deDondeVengo
            # verifiacmos que la variable ya existe o todavia no tiene un valor (es decir la primera vez que se ejecuta el codigo)
            # if 'salirAlMenuPrincipal' in globals():
            if self.salirAlMenuPrincipal == "":
                if self.salirAlMenuPrincipal != False:
                    print("Bienvenido al Sistema de Elecciones Presidenciales")
            self.salirAlMenuPrincipal = False
            self.deDondeVengo = "MenuPrincipal"
            # mostramos opciones
            self.MostrarOpcionesMenuPrincipal()

            # solicitamos opcion
            seleccion = input("Por favor, selecciona una opcion => ")

            # seleccionamos de nuestras opciones mediante su clave (la hacemos por separado ya que se espera que se ingrese numeros generando asi no tener que recorrer el objeto)
            if seleccion in self.opcionesMenuPrincipal:
                # buscamos la opcion seleccionada
                opcion = self.opcionesMenuPrincipal[seleccion]
                # Llama a la funcion correspondiente
                opcion["Funcion"](opcion["Menu"], opcion["Descripcion"])
            # seleccionamos de nuestras opciones mediante su desciocion
            elif seleccion in [opcion["Descripcion"] for opcion in self.opcionesMenuPrincipal.values()]:
                for clave, opcion in self.opcionesMenuPrincipal.items():
                    if opcion["Descripcion"] == seleccion:
                        opcion["Funcion"](
                            opcion["Menu"], opcion["Descripcion"])
                        break
            # si la opcion es 1 mas que la lista
            elif seleccion == str(len(self.opcionesMenuPrincipal) + 1):
                print("Finalizando programa")
                # finaliza el programa
                break
            else:
                print("Opcion invalida. Por favor, selecciona nuevamente.")

# Mostrar Opciones Menu Principal
    def MostrarOpcionesMenuPrincipal(self):
        for opcion, Funcion in self.opcionesMenuPrincipal.items():
            print(f"{opcion}) {Funcion['Descripcion']}")
        print(f"{len(self.opcionesMenuPrincipal) + 1}) Salir")

# Mostrar Opciones Menu Parametrizacion
    def MostrarOpcionesMenuParametrizacion(self):
        for opcion, Funcion in self.opcionesMenuParametrizacion.items():
            print(f"{opcion}) {Funcion['Descripcion']}")
        print(f"{len(self.opcionesMenuPrincipal) + 1}) Salir")

# Mostrar Opciones Menu DescargaArchivos
    def MostrarOpcionesMenuDescargaArchivos(self):
        for opcion, Funcion in self.opcionesMenuDescargaArchivos.items():
            print(f"{opcion}) {Funcion['Descripcion']}")
        print(f"{len(self.opcionesMenuPrincipal) + 1}) Salir")

    # Mostrar Opciones Menu Generico
    def MostrarOpcionesMenu(self, menu):
        for opcion, Funcion in menu.items():
            print(f"{opcion}) {Funcion['Descripcion']}")
        print(f"{len(menu) + 1}) Volver")
        print(f"{len(menu) + 2}) Menu Principal")

    # Funcion para confirmacion de datos
    def EjecutarConfirmacion(self, si="Confirmar", no="Cancelar"):
        retorno = 0
        while retorno == 0:
            print("1)", si)
            print("0)", no)
            seleccion = input("Por favor, selecciona una opcion => ")
            if seleccion == "1" or seleccion == si:
                retorno = True
            elif seleccion == "0" or seleccion == no:
                retorno = False
            else:
                print("Opcion invalida. Por favor, selecciona nuevamente.")
        return retorno

    # verificamos si no hay simbolos
    def ValidacionUnicamenteTexto(self, texto):
        textoSinEspacios = texto.replace(" ", "")
        return textoSinEspacios.isalpha()

    # Funcion Descargar Partidos politicos
    def DecargarPartidosPoliticos(self):
        print("Descargado Partidos Políticos...")
        self.controller.decargarPartidosPoliticos(self.listaATrabajar)

    # Funcion Descargar Regiones Geograficas
    def DecargarRegionesGeograficas(self):
        print("Descargado Regiones Geográficas...")
        self.controller.decargarRegionesGeograficas(self.listaATrabajar)

    # Funcion para no tener que repetir el mismo mensaje permitiendo cambiar facilmente
    def MensajeErrorValidacion(self, dato, campo, tipo):
        if tipo == "Modificar":
            print(
                campo, "Invalido, Recuerde si quiere Mantener la Informacion Dejelo el Campo en Blanco")
            dato = input("Por Favor, Ingrese el " + campo + " nuevamente =>")
        else:
            dato = input(campo+" Invalido, Ingrese el " +
                         campo + " nuevamente => ")
        return dato

    # Funcion para no tener que repetir el mismo mensaje permitiendo cambiar facilmente
    # Si se equivoca multiples veces mostrar Recordatorio

    def MensajeVolverAtras(self, cantidad=0):
        if cantidad == 0:
            print(
                "Ingrese 'Volver Atras' en cualquier momenento si desea Regresar al Menu anterior.")
        elif cantidad == 3:
            print("Recuerde que Ingrando 'Volver Atras' Regresara al Menu anterior.")
        cantidad += 1
        return cantidad

# Funcion para verificar si esta el elemento en la lista, claveElemento es para si son iguales permitirmos continuar el proceso
    def VerificarRepetidos(self, lista, dato, claveElemento="", campo=""):
        for clave, opcion in lista.items():
            if campo == "":
                if str(clave) == str(claveElemento):
                    return True
            else:
                if opcion[campo] == dato:
                    if str(clave) == claveElemento or opcion["Nombre"] == claveElemento:
                        return False
                    else:
                        return True
        return False

# funcion para validar cada dato d e las altas
    def ValidacionesCampo(self, dato, campo, tipo, claveElemento=""):
        # global deDondeVengo
        flag = False
        if self.deDondeVengo == "Partidos Politicos":
            if campo == "Nombre":
                while dato == "" or self.VerificarRepetidos(self.listaPartidosPoliticos, dato, claveElemento, "Nombre"):
                    if dato == "" and tipo == "Modificar":
                        break
                    if self.VerificarRepetidos(self.listaPartidosPoliticos, dato, "Nombre") == True:
                        print("Este Nombre ya pertence a un Partido")
                    dato = self.MensajeErrorValidacion(dato, campo, tipo)
                    dato = str(dato).upper()
                dato = dato.upper()
            elif campo == "Abreviatura":
                while (not dato.isalpha()) or len(dato) != 3 or self.VerificarRepetidos(self.listaPartidosPoliticos, dato, claveElemento, "Abreviatura"):
                    if dato == "" and tipo == "Modificar":
                        break
                    if self.VerificarRepetidos(self.listaPartidosPoliticos, dato, claveElemento, "Abreviatura") == True:
                        print("Este Abreviatura ya pertence a un Partido")
                    dato = self.MensajeErrorValidacion(dato, campo, tipo)
                    dato = str(dato).upper()
                dato = dato.upper()
            elif campo == "Numero":
                while flag == False:
                    if dato == "" and tipo == "Modificar":
                        break
                    elif str(dato).isdigit():
                        dato = int(dato)
                        if 0 < dato <= 999:
                            if self.VerificarRepetidos(self.listaPartidosPoliticos, dato, claveElemento, "Numero") == False:
                                flag = True
                            else:
                                print("Este Numero ya pertence a un Partido:",
                                      self.listaPartidosPoliticos[dato]["Nombre"])
                    # no cambiar a elif
                    if flag == False:
                        dato = self.MensajeErrorValidacion(dato, campo, tipo)

        elif self.deDondeVengo == "Regiones Geograficas":
            if campo == "Nombre":
                while flag == True:
                    while (not self.ValidacionUnicamenteTexto(dato)) or dato == "":
                        if dato == "" and tipo == "Modificar":
                            break
                        dato = self.MensajeErrorValidacion(dato, campo, tipo)
                    dato = dato.upper()
                    flag = self.VerificarRepetidos(
                        self.listaProvincias, dato, claveElemento, "Nombre")
                    if flag == True:
                        if tipo == "Modificar":
                            print(
                                "Provincia ya Existente, Recuerde si quiere Mantener la Informacion Dejelo el Campo en Blanco")
                            dato = input("Por Favor, Ingrese el " +
                                         campo + " nuevamente => ")
                        else:
                            dato = input(
                                "Provincia ya Existente, Ingrese el " + campo + " nuevamente => ")
        return dato

    # Funcion que redirige a la funcion de alta espesifica
    def ParametrizacionAlta(self):
        # global deDondeVengo
        opciones = self.datosDeCadaLista[self.deDondeVengo]["ElementosSolicitar"]
        self.listaATrabajar = self.datosDeCadaLista[self.deDondeVengo]["Lista"]
        elemento = {}
        print("Alta", self.deDondeVengo)
        self.MensajeVolverAtras()
        for campo in opciones:
            dato = input("Ingrese " + campo + " => ")
            if dato == "Volver Atras":
                return
            else:
                elemento[campo] = self.ValidacionesCampo(dato, campo, "Alta")

        clave = max(self.listaATrabajar.keys()) + 1
        textoEscribir = ""
        totalElementos = len(elemento)
        indiceActual = 0
        for propiedad, valor in elemento.items():
            indiceActual += 1
            textoEscribir += str(propiedad) + ": " + str(valor)
            if indiceActual != totalElementos:
                textoEscribir += " / "
        print(str(clave) + ")", textoEscribir)

        confirmacion = self.EjecutarConfirmacion()
        if confirmacion == True:
            self.listaATrabajar[clave] = elemento
            print(self.deDondeVengo, "Registrado Existosamente")
        else:
            print(self.deDondeVengo, "No Registrado")

# Funcion que suplanta al find
    def BuscarElementoLista(self, dato, listaATrabajar):
        encontrado = None
        mostrarMensajeVolverAtras = 0
        while encontrado == None:
            if dato == "Volver Atras":
                return
            else:
                for clave, opciones in listaATrabajar.items():
                    if str(clave) == str(dato):
                        encontrado = clave
                        break
                    elif "Nombre" in opciones:
                        dato = str(dato).upper()
                        if dato == opciones["Nombre"]:
                            encontrado = clave
                            break
            if encontrado == None:
                mostrarMensajeVolverAtras = self.MensajeVolverAtras(
                    mostrarMensajeVolverAtras)
                dato = input(
                    "No se ha Encontrado el Campo, Por Favor Ingrese Nuevamente => ")
        return encontrado

# Funcion Parametrizacion Baja
    def ParametrizacionBaja(self):
        # global deDondeVengo
        print("Baja", self.deDondeVengo)
        self.ParametrizacionVer()
        dato = input("Ingrese el elemento a Eliminar => ")
        if dato == "Volver Atras":
            return
        self.listaATrabajar = self.datosDeCadaLista[self.deDondeVengo]["Lista"]
        dato = self.BuscarElementoLista(dato, self.listaATrabajar)

        elemento = self.listaATrabajar[dato]
        textoEscribir = ""
        totalElementos = len(elemento)
        indiceActual = 0
        for propiedad, valor in elemento.items():
            indiceActual += 1
            textoEscribir += str(propiedad) + ": " + str(valor)
            if indiceActual != totalElementos:
                textoEscribir += " / "
        print(str(dato) + ")", textoEscribir)

        confirmacion = self.EjecutarConfirmacion()
        if confirmacion == True:
            del self.listaATrabajar[dato]
            print("Registrado Eliminado Existosamente")
        else:
            print("Registrado No Eliminado")

# Funcion Parametrizacion Modificar
    def ParametrizacionModificar(self):
        # global deDondeVengo
        print("Modificacion", self.deDondeVengo)
        print("¿Desea Ver las Opciones?")

        if self.EjecutarConfirmacion("Si", "No") == True:
            self.ParametrizacionVer()
        self.MensajeVolverAtras()

        dato = input("Ingrese el campo a Modificar => ")
        if dato == "Volver Atras":
            return

        self.listaATrabajar = self.datosDeCadaLista[self.deDondeVengo]["Lista"]
        encontrado = self.BuscarElementoLista(dato, self.listaATrabajar)

        opciones = self.datosDeCadaLista[self.deDondeVengo]["ElementosSolicitar"]
        elemento = {}

        for campo in opciones:
            dato = input("Ingrese " + campo + " => ")
            if dato == "Volver Atras":
                return
            else:
                elemento[campo] = self.ValidacionesCampo(
                    dato, campo, "Modificar", encontrado)

        clave = max(self.listaATrabajar.keys()) + 1

        textoEscribir = ""
        totalElementos = len(elemento)
        indiceActual = 0
        for propiedad, valor in elemento.items():
            indiceActual += 1
            textoEscribir += str(propiedad) + ": " + str(valor)
            if indiceActual != totalElementos:
                textoEscribir += " / "
        print("Nuevo Elemetno)", textoEscribir)

        confirmacion = self.EjecutarConfirmacion()

        if confirmacion == True:
            del self.listaATrabajar[encontrado]
            self.listaATrabajar[clave] = elemento
            print("Cambio Registrado")
        else:
            print("Cambio No Registrado")

# Funcion Parametrizacion Ver
    def ParametrizacionVer(self):
        # global deDondeVengo
        lista = None
        if self.deDondeVengo == "Partidos Politicos":
            lista = self.listaPartidosPoliticos
        elif self.deDondeVengo == "Regiones Geograficas":
            lista = self.listaProvincias

        valorOpcion = 0
        if lista != None:
            print(self.deDondeVengo)
            for clave, obj in lista.items():
                valorOpcion += 1
                textoEscribir = ""
                totalElementos = len(obj)
                indiceActual = 0
                for propiedad, valor in obj.items():
                    indiceActual += 1
                    textoEscribir += str(propiedad) + ": " + str(valor)
                    if indiceActual != totalElementos:
                        textoEscribir += " / "
                print(str(valorOpcion) + ")", textoEscribir)
        else:
            print("No hay", self.deDondeVengo, "Cargadas")
        input("Pulse Enter para Continuar ")

    # Funcion menu Generico
    def MenuGenerico(self, menu, titulo):
        salir = False
        # global salirAlMenuPrincipal
        # global deDondeVengo
        while salir == False and self.salirAlMenuPrincipal == False:
            self.deDondeVengo = titulo
            tituloMostrar = "Menu " + titulo
            print(tituloMostrar)
            # mostramos opciones
            self.MostrarOpcionesMenu(menu)

            # solicitamos opcion
            seleccion = input("Por favor, selecciona una opcion => ")

            # seleccionamos de nuestras opciones mediante su clave
            if seleccion in menu:
                opcion = menu[seleccion]

                if "Menu" in opcion:
                    # Llama a la funcion correspondiente
                    opcion["Funcion"](opcion["Menu"], opcion["Descripcion"])
                else:
                    opcion["Funcion"]()  # Llama a la funcion correspondiente1
                salir = False

            elif seleccion in [opcion["Descripcion"] for opcion in menu.values()]:
                for clave, opcion in menu.items():
                    if opcion["Descripcion"] == seleccion:
                        if "Menu" in opcion:
                            # Llama a la funcion correspondiente
                            opcion["Funcion"](
                                opcion["Menu"], opcion["Descripcion"])
                        else:
                            # Llama a la funcion correspondiente1
                            opcion["Funcion"]()
                        salir = False

            # si la opcion es 1 mas que la lista
            elif seleccion == str(len(menu) + 1) or seleccion == "Volver":
                salir = True
                # finaliza el programa
                break
            elif seleccion == str(len(menu) + 2) or seleccion == "Menu Principal":
                self.salirAlMenuPrincipal = True
                # finaliza el programa
                break
            else:
                print("Opcion invalida. Por favor, selecciona nuevamente.")
