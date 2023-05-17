
#Mostrar Opciones Menu Principal
def MostrarOpcionesMenuPrincipal():
    for opcion, funcion in opcionesMenuPrincipal.items():
        print(f"{opcion}) {funcion['descripcion']}")
    print(f"{len(opcionesMenuPrincipal) + 1}) Salir")

def MostrarOpcionesMenu(menu):
    for opcion, funcion in menu.items():
        print(f"{opcion}) {funcion['descripcion']}")
    print(f"{len(menu) + 1}) Volver")
    print(f"{len(menu) + 2}) Menu Principal")

def EjecutarConfirmacion():
    retorno = 0
    while retorno == 0:
        print("1) Confirmar")
        print("0) Cancelar")
        seleccion = input("Por favor, selecciona una opción => ")
        if seleccion == "1" or seleccion == "Confirmar":
            retorno = True
        elif seleccion == "0" or seleccion == "Cancelar":
            retorno = False
        else:
            print("Opción inválida. Por favor, selecciona nuevamente.")
    return retorno

#Pedir Partido politico
def AltaPartidoPolitico():
    print("Ingrese 'Volver Atras' en cualquier momenento si desea Regresar")
    nombre = input("Ingrese el nombre del partido => ")

    if nombre == "Volver Atras":
        return

    while (not EsTextoValido(nombre)) or nombre == "":
        print("Nombre invalido, ingrese el nombre nuevamente")
        nombre = input("Ingrese el nombre del partido => ")
    
    abreviatura = input("Ingrese la abreviatura del Partido => ")

    if abreviatura == "Volver Atras":
        return

    while (not abreviatura.isalpha()) or len(abreviatura) != 3:
        print("Abreviatura invalida, ingrese la abreviatura nuevamente")
        abreviatura = input("Ingrese la abreviatura del partido => ")    
    
    numeroValido = False
    if abreviatura == "Volver Atras":
        return

    while not numeroValido:
        numPartido = input("Ingrese el número del partido => ")
        if numPartido.isdigit():
            numPartido = int(numPartido)    
            if 0 < numPartido <= 999:
                numeroValido = True
            else:
                print("Número de partido inválido, ingrese el número nuevamente")
        else:
            print("Entrada inválida, ingrese un número entero válido")
    
    print("¿Desea confirmar esta información?")
    print("Nombre del partido ", nombre, "Abreviatura ", abreviatura, "Número ", numPartido)

    confirmacion = EjecutarConfirmacion() 
    if confirmacion == True:
        listaPartidosPoliticos[numPartido] = {"nombre": nombre, "abreviatura": abreviatura}
        print("Partido registrado correctamente")
    else:
        print("Partido no registrado")

    
def EsTextoValido(texto):
    textoSinEspacios = texto.replace(" ", "")
    return textoSinEspacios.isalpha()

#funcion Descargar Partidos políticos
def DecargarPartidosPoliticos():
    print("Descargado")

#funcion Descargar Regiones Geográficas
def DecargarRegionesGeograficas():
    print("Descargado")

#funcion Parametrizacion Alta
def ParametrizacionAlta():
    print("parametrizacionAlta")

#funcion Parametrizacion Baja
def ParametrizacionBaja():
    print("parametrizacionBaja")

#funcion Parametrizacion Alta
def ParametrizacionModificar():
    print("parametrizacionModificar")

#funcion Parametrizacion Alta
def ParametrizacionVer():
    print("parametrizacionVer")

#funcion menu Generico
def MenuGenerico(menu, titulo):
    salir = False
    global salirAlMenuPrincipal
    while salir == False and salirAlMenuPrincipal == False:
        tituloMostrar="Menu " + titulo
        print(tituloMostrar)
        #mostramos opciones
        MostrarOpcionesMenu(menu)

        #solicitamos opcion
        seleccion = input("Por favor, selecciona una opción => ")

        #seleccionamos de nuestras opciones mediante su clave
        if seleccion in menu:
            opcion = menu[seleccion]
            if "menu" in opcion or seleccion in [opcion["descripcion"] for opcion in opcionesMenuPrincipal.values()]:
                opcion["funcion"](opcion["menu"],opcion["descripcion"])  # Llama a la función correspondiente
            else:
                opcion["funcion"]()  # Llama a la función correspondiente1
            salir = False

        elif seleccion in [opcion["descripcion"] for opcion in menu.values()]:
            for clave, opcion in menu.items():
                if opcion["descripcion"] == seleccion:
                    if "menu" in opcion or seleccion in [opcion["descripcion"] for opcion in opcionesMenuPrincipal.values()]:
                        opcion["funcion"](opcion["menu"],opcion["descripcion"])  # Llama a la función correspondiente
                    else:
                        opcion["funcion"]()  # Llama a la función correspondiente1
                    salir = False

        #si la opcion es 1 mas que la lista 
        elif seleccion == str(len(menu) + 1):
            salir = True
            #finaliza el programa
            break
        elif seleccion == str(len(menu) + 2):
            salirAlMenuPrincipal = True
            #finaliza el programa
            break
        else:
            print("Opción inválida. Por favor, selecciona nuevamente.")

# Diccionario de opciones y funciones asociadas Menu Descarga Archivos
opcionesMenuDescargaArchivos = {
    "1": {"descripcion": "Partidos Políticos", "funcion": DecargarPartidosPoliticos},
    "2": {"descripcion": "Regiones Geográficas", "funcion": DecargarRegionesGeograficas}
}

# Diccionario de opciones y funciones asociadas opciones del ABM
opcionesABM = {
    "1": {"descripcion": "Alta", "funcion": AltaPartidoPolitico},
    "2": {"descripcion": "Baja", "funcion": ParametrizacionBaja},
    "3": {"descripcion": "Modificar", "funcion": ParametrizacionModificar},
    "4": {"descripcion": "Ver", "funcion": ParametrizacionVer}
}

# Diccionario de partidos politicos la clave es el numero y el resto son sus datos (nombre abreviatura)
listaPartidosPoliticos = {}

# Diccionario de opciones y funciones asociadas Menu Parametizacion
opcionesMenuParametrizacion= {
    "1": {"descripcion": "Partidos Políticos", "funcion": MenuGenerico, "menu":opcionesABM},
    "2": {"descripcion": "Regiones Geográficas", "funcion": MenuGenerico, "menu":opcionesABM}
}

# Diccionario de opciones y funciones asociadas Menu Principal
opcionesMenuPrincipal = {
    "1": {"descripcion": "Parametrización", "funcion": MenuGenerico, "menu":opcionesMenuParametrizacion},
    "2": {"descripcion": "Descarga de Archivos", "funcion": MenuGenerico, "menu":opcionesMenuDescargaArchivos}
}



#funcion del menu principal
while True:
    #definimos esta variable como global para que pueda ser consumida por cualquier funcion
    global salirAlMenuPrincipal
    #verifiacmos que la variable ya existe o todavia no tiene un valor (es decir la primera vez que se ejecuta el codigo)
    if 'salirAlMenuPrincipal' in globals():
        if salirAlMenuPrincipal != False:
            print("Bienvenido al Sistema de Elecciones Presidenciales")
    salirAlMenuPrincipal = False

    #mostramos opciones
    MostrarOpcionesMenuPrincipal()

    #solicitamos opcion
    seleccion = input("Por favor, selecciona una opción => ")

    #seleccionamos de nuestras opciones mediante su clave
    if seleccion in opcionesMenuPrincipal:
        opcion = opcionesMenuPrincipal[seleccion] #buscamos la opcion seleccionada
        opcion["funcion"](opcion["menu"],opcion["descripcion"])  # Llama a la función correspondiente
    #seleccionamos de nuestras opciones mediante su desciocion
    elif seleccion in [opcion["descripcion"] for opcion in opcionesMenuPrincipal.values()]:
        for clave, opcion in opcionesMenuPrincipal.items():
            if opcion["descripcion"] == seleccion:
                opcion["funcion"](opcion["menu"], opcion["descripcion"])
                break
    #si la opcion es 1 mas que la lista 
    elif seleccion == str(len(opcionesMenuPrincipal) + 1):
        print("Finalizando programa")
        #finaliza el programa
        break
    else:
        print("Opción inválida. Por favor, selecciona nuevamente.")

