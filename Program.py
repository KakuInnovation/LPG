#Mostrar Opciones Menu Principal
def MostrarOpcionesMenuPrincipal():
    for opcion, Funcion in opcionesMenuPrincipal.items():
        print(f"{opcion}) {Funcion['Descripcion']}")
    print(f"{len(opcionesMenuPrincipal) + 1}) Salir")

def MostrarOpcionesMenu(menu):
    for opcion, Funcion in menu.items():
        print(f"{opcion}) {Funcion['Descripcion']}")
    print(f"{len(menu) + 1}) Volver")
    print(f"{len(menu) + 2}) Menu Principal")

#Funcion para confirmacion de datos
def EjecutarConfirmacion():
    retorno = 0
    while retorno == 0:
        print("1) Confirmar")
        print("0) Cancelar")
        seleccion = input("Por favor, selecciona una opcion => ")
        if seleccion == "1" or seleccion == "Confirmar":
            retorno = True
        elif seleccion == "0" or seleccion == "Cancelar":
            retorno = False
        else:
            print("Opcion invalida. Por favor, selecciona nuevamente.")
    return retorno

#verificamos si no hay simbolos
def ValidacionUnicamenteTexto(texto):
    textoSinEspacios = texto.replace(" ", "")
    return textoSinEspacios.isalpha()

#Funcion Descargar Partidos politicos
def DecargarPartidosPoliticos():
    print("Descargado")

#Funcion Descargar Regiones Geograficas
def DecargarRegionesGeograficas():
    print("Descargado")

#Funcion para no tener que repetir el mismo mensaje permitiendo cambiar facilmente
def MensajeErrorValidacion(dato,campo):
    dato = input(campo+" Invalido, Ingrese el "+ campo + " nuevamente =>")
    return dato

#funcion para validar cada dato d e las altas
def ValidacionesCampo(dato, campo):
    global deDondeVengo
    flag = False
    if deDondeVengo == "Partidos Politicos":
        if campo=="Nombre":
            while (not ValidacionUnicamenteTexto(dato)) or dato == "":
                dato = MensajeErrorValidacion(dato,campo)
            dato = dato.upper()
        elif campo == "Abreviatura":
            while (not dato.isalpha()) or len(dato) != 3:
                dato = MensajeErrorValidacion(dato,campo)
            dato = dato.upper() 
        elif campo == "Numero del Partido":
            while flag == False:
                if dato.isdigit():
                    dato = int(dato)
                    if 0 < dato <= 999:
                        encontrado = False
                        for clave, opciones in listaPartidosPoliticos.items():
                            if clave == dato:
                                print("Este numero ya pertence a un partido: ", opciones ["Nombre"]) 
                                dato = input("Por favor Ingrese un Numero nuevamente: ")
                                encontrado == True
                                break
                        if encontrado == False:
                            flag = True
                    else:
                        dato = MensajeErrorValidacion(dato, campo)

                elif flag == False:
                    dato = MensajeErrorValidacion(dato, campo)

    elif deDondeVengo == "Regiones Geograficas":
        if campo == "Nombre":
            while flag == False:
                dato = dato.upper()
                flag = True
                for clave, opcion in listaProvincias.items():
                    if opcion["Nombre"] == dato:
                        flag = False
                if flag == False:
                    dato = input("Provincia ya Existente, Ingrese el "+ campo + " nuevamente =>")
    return dato

#Funcion que redirige a la funcion de alta espesifica
def ParametrizacionAlta():
    global deDondeVengo
    opciones = datosDeCadaLista[deDondeVengo]["ElementosSolicitar"]
    listaATrabajar = datosDeCadaLista[deDondeVengo]["Lista"]
    volverAtras = False
    clave=""
    elemento = {}
    for campo in opciones:
        if volverAtras == False:
            if campo == "ClaveAutoIncrimental":
                clave = len(listaATrabajar) + 1
            else:
                if campo == "Clave":
                    campo = datosDeCadaLista[deDondeVengo]["NombreClave"]
                dato = input("Ingrese " + campo + " => ")
                if dato == "Volver Atras":
                    volverAtras = True
                else:
                    dato = ValidacionesCampo(dato, campo)
                if campo == "Clave":
                    clave = dato
                else:
                    elemento[campo] = dato
    confirmacion = EjecutarConfirmacion() 
    if confirmacion == True:
        listaATrabajar[clave] = elemento
        print(deDondeVengo, "Registrado Correctamente")
    else:
        print(deDondeVengo, "No Registrado")

#Funcion Parametrizacion Baja
def ParametrizacionBaja():
    print("parametrizacionBaja")

#Funcion Parametrizacion Alta
def ParametrizacionModificar():
    print("parametrizacionModificar")

#Funcion Parametrizacion Alta
def ParametrizacionVer():
    global deDondeVengo
    lista = None
    if deDondeVengo == "Partidos Politicos":
        lista = listaPartidosPoliticos
    elif deDondeVengo == "Regiones Geograficas":
        lista = listaProvincias
    
    if lista != None:
        for clave, obj in lista.items():
            textoEscribir = ""
            for propiedad, valor in obj.items():
                textoEscribir += str(propiedad) + " " + str(valor) + " "
            print(str(clave) + ")",textoEscribir)

#Funcion menu Generico
def MenuGenerico(menu, titulo):
    salir = False
    global salirAlMenuPrincipal
    global deDondeVengo
    while salir == False and salirAlMenuPrincipal == False:
        deDondeVengo = titulo
        tituloMostrar="Menu " + titulo
        print(tituloMostrar)
        #mostramos opciones
        MostrarOpcionesMenu(menu)

        #solicitamos opcion
        seleccion = input("Por favor, selecciona una opcion => ")

        #seleccionamos de nuestras opciones mediante su clave
        if seleccion in menu:
            opcion = menu[seleccion]
            if "Menu" in opcion:
                opcion["Funcion"](opcion["Menu"],opcion["Descripcion"])  # Llama a la funcion correspondiente
            else:
                opcion["Funcion"]()  # Llama a la funcion correspondiente1
            salir = False

        elif seleccion in [opcion["Descripcion"] for opcion in menu.values()]:
            for clave, opcion in menu.items():
                if opcion["Descripcion"] == seleccion:
                    if "Menu" in opcion:
                        opcion["Funcion"](opcion["Menu"],opcion["Descripcion"])  # Llama a la funcion correspondiente
                    else:
                        opcion["Funcion"]()  # Llama a la funcion correspondiente1
                    salir = False

        #si la opcion es 1 mas que la lista 
        elif seleccion == str(len(menu) + 1) or seleccion == "Volver":
            salir = True
            #finaliza el programa
            break
        elif seleccion == str(len(menu) + 2) or seleccion == "Menu Principal":
            salirAlMenuPrincipal = True
            #finaliza el programa
            break
        else:
            print("Opcion invalida. Por favor, selecciona nuevamente.")

# Diccionario de opciones y Funciones asociadas Menu Descarga Archivos
opcionesMenuDescargaArchivos = {
    "1": {"Descripcion": "Partidos Politicos", "Funcion": DecargarPartidosPoliticos},
    "2": {"Descripcion": "Regiones Geograficas", "Funcion": DecargarRegionesGeograficas}
}

# Diccionario de opciones y Funciones asociadas opciones del ABM
opcionesABM = {
    "1": {"Descripcion": "Alta", "Funcion": ParametrizacionAlta},
    "2": {"Descripcion": "Baja", "Funcion": ParametrizacionBaja},
    "3": {"Descripcion": "Modificar", "Funcion": ParametrizacionModificar},
    "4": {"Descripcion": "Ver", "Funcion": ParametrizacionVer}
}

# Diccionario de partidos politicos la clave es el numero y el resto son sus datos (nombre abreviatura)
listaPartidosPoliticos = {
    1 :{"Nombre":"PSJ", "Abreviatura":"PSJ" },
    2 :{"Nombre":"AAA", "Abreviatura":"AAA"},
    3 :{"Nombre":"BBB", "Abreviatura":"BBB"},
    4 :{"Nombre":"CCC", "Abreviatura":"CCC"},
    5 :{"Nombre":"DDD", "Abreviatura":"DDD"},
    6 :{"Nombre":"EEE", "Abreviatura":"EEE"},
}

# Diccionario de provincias la clave es un numero autoincremental y su nombre
listaProvincias = {}

datosDeCadaLista = {
    "Partidos Politicos": {"ElementosSolicitar":["Nombre", "Abreviatura", "Clave"], "Lista":listaPartidosPoliticos, "NombreClave": "Numero del Partido"},
    "Regiones Geograficas": {"ElementosSolicitar":["ClaveAutoIncrimental","Nombre"],"Lista":listaProvincias}
}

# Diccionario de opciones y Funciones asociadas Menu Parametizacion
opcionesMenuParametrizacion= {
    "1": {"Descripcion": "Partidos Politicos", "Funcion": MenuGenerico, "Menu":opcionesABM},
    "2": {"Descripcion": "Regiones Geograficas", "Funcion": MenuGenerico, "Menu":opcionesABM}
}

# Diccionario de opciones y Funciones asociadas Menu Principal
opcionesMenuPrincipal = {
    "1": {"Descripcion": "Parametrizacion", "Funcion": MenuGenerico, "Menu":opcionesMenuParametrizacion},
    "2": {"Descripcion": "Descarga de Archivos", "Funcion": MenuGenerico, "Menu":opcionesMenuDescargaArchivos}
}

#Funcion del menu principal
while True:
    #definimos esta variable como global para que pueda ser consumida por cualquier Funcion
    global salirAlMenuPrincipal
    global deDondeVengo
    #verifiacmos que la variable ya existe o todavia no tiene un valor (es decir la primera vez que se ejecuta el codigo)
    if 'salirAlMenuPrincipal' in globals():
        if salirAlMenuPrincipal != False:
            print("Bienvenido al Sistema de Elecciones Presidenciales")
    salirAlMenuPrincipal = False
    deDondeVengo = "MenuPrincipal"
    #mostramos opciones
    MostrarOpcionesMenuPrincipal()

    #solicitamos opcion
    seleccion = input("Por favor, selecciona una opcion => ")

    
    #seleccionamos de nuestras opciones mediante su clave (la hacemos por separado ya que se espera que se ingrese numeros generando asi no tener que recorrer el objeto)
    if seleccion in opcionesMenuPrincipal:
        opcion = opcionesMenuPrincipal[seleccion] #buscamos la opcion seleccionada
        opcion["Funcion"](opcion["Menu"],opcion["Descripcion"])  # Llama a la funcion correspondiente
    #seleccionamos de nuestras opciones mediante su desciocion
    elif seleccion in [opcion["Descripcion"] for opcion in opcionesMenuPrincipal.values()]:
        for clave, opcion in opcionesMenuPrincipal.items():
            if opcion["Descripcion"] == seleccion:
                opcion["Funcion"](opcion["Menu"], opcion["Descripcion"])
                break
    #si la opcion es 1 mas que la lista 
    elif seleccion == str(len(opcionesMenuPrincipal) + 1):
        print("Finalizando programa")
        #finaliza el programa
        break
    else:
        print("Opcion invalida. Por favor, selecciona nuevamente.")

