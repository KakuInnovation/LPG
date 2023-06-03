import random
filereg = 'db/regiones.csv'
filepartpol = 'db/partidos.csv'


def main():
    # funcion para alta de votos Manual
    def VotacionAltaManual():
        global deDondeVengo
        print("Alta Votacion Manual")
        MensajeVolverAtras()
        element = {}
        dato = input("Por Favor, Ingrese el DNI del Votante => ")
        if dato.lower() in {"volver", "volver atras"}:
            return
        while not str(dato).isdigit() or not 0 < int(dato) <= 999999999 or not ValidacionDNI(dato):
            if dato.lower() in {"volver", "volver atras"}:
                return
            if ValidacionDNI(dato):
                print("Este Votante ya ha realizado todas ha relizado todos sus votos.")
            else:
                print("DNI Invalido")
            dato = input("Por Favor, Ingrese el DNI del Votante => ")

        element["Dni"] = str(dato)

        datoVotos = ValidacionVotosPrevios(dato)
        if datoVotos != {}:
            print("Provincia Elegida")
            element["Provincia"] = next(iter(datoVotos.values()))["Provincia"]
        else:
            deDondeVengo = "Regiones Geograficas"
            ParametrizacionVer()
            deDondeVengo = "Alta Nuevos Votos"
            dato = input("Por Favor, Ingrese la Provincia del Votante => ")
            if dato.lower() in {"volver", "volver atras"}:
                return
            while not (dato in listaProvincias.keys()):
                if dato.lower() in {"volver", "volver atras"}:
                    return
                dato = input(
                    "Opcion Incorrecta, por Favor Seleccione un Provincia Valida = >")
            element["Provincia"] = str(dato)

        print("Cargos Disponibles:")
        allOptions = True
        for cargo in opcionesCargos:
            find = False
            for voto in datoVotos.items():
                if cargo == voto[1]["Cargo"]:
                    find = True
                    allOptions = False
                    break
            if not find:
                print(str(cargo) + ")", opcionesCargos[cargo]["Descripcion"])
        if allOptions == False:
            print(
                "Si no ve alguna Opcion significa que Votante ya ha realizado un voto para ese cargo")
        dato = input("Por Favor,  Ingrese un cargo => ")
        if dato.lower() in {"volver", "volver atras"}:
            return
        while not (dato in opcionesCargos.keys()) and not (dato in [opcion["Cargo"] for opcion in datoVotos.values()]):
            if dato.lower() in {"volver", "volver atras"}:
                return
            dato = input(
                "Opcion Incorrecta, por Favor Seleccione un cargo => ")
        element["Cargo"] = str(dato)

        deDondeVengo = "Partidos Politicos"
        ParametrizacionVer(True)
        deDondeVengo = "Alta Nuevos Votos"
        dato = input("Por Favor, Ingrese el Partido Politico del Votante => ")
        if dato.lower() in {"volver", "volver atras"}:
            return
        while not (dato in listaPartidosPoliticos.keys()) and not str(dato) == "0":
            if dato.lower() in {"volver", "volver atras"}:
                return
            dato = input(
                "Opcion Incorrecta, por Favor Seleccione un Partido Politico Valido => ")
        element["Partido"] = str(dato)

        if votos == {}:
            clave = 1
        else:
            clave = max(votos.keys()) + 1

        textoEscribir = ""
        totalElementos = len(element)
        indiceActual = 0
        for propiedad, valor in element.items():
            indiceActual += 1
            textoEscribir += str(propiedad) + ": " + str(valor)
            if indiceActual != totalElementos:
                textoEscribir += " / "
        print(str(clave) + ")", textoEscribir)

        confirmacion = EjecutarConfirmacion()
        if confirmacion == True:
            votos[clave] = element
            print(deDondeVengo, "Registrado Existosamente")
        else:
            print(deDondeVengo, "No Registrado")

    # funcion para alta de votos Automatica
    def VotacionAltaAutomatica():
        cantRegistros = input("Por favor, Ingrese la Cantidad de Votos => ")
        while not str(cantRegistros).isdigit():
            if cantRegistros.lower() in {"volver", "volver atras"}:
                return
            cantRegistros = input(
                "Numero invalido, por favor Ingrese la Cantidad de Votos Nuevamente")

        global deDondeVengo
        for i in range(int(cantRegistros)):
            element = {}
            dato = str(random.randint(1, 999999999))
            while not str(dato).isdigit() or not 0 < int(dato) <= 999999999 or not ValidacionDNI(dato):
                dato = str(random.randint(1, 999999999))
            element["Dni"] = str(dato)

            datoVotos = ValidacionVotosPrevios(dato)
            if datoVotos != {}:
                element["Provincia"] = next(
                    iter(datoVotos.values()))["Provincia"]
            else:
                dato = random.choice(list(listaProvincias.keys()))
                element["Provincia"] = str(dato)

            while not dato in opcionesCargos.keys() and not (dato in [opcion["Cargo"] for opcion in datoVotos.values()]):
                dato = random.choice(list(opcionesCargos.keys()))
            element["Cargo"] = str(dato)

            dato = str(random.randint(0, len(listaPartidosPoliticos)))
            if dato != "0":
                claves = list(listaPartidosPoliticos.keys())
                dato = claves[int(dato) - 1]

            element["Partido"] = str(dato)

            if votos == {}:
                clave = 1
            else:
                clave = max(votos.keys()) + 1

            textoEscribir = ""
            totalElementos = len(element)
            indiceActual = 0
            for propiedad, valor in element.items():
                indiceActual += 1
                textoEscribir += str(propiedad) + ": " + str(valor)
                if indiceActual != totalElementos:
                    textoEscribir += " / "
            print(str(clave) + ")", textoEscribir)

            votos[clave] = element

    # funcion para alta de votos Automatica
    def VotacionAltaAutomaticaSegundaVuelta(balotaje):
        # INGRESA LA CANTIDAD DE VOTOS POR PANTALLA DE SELECCIÓN
        cantRegistros = input("Por favor, Ingrese la Cantidad de Votos => ")
# Valida que se ingrese un número
        while not str(cantRegistros).isdigit():
            if cantRegistros.lower() in {"volver", "volver atras"}:
                return
            cantRegistros = input(
                "Numero invalido, por favor Ingrese la Cantidad de Votos Nuevamente")

#        global deDondeVengo

# Se tiene en cuenta sólo los partidos del balotaje
        listaPartidosPoliticosSegundaVuelta = {}
        listaPartidosPoliticosSegundaVuelta = balotaje

        for i in range(int(cantRegistros)):
            element = {}
            votoNoPermitido = True

# Si no es numérico negativo o DNI duplicado
            while votoNoPermitido == True:
                dato = str(random.randint(1, 999999999))
                votoNoPermitido = ValidacionVotosSegundaVuelta(dato)
            element["Dni"] = str(dato)

            datoVotos = ValidacionVotosPrevios(dato)
            if datoVotos != {}:
                element["Provincia"] = next(
                    iter(datoVotos.values()))["Provincia"]
            else:
                dato = random.choice(list(listaProvincias.keys()))
                element["Provincia"] = str(dato)

# Selecciona al azar un Cargo - SÓLAMENTE APLICA A PRESIDENTE Y VICEPRESIDENTE
            while not dato in opcionesCargosSegundaVuelta.keys() and not (dato in [opcion["Cargo"] for opcion in datoVotos.values()]):
                dato = random.choice(list(opcionesCargosSegundaVuelta.keys()))
            element["Cargo"] = str(dato)

            dato = str(random.randint(
                0, len(listaPartidosPoliticosSegundaVuelta)))
            if dato != "0":
                claves = list(listaPartidosPoliticosSegundaVuelta.keys())
                dato = claves[int(dato) - 1]

            element["Partido"] = str(dato)

            if votos == {}:
                clave = 1
            else:
                clave = max(votos.keys()) + 1

            textoEscribir = ""
            totalElementos = len(element)
            indiceActual = 0
            for propiedad, valor in element.items():
                indiceActual += 1
                textoEscribir += str(propiedad) + ": " + str(valor)
                if indiceActual != totalElementos:
                    textoEscribir += " / "
            print(str(clave) + ")", textoEscribir)

            votosSegundaVuelta[clave] = element

    # Funcion para mostrar los porcentajes

    def PorcentajeVotacion(esDescarga=False):
        if len(votos) == 0:
            print("Aun no hay Votos Cargados")
            input("Pulse Enter para Continuar ")
            return None

        global deDondeVengo
        deDondeVengo = "Regiones Geograficas"
        ParametrizacionVer()
        MensajeVolverAtras()
        provincia = input("Por Favor, Seleccione una Provincia => ")
        if provincia.lower() in {"volver", "volver atras"}:
            return
        while not (provincia in listaProvincias.keys()):
            if provincia.lower() in {"volver", "volver atras"}:
                return
            provincia = input(
                "Opcion Incorrecta, por Favor Seleccione un Provincia Valida => ")

        deDondeVengo = "Opciones Cargos"
        ParametrizacionVer()
        cargo = input("Por Favor, Seleccione un Cargos => ")
        if cargo.lower() in {"volver", "volver atras"}:
            return
        while not (cargo in opcionesCargos.keys()):
            if cargo.lower() in {"volver", "volver atras"}:
                return
            cargo = input(
                "Opcion Incorrecta, por Favor Seleccione un Cargos Valido => ")

        votosTotales = 0
        elements = {}
        for clave, partido in listaPartidosPoliticos.items():
            element = {}
            element["Partido"] = partido["Nombre"]
            element["PartidoCodigo"] = clave
            element["Cantidad Votos"] = 0
            elements[clave] = element

        if len(elements) != 0:
            element = {}
            element["Partido"] = "VOTO EN BLANCO"
            element["PartidoCodigo"] = "0"
            element["Cantidad Votos"] = 0
            elements["0"] = element

        for clave, element in votos.items():
            if str(element["Provincia"]) == str(provincia) and str(element["Cargo"]) == str(cargo):
                for clave2, element2 in elements.items():
                    if str(clave2) == str(element["Partido"]):
                        element2["Cantidad Votos"] += 1
                        break

                votosTotales += 1

        if votosTotales == 0:
            print("No hay Votos con esta Combinacion")
            input("Pulse Enter para Continuar ")
            return None
        cargoTexto = opcionesCargos.get(
            str(cargo), {}).get("Descripcion", None)
        provinciaTexto = listaProvincias.get(
            str(provincia), {}).get("Nombre", None)

        elements = MuestraYCalculoDePorcentajes(
            elements, votosTotales, cargoTexto, provinciaTexto)

        if esDescarga == False:
            input("Pulse Enter para Continuar ")
            return
        else:
            element = {}
            element["Provincia"] = provinciaTexto
            element["ProvinciaCodigo"] = str(provincia)
            element["Cargo"] = cargoTexto
            elements["DatosNombreArchivo"] = element
            return elements

    # Funcion para mostrar los porcentajes Presidencia de todaas las provincias
    def PorcentajeVotacionPresidencia(esDescarga=False):
        if len(votos) == 0:
            print("Aun no hay Votos Cargados")
            input("Pulse Enter para Continuar ")
            return None

        global deDondeVengo
        cargo = "1"
        votosTotales = 0
        elements = {}
        for clave, partido in listaPartidosPoliticos.items():
            element = {}
            element["Partido"] = partido["Nombre"]
            element["PartidoCodigo"] = clave
            element["Cantidad Votos"] = 0
            elements[clave] = element

        if len(elements) != 0:
            element = {}
            element["Partido"] = "VOTO EN BLANCO"
            element["Cantidad Votos"] = 0
            element["PartidoCodigo"] = "0"
            elements["0"] = element

        for clave, element in votos.items():
            if str(element["Cargo"]) == cargo:
                for clave2, element2 in elements.items():
                    if str(clave2) == str(element["Partido"]):
                        element2["Cantidad Votos"] += 1
                        break

                votosTotales += 1

        if votosTotales == 0:
            print("No hay Votos para Presidencia Aun")
            input("Pulse Enter para Continuar ")
            return None
        cargoTexto = opcionesCargos.get(
            str(cargo), {}).get("Descripcion", None)

        elements = MuestraYCalculoDePorcentajes(
            elements, votosTotales, cargoTexto)

        if esDescarga == False:
            input("Pulse Enter para Continuar ")
            return
        else:
            element = {}
            element["Provincia"] = "Nacionales"
            element["ProvinciaCodigo"] = "Nacionales"
            element["Cargo"] = cargoTexto
            elements["DatosNombreArchivo"] = element
            return elements

    def PorcetajeSegundaVuelta(esDescarga=False):
        votosTotales = 0
        elements = {}
        for clave, partido in listaPartidosPoliticos.items():
            element = {}
            element["Partido"] = partido["Nombre"]
            element["PartidoCodigo"] = clave
            element["Cantidad Votos"] = 0
            elements[clave] = element

        if len(elements) != 0:
            element = {}
            element["Partido"] = "VOTO EN BLANCO"
            element["Cantidad Votos"] = 0
            element["PartidoCodigo"] = "0"
            elements["0"] = element

        for clave, element in votosSegundaVuelta.items():
            for clave2, element2 in elements.items():
                if str(clave2) == str(element["Partido"]):
                    element2["Cantidad Votos"] += 1
                    break

            votosTotales += 1

        if votosTotales == 0:
            print("No hay Votos para Presidencia Aun")
            input("Pulse Enter para Continuar ")
            return None
        cargoTexto = opcionesCargos.get(
            str("1"), {}).get("Descripcion", None)

        elements = MuestraYCalculoDePorcentajes(
            elements, votosTotales, cargoTexto)

        if esDescarga == False:
            input("Pulse Enter para Continuar ")
            return
        else:
            element = {}
            element["Provincia"] = "Nacionales"
            element["ProvinciaCodigo"] = "Nacionales"
            element["Cargo"] = cargoTexto
            elements["DatosNombreArchivo"] = element
            return elements

    def MuestraYCalculoDePorcentajes(elements, votosTotales, cargoTexto, provinciaTexto="Nacionales"):
        print("Region:", provinciaTexto)
        print("---------------------------------------------------------------------------------------------------------------")
        print("Elecciones Generales 2023")
        print("---------------------------------------------------------------------------------------------------------------")
        print("Categoria:", cargoTexto)
        print("---------------------------------------------------------------------------------------------------------------")
        cantidadVotosEnBlanco = elements.get(
            ("0"), {}).get("Cantidad Votos", None)
        porcentajeEnBlanco = cantidadVotosEnBlanco * 100 / votosTotales
        porcentajePositivo = 100-porcentajeEnBlanco

        porcentajeEnBlanco = "{:.2f}".format(porcentajeEnBlanco)
        porcentajePositivo = "{:.2f}".format(porcentajePositivo)

        votosPais = len(votos)
        votosPais = votosTotales * 100 / votosPais
        votosPais = "{:.2f}".format(votosPais)

        print("Electrores Habilitados:", votosTotales,
              "/ Porcentaje de Votos Totales:", votosPais + "%")
        print("---------------------------------------------------------------------------------------------------------------")
        elements = dict(
            sorted(elements.items(), key=lambda x: x[1]["Cantidad Votos"], reverse=True))
        index = 1
        for clave, element in elements.items():
            porcentaje = element["Cantidad Votos"] * 100 / votosTotales
            porcentaje = "{:.2f}".format(porcentaje) + "%"
            if clave != "0":
                print(str(index) + ")", element["Partido"] + ":",
                      porcentaje, "con", element["Cantidad Votos"], "Votos")
                index += 1
            element["Porcentaje"] = porcentaje
        print("---------------------------------------------------------------------------------------------------------------")
        print("Votos Positivos:", votosTotales -
              cantidadVotosEnBlanco, "/", porcentajePositivo + "%")
        print("Votos En Blanco:", cantidadVotosEnBlanco,
              "/", porcentajeEnBlanco + "%")
        print("Votos Totales:", votosTotales, "/", "100%")
        return elements

    # Mostrar Opciones Menu Principal
    def MostrarOpcionesMenuPrincipal():
        for opcion, Funcion in opcionesMenuPrincipal.items():
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
        print("1)", si)
        print("0)", no)

        while True:
            seleccion = input("Por favor, selecciona una opción => ").strip()

            if seleccion == "1" or seleccion == si:
                return True
            elif seleccion == "0" or seleccion == no:
                return False
            else:
                print("Opción inválida. Por favor, selecciona nuevamente.")

    # verificamos si no hay simbolos
    def ValidacionUnicamenteTexto(texto):
        textoSinEspacios = texto.replace(" ", "")
        return textoSinEspacios.isalpha()

    # Funcion Descargar Partidos politicos
    def DecargarPartidosPoliticos():
        print("Descargado Partidos Politicos...")
        listaATrabajar = datosDeCadaLista["Partidos Politicos"]["Lista"]
        WritePartidosPoliticos(listaATrabajar)
        global deDondeVengo
        deDondeVengo = "Partidos Politicos"
        ParametrizacionVer()

    # Funcion Descargar Regiones Geograficas
    def DecargarRegionesGeograficas():
        print("Descargado Regiones Geograficas...")
        listaATrabajar = datosDeCadaLista["Regiones Geograficas"]["Lista"]
        WriteRegionesGeograficas(listaATrabajar)
        global deDondeVengo
        deDondeVengo = "Regiones Geograficas"
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
                "Ingrese 'Volver Atras' o 'Volver'en cualquier momento si desea Regresar al Menu anterior.")
        elif cantidad == 3:
            print(
                "Recuerde que Ingresando 'Volver Atras' o 'Volver' Regresara al Menu anterior.")
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

    def VerficacionSegundaVuelta(info, esdescarga=False):
        index = 1
        for clave, reg in info.values():
            if clave != 0:
                if index == 1:
                    partido1 = reg
                    index += 1
                elif index == 2:
                    partido2 = reg
                    break
        partido1Porcentaje = partido1["Porcentaje"][:-1]
        partido1Porcentaje = float(partido1["Porcentaje"][:-1])
        partido2Porcentaje = float(partido2["Porcentaje"][:-1])

        diferencia = partido1Porcentaje - partido2Porcentaje
        if diferencia < 0:
            diferencia *= -1

        if diferencia > 5 and partido1Porcentaje > 40:
            print(f"El partido", partido1["Partido"],
                  "ha ganado las elecciones")
            print("No es Necesaria Segunda Vuelta")
            input("Pulse Enter para Continuar ")
        elif diferencia > 5 and partido1Porcentaje > 40:
            print(f"El partido", partido2["Partido"],
                  "ha ganado las elecciones")
            print("No es Necesaria Segunda Vuelta")
            input("Pulse Enter para Continuar ")
        else:
            if votosSegundaVuelta != {}:
                print("Mostrar quien gano")
            else:
                print(f"Los partidos", partido1["Partido"],
                      "y", partido2["Partido"], "iran a Balotage")
                input("Presione Enter para Continuar")

                VotacionAltaAutomaticaSegundaVuelta({partido1, partido2})
                resultadoSegundaVuelta = PorcetajeSegundaVuelta()

        # if float(partido1["Porcentaje"])

    # funcion para validar cada dato d e las altas

    def ValidacionesCampo(dato, campo, tipo, claveElemento=""):
        global deDondeVengo
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
        global deDondeVengo
        opciones = datosDeCadaLista[deDondeVengo]["ElementosSolicitar"]
        listaATrabajar = datosDeCadaLista[deDondeVengo]["Lista"]
        elemento = {}
        print("Alta", deDondeVengo)
        MensajeVolverAtras()
        for campo in opciones:
            dato = input("Ingrese " + campo + " => ")
            if dato.lower() in {"volver", "volver atras"}:
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
            if dato.lower() in {"volver", "volver atras"}:
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
        global deDondeVengo
        print("Baja", deDondeVengo)
        ParametrizacionVer()
        dato = input("Ingrese el elemento a Eliminar => ")
        if dato.lower() in {"volver", "volver atras"}:
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
        global deDondeVengo
        print("Modificacion", deDondeVengo)
        print("¿Desea Ver las Opciones?")

        if EjecutarConfirmacion("Si", "No") == True:
            ParametrizacionVer()
        MensajeVolverAtras()

        dato = input("Ingrese el campo a Modificar => ")
        if dato.lower() in {"volver", "volver atras"}:
            return

        listaATrabajar = datosDeCadaLista[deDondeVengo]["Lista"]
        encontrado = BuscarElementoLista(dato, listaATrabajar)

        opciones = datosDeCadaLista[deDondeVengo]["ElementosSolicitar"]
        elemento = {}

        for campo in opciones:
            dato = input("Ingrese " + campo + " => ")
            if dato.lower() in {"volver", "volver atras"}:
                return
            else:
                elemento[campo] = ValidacionesCampo(
                    dato, campo, "Modificar", encontrado)

        if dato.lower() in {"volver", "volver atras"}:
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
    def ParametrizacionVer(votacion=False):
        global deDondeVengo
        lista = None
        if deDondeVengo == "Partidos Politicos":
            lista = listaPartidosPoliticos
        elif deDondeVengo == "Regiones Geograficas":
            lista = listaProvincias
        elif deDondeVengo == "Opciones Cargos":
            lista = opcionesCargos

        if lista != None:
            print(deDondeVengo)
            for clave, obj in lista.items():
                textoEscribir = ""
                totalElementos = len(obj)
                indiceActual = 0
                for propiedad, valor in obj.items():
                    indiceActual += 1
                    textoEscribir += str(propiedad) + ": " + str(valor)
                    if indiceActual != totalElementos:
                        textoEscribir += " / "
                print(str(clave) + ")", textoEscribir)
        else:
            print("No hay", deDondeVengo, "Cargadas")
        if votacion == True:
            print("0) Voto en Blanco")
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
        for clave, element in votos.items():
            if str(element["Dni"]) == str(dni):
                cantidad += 1
        if cantidad <= 4:
            return True
        else:
            return False

    def ValidacionVotosPrevios(dni):
        elements = {}
        for clave, element in votos.items():
            if str(element["Dni"]) == str(dni):
                elements[clave] = votos[clave]
        return elements

    def ValidacionVotosSegundaVuelta(dni):
        for clave, element in votosSegundaVuelta.items():
            if str(element["Dni"]) == str(dni):
                return True
        return False

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

    def getInfoArchivoVotacionRegional():
        print("Descargado Votaciones...")
        info = PorcentajeVotacion(True)
        WriteArchivoVotacion(info)

    def getInfoArchivoVotacionPresidencia():
        print("Descargado Votaciones...")
        info = PorcentajeVotacionPresidencia(True)
        WriteArchivoVotacion(info)
        if info != None:
            VerficacionSegundaVuelta(info, True)

    def getPorcentajeVotacionPresidencia():
        info = PorcentajeVotacionPresidencia(True)
        if info != None:
            VerficacionSegundaVuelta(info)

    def WriteArchivoVotacion(info):
        if info != None:
            datosTexto = ""
            datosTexto = (info.get("DatosNombreArchivo", {}).get(
                "Provincia", "") + info.get("DatosNombreArchivo", {}).get("Cargo", ""))
            provinciaCodigo = info.get(
                "DatosNombreArchivo", {}).get("ProvinciaCodigo", "")
            del info["DatosNombreArchivo"]

            filevotacion = 'db/votacion' + str(datosTexto)+'.csv'
            f = open(filevotacion, 'w', encoding='UTF-8')

            try:
                for reg in info.values():
                    if reg["PartidoCodigo"] != "0":
                        registro = provinciaCodigo + ";" + \
                            reg["PartidoCodigo"] + ";" + \
                            str(reg["Cantidad Votos"]) + \
                            ";" + reg["Porcentaje"] + "\n"
                        str(registro)
                        f.write(registro)
            except:
                print("Error al escribir el Archivo")
            finally:
                f.close()
                input("Pulse Enter para Continuar ")
                print("Archivo Generado")

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

# Aplica el Diccionario sólo para la segunda vuelta
    opcionesCargosSegundaVuelta = {
        "1": {"Descripcion": "Presidente y Vicepresidente"}
    }

    # Diccionario de opciones y Funciones asociadas Menu Parametizacion
    opcionesMenuParametrizacion = {
        "1": {"Descripcion": "Partidos Politicos", "Funcion": MenuGenerico, "Menu": opcionesABM},
        "2": {"Descripcion": "Regiones Geograficas", "Funcion": MenuGenerico, "Menu": opcionesABM}
    }

    # Diccionario de opciones y Funciones asociadas Menu Descarga Archivos
    opcionesMenuDescargaArchivos = {
        "1": {"Descripcion": "Partidos Politicos", "Funcion": DecargarPartidosPoliticos},
        "2": {"Descripcion": "Regiones Geograficas", "Funcion": DecargarRegionesGeograficas},
        "3": {"Descripcion": "Votaciones",  "Funcion": WriteArchivoVotacion}
    }

    listaPartidosPoliticos1 = {
        "1": {"Nombre": "FRENTE DE TODOS", "Abreviatura": "FDT", "Lista": "1"},
        "2": {"Nombre": "JUNTOS POR EL CAMBIO", "Abreviatura": "JXC", "Lista": "2"},
        "3": {"Nombre": "LIBERTRAIOS", "Abreviatura": "LIB", "Lista": "3"},
        "4": {"Nombre": "PERONISMO FEDERAL", "Abreviatura": "PFE", "Lista": "4"},
        "5": {"Nombre": "FRENTE DE IZQUIERDA", "Abreviatura": "FDI", "Lista": "5"},
        "6": {"Nombre": "LIBRES DEL SUR", "Abreviatura": "LBS", "Lista": "6"},
    }

    opcionesMenuVotacionAlta = {
        "1": {"Descripcion": "Automatica", "Funcion": VotacionAltaAutomatica},
        "2": {"Descripcion": "Manual", "Funcion": VotacionAltaManual}
    }

    opcionesEscrutino = {
        "1": {"Descripcion": "Ver Porcentajes Por Region", "Funcion": PorcentajeVotacion},
        "2": {"Descripcion": "Ver Porcentaje Presidencial Nacional", "Funcion": getPorcentajeVotacionPresidencia},
        "3": {"Descripcion": "Descargar Votacion Por Region", "Funcion": getInfoArchivoVotacionRegional},
        "4": {"Descripcion": "Descargar Votacion Presidencial Nacional Primera Vuelta", "Funcion": getInfoArchivoVotacionPresidencia}
    }

    opcionesMenuPrincipal = {
        "1": {"Descripcion": "Parametrizacion", "Funcion": MenuGenerico, "Menu": opcionesMenuParametrizacion},
        "2": {"Descripcion": "Descarga de Archivos de Parametrizacion", "Funcion": MenuGenerico, "Menu": opcionesMenuDescargaArchivos},
        "3": {"Descripcion": "Alta de Votos", "Funcion": MenuGenerico, "Menu": opcionesMenuVotacionAlta},
        "4": {"Descripcion": "Escrutinio", "Funcion": MenuGenerico, "Menu": opcionesEscrutino}
    }

    votos = {}
    votosSegundaVuelta = {}

    # Diccionario de partidos politicos la clave es el numero y el resto son sus datos (nombre abreviatura)
    listaPartidosPoliticos = {
        "1": {"Nombre": "FRENTE DE TODOS", "Abreviatura": "FDT", "Lista": "1"},
        "2": {"Nombre": "JUNTOS POR EL CAMBIO", "Abreviatura": "JXC", "Lista": "2"},
        "3": {"Nombre": "LIBERTRAIOS", "Abreviatura": "LIB", "Lista": "3"},
        "4": {"Nombre": "PERONISMO FEDERAL", "Abreviatura": "PFE", "Lista": "4"},
        "5": {"Nombre": "FRENTE DE IZQUIERDA", "Abreviatura": "FDI", "Lista": "5"},
        "6": {"Nombre": "LIBRES DEL SUR", "Abreviatura": "LBS", "Lista": "6"},
    }

    # Diccionario de provincias la clave es un numero autoincremental y su nombre
    listaProvincias = {
        "1": {"Nombre": "CABA", "Codigo": "1"},
        "2": {"Nombre": "BUENOS AIRES", "Codigo": "2"},
        "3": {"Nombre": "CATAMARCA", "Codigo": "3"},
        "4": {"Nombre": "CHACO", "Codigo": "4"},
        "5": {"Nombre": "CHUBUT", "Codigo": "5"},
        "6": {"Nombre": "CORDOBA", "Codigo": "6"},
        "7": {"Nombre": "CORRIENTES", "Codigo": "7"},
        "8": {"Nombre": "ENTRE RIOS", "Codigo": "8"},
        "9": {"Nombre": "FORMOSA", "Codigo": "9"},
        "10": {"Nombre": "JUJUY", "Codigo": "10"},
        "11": {"Nombre": "LA PAMPA", "Codigo": "11"},
        "12": {"Nombre": "LA RIOJA", "Codigo": "12"},
        "13": {"Nombre": "MENDOZA", "Codigo": "13"},
        "14": {"Nombre": "MISIONES", "Codigo": "14"},
        "15": {"Nombre": "NEUQUEN", "Codigo": "15"},
        "16": {"Nombre": "RIO NEGRO", "Codigo": "16"},
        "17": {"Nombre": "SALTA", "Codigo": "17"},
        "18": {"Nombre": "SAN JUAN", "Codigo": "18"},
        "19": {"Nombre": "SAN LUIS", "Codigo": "19"},
        "20": {"Nombre": "SANTA CRUZ", "Codigo": "20"},
        "21": {"Nombre": "SANTA FE", "Codigo": "21"},
        "22": {"Nombre": "SANTIAGO DEL ESTERO", "Codigo": "22"},
        "23": {"Nombre": "TIERRA DEL FUEGO", "Codigo": "23"},
        "24": {"Nombre": "TUCUMAN", "Codigo": "24"}
    }

    datosDeCadaLista = {
        "Partidos Politicos": {"ElementosSolicitar": ["Nombre", "Abreviatura", "Lista"], "Lista": listaPartidosPoliticos},
        "Regiones Geograficas": {"ElementosSolicitar": ["Nombre", "Codigo"], "Lista": listaProvincias}
    }

    while True:
        global salirAlMenuPrincipal
        global deDondeVengo
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


main()
