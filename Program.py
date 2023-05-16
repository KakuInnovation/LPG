#Mostrar Opciones Menu Principal
def mostrarOpcionesMenuPrincipal():
    for opcion, funcion in opcionesMenuPrincipal.items():
        print(f"{opcion}) {funcion['descripcion']}")
    print(f"{len(opcionesMenuPrincipal) + 1}) Salir")

def mostrarOpcionesMenu(menu):
    for opcion, funcion in menu.items():
        print(f"{opcion}) {funcion['descripcion']}")
    print(f"{len(menu) + 1}) Volver")

#funcion Descargar Partidos políticos
def decargarPartidosPoliticos():
    print("Descargado")

#funcion Descargar Regiones Geográficas
def decargarRegionesGeograficas():
    print("Descargado")

#funcion Parametrizacion Alta
def parametrizacionAlta():
    print("parametrizacionAlta")

#funcion Parametrizacion Baja
def parametrizacionBaja():
    print("parametrizacionBaja")

#funcion Parametrizacion Alta
def parametrizacionModificar():
    print("parametrizacionModificar")

#funcion Parametrizacion Alta
def parametrizacionVer():
    print("parametrizacionVer")



#funcion menu Descarga Archivos
def mostrarMenuGenerico(menu, titulo):
    salir = False
    while salir == False:
        tituloMostrar="Menu " + titulo
        print(tituloMostrar)
        #mostramos opciones
        mostrarOpcionesMenu(menu)

        #solicitamos opcion
        seleccion = input("Por favor, selecciona una opción => ")

        #si la seleccion esta en nuestras opciones la eleguimos
        if seleccion in menu:
            opcion = menu[seleccion]
            if "Menu" in opcion:
                opcion["funcion"](opcion["menu"],opcion["descripcion"])  # Llama a la función correspondiente
            else:
                opcion["funcion"](seleccion)  # Llama a la función correspondiente1

            
            salir = False

        #si la opcion es 1 mas que la lista 
        elif seleccion == str(len(menu) + 1):
            print("Volver Atras")
            salir = True
            #finaliza el programa
            break
        else:
            print("Opción inválida. Por favor, selecciona nuevamente.")

# Diccionario de opciones y funciones asociadas Menu Descarga Archivos
opcionesMenuDescargaArchivos = {
    "1": {"descripcion": "Partidos Políticos", "funcion": decargarPartidosPoliticos},
    "2": {"descripcion": "Regiones Geográficas", "funcion": decargarRegionesGeograficas}
}

# Diccionario de opciones y funciones asociadas opciones del ABM
opcionesABM = {
    "1": {"descripcion": "Alta", "funcion": parametrizacionAlta},
    "2": {"descripcion": "Baja", "funcion": parametrizacionBaja},
    "3": {"descripcion": "Modificar", "funcion": parametrizacionModificar},
    "4": {"descripcion": "Ver", "funcion": parametrizacionVer}
}

# Diccionario de opciones y funciones asociadas Menu Parametizacion
opcionesMenuParametrizacion= {
    "1": {"descripcion": "Partidos Políticos", "funcion": mostrarMenuGenerico, "menu":opcionesABM},
    "2": {"descripcion": "Regiones Geográficas", "funcion": mostrarMenuGenerico, "menu":opcionesABM}
}

# Diccionario de opciones y funciones asociadas Menu Principal
opcionesMenuPrincipal = {
    "1": {"descripcion": "Parametrización", "funcion": mostrarMenuGenerico, "menu":opcionesMenuParametrizacion},
    "2": {"descripcion": "Descarga de Archivos", "funcion": mostrarMenuGenerico, "menu":opcionesMenuDescargaArchivos}
}

print("Bienvenido al Sistema de Elecciones Presidenciales")
#funcion del menu principal
while True:
    #mostramos opciones
    mostrarOpcionesMenuPrincipal()

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
