
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

#Pedir Partido politico
def AltaPartidoPolitico():
    print("Ingrese 'Volver Atras' si desea volver al Menu Principal")
    nombre = input("Ingrese el nombre del partido => ")
    while (not EsTextoValido(nombre)) or nombre == "":
        print("Nombre invalido, ingrese el nombre nuevamente")
        nombre = input("Ingrese el nombre del partido => ")
    
    abreviatura = input("Ingrese la abreviatura del Partido => ")
    while (not abreviatura.isalpha()) or len(abreviatura) != 3:
        print("Abreviatura invalida, ingrese la abreviatura nuevamente")
        abreviatura = input("Ingrese la abreviatura del partido => ")    
    
    numeroValido = False
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



#funcion menu Descarga Archivos
def MostrarMenuGenerico(menu, titulo):
    salir = False
    global salirAlMenuPrincipal
    while salir == False and salirAlMenuPrincipal == False:
        tituloMostrar="Menu " + titulo
        print(tituloMostrar)
        #mostramos opciones
        MostrarOpcionesMenu(menu)

        #solicitamos opcion
        seleccion = input("Por favor, selecciona una opción => ")

        #si la seleccion esta en nuestras opciones la eleguimos
        if seleccion in menu:
            opcion = menu[seleccion]
            if "menu" in opcion:
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

# Diccionario de opciones y funciones asociadas Menu Parametizacion
opcionesMenuParametrizacion= {
    "1": {"descripcion": "Partidos Políticos", "funcion": MostrarMenuGenerico, "menu":opcionesABM},
    "2": {"descripcion": "Regiones Geográficas", "funcion": MostrarMenuGenerico, "menu":opcionesABM}
}

# Diccionario de opciones y funciones asociadas Menu Principal
opcionesMenuPrincipal = {
    "1": {"descripcion": "Parametrización", "funcion": MostrarMenuGenerico, "menu":opcionesMenuParametrizacion},
    "2": {"descripcion": "Descarga de Archivos", "funcion": MostrarMenuGenerico, "menu":opcionesMenuDescargaArchivos}
}



#funcion del menu principal
while True:
    global salirAlMenuPrincipal
    if 'salirAlMenuPrincipal' in globals():
        if salirAlMenuPrincipal != False:
            print("Bienvenido al Sistema de Elecciones Presidenciales")
    salirAlMenuPrincipal = False

    #mostramos opciones
    MostrarOpcionesMenuPrincipal()

    #solicitamos opcion
    seleccion = input("Por favor, selecciona una opción => ")

    #si la seleccion esta en nuestras opciones la eleguimos
    if seleccion in opcionesMenuPrincipal:
        opcion = opcionesMenuPrincipal[seleccion]
        opcion["funcion"](opcion["menu"],opcion["descripcion"])  # Llama a la función correspondiente
    #si la opcion es 1 mas que la lista 
    elif seleccion == str(len(opcionesMenuPrincipal) + 1):
        print("Finalizando programa")
        #finaliza el programa
        break
    else:
        print("Opción inválida. Por favor, selecciona nuevamente.")

