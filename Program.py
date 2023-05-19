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

#Pedir Partido politico
def AltaPartidoPolitico():
    print("Ingrese 'Volver Atras' en cualquier momenento si desea Regresar")
    nombre = input("Ingrese el nombre del partido => ")

    if nombre == "Volver Atras":
        return

    

    abreviatura = input("Ingrese la abreviatura del Partido => ")

    if abreviatura == "Volver Atras":
        return

    
    
    numeroValido = False
    if abreviatura == "Volver Atras":
        return

    while not numeroValido:
        numPartido = input("Ingrese el numero del partido => ")
        if numPartido.isdigit():
            numPartido = int(numPartido)    
            if 0 < numPartido <= 999:
                numeroValido = True
            else:
                print("Numero de partido invalido, ingrese el numero nuevamente")
        elif numPartido == "Volver Atras":
            return
        else:
            print("Entrada invalida, ingrese un numero entero valido")
    
    print("¿Desea confirmar esta informacion?")
    print("Nombre del partido: " + nombre + ", Abreviatura: " + abreviatura + ", Numero ", str(numPartido))

    confirmacion = EjecutarConfirmacion() 
    if confirmacion == True:
        listaPartidosPoliticos[numPartido] = {"Nombre": nombre, "Abreviatura": abreviatura}
        print("Partido registrado correctamente")
    else:
        print("Partido no registrado")


#verificamos si no hay simbolos
def ValidacionUnicamneteTexto(texto):
    textoSinEspacios = texto.replace(" ", "")
    return textoSinEspacios.isalpha()

#Funcion Descargar Partidos politicos
def DecargarPartidosPoliticos():
    print("Descargado")

#Funcion Descargar Regiones Geograficas
def DecargarRegionesGeograficas():
    print("Descargado")

def ValidacionesCampo(dato, campo):
    global deDondeVengo
    if deDondeVengo == "Partidos Politicos":
        if campo=="Nombre":
            while (not ValidacionUnicamneteTexto(dato)) or dato == "":
                dato = input(campo," Invalido, Ingrese el", campo, "nuevamente")
            dato = dato.upper()
        elif campo == "Abreviatura":
            while (not dato.isalpha()) or len(dato) != 3:
                dato = input(campo," Invalido, Ingrese el", campo, "nuevamente")
            dato = dato.upper() 
    elif deDondeVengo == "Regiones Geograficas":
        print("aun no")
    return dato
        

#Funcion que redirige a la funcion de alta espesifica
def ParametrizacionAlta():
    global deDondeVengo
    if deDondeVengo == "Partidos Politicos":
        AltaPartidoPolitico()
    elif deDondeVengo == "Regiones Geograficas":
        AltaPartidoPolitico()

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

datosDeCadaLista = {
    "Partidos Politicos": ["Nombre", "Abreviatura", "Clave"],
    "Regiones Geograficas": ["ClaveAutoIncrimental","Nombre"] 
}

# Diccionario de partidos politicos la clave es el numero y el resto son sus datos (nombre abreviatura)
listaPartidosPoliticos = {}

# Diccionario de provincias la clave es un numero autoincremental y su nombre
listaProvincias = {}

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

    #seleccionamos de nuestras opciones mediante su clave
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

