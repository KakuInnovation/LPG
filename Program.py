#Mostrar Opciones Menu Principal
def mostrarMenuPrincipal():
    print("Menu Principal")
    for opcion, funcion in opcionesMenuPrincipal.items():
        print(f"{opcion}) {funcion['descripcion']}")
    print(f"{len(opcionesMenuPrincipal) + 1}) Salir")

#funcion menu Parametrizacion
def mostrarMenuParametrizacion():
    print("Menu Parametrización")
    seleccion = input("Por favor, selecciona una opción => ")

#funcion menu Descarga Archivos
def mostrarMenuDescargaArchivos():
    print("Menu Descarga de Archivos")
    seleccion = input("Por favor, selecciona una opción => ")

# Diccionario de opciones y funciones asociadas
opcionesMenuPrincipal = {
    "1": {"descripcion": "Parametrización", "funcion": mostrarMenuParametrizacion},
    "2": {"descripcion": "Descarga de Archivos", "funcion": mostrarMenuDescargaArchivos}
}


print("Bienvenido al Sistema de Elecciones Presidenciales")
#funcion del menu principal
while True:
    mostrarMenuPrincipal()

    seleccion = input("Por favor, selecciona una opción => ")

    if seleccion in opcionesMenuPrincipal:
        opcion = opcionesMenuPrincipal[seleccion]
        opcion["funcion"]()  # Llama a la función correspondiente
    elif seleccion == str(len(opcionesMenuPrincipal) + 1):
        print("Finalizando programa")
        break
    else:
        print("Opción inválida. Por favor, selecciona nuevamente.")
