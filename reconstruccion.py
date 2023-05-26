filereg = 'db/regiones.csv'
filepartpol = 'db/partidos.csv'
filevotacion = 'db/votacion.csv'

def temporal():
    print("a")

def main():
    while True:
        # definimos esta variable como global para que pueda ser consumida por cualquier Funcion
        global salirAlMenuPrincipal
        global deDondeVengo
        # verifiacmos que la variable ya existe o todavia no tiene un valor (es decir la primera vez que se ejecuta el codigo)
        if 'salirAlMenuPrincipal' in globals():
            if salirAlMenuPrincipal != False:
                print("Bienvenido al Sistema de Elecciones Presidenciales")
        salirAlMenuPrincipal = False
        deDondeVengo = "MenuPrincipal"
        # mostramos opciones
        MostrarOpcionesMenuPrincipal()

        # solicitamos opcion
        seleccion = input("Por favor, selecciona una opcion => ")

        # seleccionamos de nuestras opciones mediante su clave (la hacemos por separado ya que se espera que se ingrese numeros generando asi no tener que recorrer el objeto)
        if seleccion in opcionesMenuPrincipal:
            # buscamos la opcion seleccionada
            opcion = opcionesMenuPrincipal[seleccion]
            # Llama a la funcion correspondiente
            opcion["Funcion"](opcion["Menu"], opcion["Descripcion"])
        # seleccionamos de nuestras opciones mediante su desciocion
        elif seleccion in [opcion["Descripcion"] for opcion in opcionesMenuPrincipal.values()]:
            for clave, opcion in opcionesMenuPrincipal.items():
                if opcion["Descripcion"] == seleccion:
                    opcion["Funcion"](
                        opcion["Menu"], opcion["Descripcion"])
                    break
        # si la opcion es 1 mas que la lista
        elif seleccion == str(len(opcionesMenuPrincipal) + 1):
            print("Finalizando programa")
            # finaliza el programa
            break
        else:
            print("Opcion invalida. Por favor, selecciona nuevamente.")

# funcion para alta de datos Manual
def VotacionAltaManual():
    print("Alta Votacion Manual")
    MensajeVolverAtras()
    element = {}
    dato = input("Por Favor, Ingrese el DNI del Votante => ")
    if dato == "Volver" or dato == "volver atras" or dato == "VOLVER ATRAS" or dato == "volveratras" or dato == "VOLVERATRAS":
        return
    while str(dato).isdigit() and 0 < int(dato) <= 99999999 or ValidacionDNI(dato):
        if dato == "Volver" or dato == "volver atras" or dato == "VOLVER ATRAS" or dato == "volveratras" or dato == "VOLVERATRAS":
            return
        if ValidacionDNI(dato):
            print("Este Votante ya ha realizado todas ha relizado todos sus votos.")
        else:
            print("DNI Invalido")
        dato = input("Por Favor, Ingrese el DNI del Votante => ")

    element["new"] = {"Dni": dato}

    datoVotos = ValidacionVotosPrevios()
    if datoVotos != {}:
        print("Provincia Elegida")
    else:
        dato = input("Por Favor, Ingrese la Provincia del Votante => ")
        if dato == "Volver" or dato == "volver atras" or dato == "VOLVER ATRAS" or dato == "volveratras" or dato == "VOLVERATRAS":
            return

    print("Cargos Disponibles")
    allOptions = True
    for cargo in opcionesCargos:
        find = False
        for voto in datoVotos.items():
            if cargo["Key"] == voto["Cargo"]:
                find = True
                allOptions = False
                break
        if find == False:
            print(str(cargo["Key"]) + ")", cargo["Descripcion"])
    if allOptions == False:
        print(
            "Si no ve alguna Opcion significa que Votante ya ha realizado un voto para ese cargo")
    dato = input("Por Favor,  => ")


# Mostrar Opciones Menu Principal


def MostrarOpcionesMenuPrincipal():
    for opcion, Funcion in opcionesMenuPrincipal.items():
        print(f"{opcion}) {Funcion['Descripcion']}")
    print(f"{len(opcionesMenuPrincipal) + 1}) Salir")

# Mostrar Opciones Menu Parametrizacion
def MostrarOpcionesMenuParametrizacion():
    for opcion, Funcion in opcionesMenuParametrizacion.items():
        print(f"{opcion}) {Funcion['Descripcion']}")
    print(f"{len(opcionesMenuPrincipal) + 1}) Salir")

# Mostrar Opciones Menu DescargaArchivos
def MostrarOpcionesMenuDescargaArchivos():
    for opcion, Funcion in opcionesMenuDescargaArchivos.items():
        print(f"{opcion}) {Funcion['Descripcion']}")
    print(f"{len(opcionesMenuPrincipal) + 1}) Salir")

# Mostrar Opciones Menu Generico
def MostrarOpcionesMenu(menu):
    for opcion, Funcion in menu.items():
        print(f"{opcion}) {Funcion['Descripcion']}")
    print(f"{len(menu) + 1}) Volver")
    print(f"{len(menu) + 2}) Menu Principal")

# Funcion para confirmacion de datos
def EjecutarConfirmacion(si="Confirmar", no="Cancelar"):
    retorno = None
    while retorno == None:
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
def ValidacionUnicamenteTexto(texto):
    textoSinEspacios = texto.replace(" ", "")
    return textoSinEspacios.isalpha()

# Funcion Descargar Partidos politicos
def DecargarPartidosPoliticos():
    print("Descargado Partidos Politicos...")
    deDondeVengo = "Partidos Politicos"
    listaATrabajar = datosDeCadaLista[deDondeVengo]["Lista"]
    WritePartidosPoliticos(listaATrabajar)
    ParametrizacionVer()

# Funcion Descargar Regiones Geograficas
def DecargarRegionesGeograficas():
    print("Descargado Regiones Geograficas...")
    deDondeVengo = "Regiones Geograficas"
    listaATrabajar = datosDeCadaLista[deDondeVengo]["Lista"]
    WriteRegionesGeograficas(listaATrabajar)
    ParametrizacionVer()

# Funcion para no tener que repetir el mismo mensaje permitiendo cambiar facilmente
def MensajeErrorValidacion(dato, campo, tipo):
    if tipo == "Modificar":
        print(
            campo, "Invalido, Recuerde si quiere Mantener la Informacion deje el Campo en Blanco")
        dato = input("Por Favor, Ingrese el " + campo + " nuevamente =>")
    else:
        dato = input(campo+" Invalido, Ingrese el " +
                        campo + " nuevamente => ")
    return dato

# Funcion para no tener que repetir el mismo mensaje permitiendo cambiar facilmente
# Si se equivoca multiples veces mostrar Recordatorio

def MensajeVolverAtras(cantidad=0):
    if cantidad == 0:
        print(
            "Ingrese 'Volver Atras' en cualquier momento si desea Regresar al Menu anterior.")
    elif cantidad == 3:
        print("Recuerde que Ingresando 'Volver Atras' Regresara al Menu anterior.")
    cantidad += 1
    return cantidad

# Funcion para verificar si esta el elemento en la lista, claveElemento es para si son iguales permitirmos continuar el proceso
def VerificarRepetidos(lista, dato, claveElemento="", campo=""):
    for clave, opcion in lista.items():
        if campo == "":
            if str(clave) == str(claveElemento):
                return True
        else:
            if str(opcion[campo]) == str(dato).upper():
                if str(clave) == claveElemento or opcion["Nombre"] == claveElemento:
                    return False
                else:
                    return True
    return False

# funcion para validar cada dato d e las altas
def ValidacionesCampo(dato, campo, tipo, claveElemento=""):
    # global deDondeVengo
    flag = False
    if deDondeVengo == "Partidos Politicos":
        if campo == "Nombre":
            while dato == "" or VerificarRepetidos(listaPartidosPoliticos, dato, claveElemento, "Nombre"):
                if dato == "" and tipo == "Modificar":
                    break
                if VerificarRepetidos(listaPartidosPoliticos, dato, claveElemento, "Nombre") == True:
                    print("Este Nombre ya pertence a un Partido")
                dato = MensajeErrorValidacion(dato, campo, tipo)
                dato = str(dato).upper()
            dato = dato.upper()
        elif campo == "Abreviatura":
            while (not dato.isalpha()) or len(dato) != 3 or VerificarRepetidos(listaPartidosPoliticos, dato, claveElemento, "Abreviatura"):
                if dato == "" and tipo == "Modificar":
                    break
                if VerificarRepetidos(listaPartidosPoliticos, dato, claveElemento, "Abreviatura") == True:
                    print("Esta Abreviatura ya pertence a un Partido")
                dato = MensajeErrorValidacion(dato, campo, tipo)
                dato = str(dato).upper()
            dato = dato.upper()
        elif campo == "Lista":
            while flag == False:
                if dato == "" and tipo == "Modificar":
                    break
                elif str(dato).isdigit():
                    dato = int(dato)
                    if 0 < dato <= 999:
                        if VerificarRepetidos(listaPartidosPoliticos, dato, claveElemento, "Lista") == False:
                            flag = True
                        else:
                            print("Este Numero ya pertence a un Partido")
                # no cambiar a elif
                if flag == False:
                    dato = MensajeErrorValidacion(dato, campo, tipo)

    elif deDondeVengo == "Regiones Geograficas":
        if campo == "Nombre":
            while flag == True:
                while (not ValidacionUnicamenteTexto(dato)) or dato == "":
                    if dato == "" and tipo == "Modificar":
                        break
                    dato = MensajeErrorValidacion(dato, campo, tipo)
                dato = dato.upper()
                flag = VerificarRepetidos(
                    listaProvincias, dato, claveElemento, "Nombre")
                if flag == True:
                    if tipo == "Modificar":
                        print(
                            "Provincia ya Existente, Recuerde si quiere Mantener la Informacion deje el Campo en Blanco")
                        dato = input("Por Favor, Ingrese el " +
                                        campo + " nuevamente => ")
                    else:
                        dato = input(
                            "Provincia ya Existente, Ingrese el " + campo + " nuevamente => ")
        elif campo == "Codigo":
            while flag == False:
                if dato == "" and tipo == "Modificar":
                    break
                if VerificarRepetidos(listaProvincias, dato, claveElemento, "Codigo") == False:
                    flag = True
                else:
                    print("Este Codigo ya pertence a una Provincia")
                    dato = MensajeErrorValidacion(dato, campo, tipo)
    return dato

# Funcion que redirige a la funcion de alta espesifica
def ParametrizacionAlta():
    # global deDondeVengo
    opciones = datosDeCadaLista[deDondeVengo]["ElementosSolicitar"]
    listaATrabajar = datosDeCadaLista[deDondeVengo]["Lista"]
    elemento = {}
    print("Alta", deDondeVengo)
    MensajeVolverAtras()
    for campo in opciones:
        dato = input("Ingrese " + campo + " => ")
        if dato == "Volver Atras" or dato == "volver atras" or dato == "VOLVER ATRAS" or dato == "volveratras" or dato == "VOLVERATRAS":
            return
        else:
            elemento[campo] = ValidacionesCampo(dato, campo, "Alta")

    if listaATrabajar == {}:
        clave = 1
    else:
        clave = max(listaATrabajar.keys()) + 1
    textoEscribir = ""
    totalElementos = len(elemento)
    indiceActual = 0
    for propiedad, valor in elemento.items():
        indiceActual += 1
        textoEscribir += str(propiedad) + ": " + str(valor)
        if indiceActual != totalElementos:
            textoEscribir += " / "
    print(str(clave) + ")", textoEscribir)

    confirmacion = EjecutarConfirmacion()
    if confirmacion == True:
        listaATrabajar[clave] = elemento
        print(deDondeVengo, "Registrado Existosamente")
    else:
        print(deDondeVengo, "No Registrado")

# Funcion que suplanta al find
def BuscarElementoLista(dato, listaATrabajar):
    encontrado = None
    mostrarMensajeVolverAtras = 0
    while encontrado == None:
        if dato == "Volver Atras" or dato == "volver atras" or dato == "VOLVER ATRAS" or dato == "volveratras" or dato == "VOLVERATRAS": 
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
            mostrarMensajeVolverAtras = MensajeVolverAtras(
                mostrarMensajeVolverAtras)
            dato = input(
                "No se ha Encontrado el Campo, Por Favor Ingrese Nuevamente => ")
    return encontrado

# Funcion Parametrizacion Baja
def ParametrizacionBaja():
    # global deDondeVengo
    print("Baja", deDondeVengo)
    ParametrizacionVer()
    dato = input("Ingrese el elemento a Eliminar => ")
    if dato == "Volver Atras" or dato == "volver atras" or dato == "VOLVER ATRAS" or dato == "volveratras" or dato == "VOLVERATRAS":
        return
    listaATrabajar = datosDeCadaLista[deDondeVengo]["Lista"]
    dato = BuscarElementoLista(dato, listaATrabajar)

    elemento = listaATrabajar[dato]
    textoEscribir = ""
    totalElementos = len(elemento)
    indiceActual = 0
    for propiedad, valor in elemento.items():
        indiceActual += 1
        textoEscribir += str(propiedad) + ": " + str(valor)
        if indiceActual != totalElementos:
            textoEscribir += " / "
    print(str(dato) + ")", textoEscribir)

    confirmacion = EjecutarConfirmacion()
    if confirmacion == True:
        del listaATrabajar[dato]
        print("Registrado Eliminado Existosamente")
    else:
        print("Registrado No Eliminado")

# Funcion Parametrizacion Modificar
def ParametrizacionModificar():
    # global deDondeVengo
    print("Modificacion", deDondeVengo)
    print("¿Desea Ver las Opciones?")

    if EjecutarConfirmacion("Si", "No") == True:
        ParametrizacionVer()
    MensajeVolverAtras()

    dato = input("Ingrese el campo a Modificar => ")
    if dato == "Volver Atras" or dato == "volver atras" or dato == "VOLVER ATRAS" or dato == "volveratras" or dato == "VOLVERATRAS":
        return

    listaATrabajar = datosDeCadaLista[deDondeVengo]["Lista"]
    encontrado = BuscarElementoLista(dato, listaATrabajar)

    opciones = datosDeCadaLista[deDondeVengo]["ElementosSolicitar"]
    elemento = {}

    for campo in opciones:
        dato = input("Ingrese " + campo + " => ")
        if dato == "Volver Atras" or dato == "volver atras" or dato == "VOLVER ATRAS" or dato == "volveratras" or dato == "VOLVERATRAS":
            return
        else:
            elemento[campo] = ValidacionesCampo(
                dato, campo, "Modificar", encontrado)

    if dato == "Volver Atras" or dato == "volver atras" or dato == "VOLVER ATRAS" or dato == "volveratras" or dato == "VOLVERATRAS":
        return

    clave = max(listaATrabajar.keys()) + 1

    textoEscribir = ""
    totalElementos = len(elemento)
    indiceActual = 0
    for propiedad, valor in elemento.items():
        indiceActual += 1
        textoEscribir += str(propiedad) + ": " + str(valor)
        if indiceActual != totalElementos:
            textoEscribir += " / "
    print("Nuevo Elemento)", textoEscribir)

    confirmacion = EjecutarConfirmacion()

    if confirmacion == True:
        del listaATrabajar[encontrado]
        listaATrabajar[clave] = elemento
        print("Cambio Registrado")
    else:
        print("Cambio No Registrado")

# Funcion Parametrizacion Ver
def ParametrizacionVer():
    # global deDondeVengo
    lista = None
    if deDondeVengo == "Partidos Politicos":
        lista = listaPartidosPoliticos
    elif deDondeVengo == "Regiones Geograficas":
        lista = listaProvincias

    valorOpcion = 0
    if lista != None:
        print(deDondeVengo)
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
        print("No hay", deDondeVengo, "Cargadas")
    input("Pulse Enter para Continuar ")

# Funcion menu Generico
def MenuGenerico(menu, titulo):
    salir = False
    global salirAlMenuPrincipal
    global deDondeVengo
    while salir == False and salirAlMenuPrincipal == False:
        deDondeVengo = titulo
        tituloMostrar = "Menu " + titulo
        print(tituloMostrar)
        # mostramos opciones
        MostrarOpcionesMenu(menu)

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
            salirAlMenuPrincipal = True
            # finaliza el programa
            break
        else:
            print("Opcion invalida. Por favor, selecciona nuevamente.")

def ValidacionDNI(dni):
    cantidad = 0
    for element in Votos:
        if element["Dni"] == dni:
            cantidad += 1
    if cantidad <= 4:
        return True
    else:
        return False

def ValidacionVotosPrevios(dni):
    elements = {}
    for element in Votos:
        if element["Dni"] == dni:
            elements[element["Key"]] = element["Value"]
    return elements

def WriteRegionesGeograficas(info):
    if info != None:
        # print("RegionesGeograficas of Model")
        f = open(filereg, 'w', encoding='UTF-8')

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

def WritePartidosPoliticos(info):
    if info != None:
        # print("Partidos Políticos of Model")
        f = open(filepartpol, 'w', encoding='UTF-8')

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

def WriteArchivoVotacion(info):
    if info != None:
        f = open(filevotacion, 'w', encoding='UTF-8')

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

# Diccionario de opciones y Funciones asociadas opciones del ABM
opcionesABM = {
    "1": {"Descripcion": "Alta", "Funcion": ParametrizacionAlta},
    "2": {"Descripcion": "Baja", "Funcion": ParametrizacionBaja},
    "3": {"Descripcion": "Modificar", "Funcion": ParametrizacionModificar},
    "4": {"Descripcion": "Ver", "Funcion": ParametrizacionVer}
}

opcionesCargos = {
    "1": {"Descripcion": "Presidente y Vicepresidente"},
    "2": {"Descripcion": "Diputado"},
    "3": {"Descripcion": "Senador"},
    "4": {"Descripcion": "Gobernador y Vicegobernador"}
}
# Diccionario de opciones y Funciones asociadas Menu Parametizacion
opcionesMenuParametrizacion = {
    "1": {"Descripcion": "Partidos Politicos", "Funcion": MenuGenerico, "Menu": opcionesABM},
    "2": {"Descripcion": "Regiones Geograficas", "Funcion": MenuGenerico, "Menu": opcionesABM}
}

# Diccionario de opciones y Funciones asociadas Menu Descarga Archivos
opcionesMenuDescargaArchivos = {
    "1": {"Descripcion": "Partidos Politicos", "Funcion": DecargarPartidosPoliticos},
    "2": {"Descripcion": "Regiones Geograficas", "Funcion": DecargarRegionesGeograficas}
}

opcionesMenuDescargaArchivos = {
    "1": {"Descripcion": "Partidos Politicos", "Funcion": DecargarPartidosPoliticos},
    "2": {"Descripcion": "Regiones Geograficas", "Funcion": DecargarRegionesGeograficas}
}

opcionesMenuVotacionAlta = {
    "1": {"Descripcion": "Automatica", "Funcion": temporal},
    "2": {"Descripcion": "SemiAutomatica", "Funcion": temporal},
    "3": {"Descripcion": "Manual", "Funcion": VotacionAltaManual}
}

opcionesMenuVotacion = {
    "1": {"Descripcion": "Alta Nuevos Votos", "Funcion": MenuGenerico, "Menu": opcionesMenuVotacionAlta},
    "2": {"Descripcion": "Ver Porcentajes", "Funcion": temporal}
}

opcionesMenuPrincipal = {
    "1": {"Descripcion": "Parametrizacion", "Funcion": MenuGenerico, "Menu": opcionesMenuParametrizacion},
    "2": {"Descripcion": "Descarga de Archivos", "Funcion": MenuGenerico, "Menu": opcionesMenuDescargaArchivos},
    "3": {"Descripcion": "Votacion", "Funcion": MenuGenerico, "Menu": opcionesMenuVotacion}
}

Votos = {}

# Diccionario de partidos politicos la clave es el numero y el resto son sus datos (nombre abreviatura)
listaPartidosPoliticos = {
}

# Diccionario de provincias la clave es un numero autoincremental y su nombre
listaProvincias = {
}

datosDeCadaLista = {
    "Partidos Politicos": {"ElementosSolicitar": ["Nombre", "Abreviatura", "Lista"], "Lista": listaPartidosPoliticos},
    "Regiones Geograficas": {"ElementosSolicitar": ["Nombre", "Codigo"], "Lista": listaProvincias}

}
main()