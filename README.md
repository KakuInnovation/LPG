# LPG
UADE Copa Algoritmia 2023

## Desarrollado por:
- Bruno, Gustavo: https://github.com/geb2701S gubruno@uade.edu.ar
- Guerrero, Alejandro: https://github.com/KakuInnovation alguerrero@uade.edu.ar
- Pedemonte, Matias https://github.com/catafrulo mpedemonte@uade.edu.ar
- Roubineau, Augusto: https://github.com/AugstR CRoubineau@uade.edu.ar

## Link del Proyecto
- https://github.com/KakuInnovation/LPG

## Aclaraciones
- El programa debe ejecutarse desde el archivo "PPROGRAM.PY"
- Las estructuras de programación utilizadas son POO - Programación Orientada a Objetos y Funciones.
- Segun entendemos con el mensaje dicho por la VARANDO MARIA EUGENIA entendemos que el tema de cargos, no contemplamos para esta etapa la funcionalidad de cargo ya que esa funcionalidad estaria pensada para la siguente etapa:
- Funcionlidad Pedida: Los cargos a elegir serán presidente y vicepresidente (código 1), diputado (2), senador (3), gobernador y vicegobernador (4). Estos datos no deberán ser ingresados ya que se encuentran preestablecidos. Para simplificar el proceso se omiten cargos de menor nivel como intendentes y concejales.
- Para mejorar la UX (experencia de usuario), hemos mejorado la funcionlidad de corte de ingreso de datos (ingresar "FIN"), por un menu dinamico y amigable para el usuario
- En Archivos Generados ya se encuentrar los archivos de salida solicitados, y en caso de querer generarlos estos se veran en la carpeta del proyecto en la carpeta db

## Funcionamiento
- Menus: Nuestro Programa esta usando menus de consola para acceder a todas las funcionalidad. 
    Este funciona de la siguente manera:
        - Tenemos un bucle inicial que mientras este activo va a hacer que el programa este activo al terminarse finaliza el programa
        - Las opciones de menu se crear con bibliotecas con valor especificos para asi poder ser llamadas correctamente
        - Se realizan los calculos correspondientes para obtener el porcentaje de votos de los respectivos partidos politicos y su print y comparacion con los otros partido politicos
        - Se integro la funcionalidad de carga automatica de votos con su respectiva validacion que permite al usuario ingresar N votos con un rango entre 0 y 999.999.999
        - Se agregaron validaciones y modificaciones a los inputs que permiten al usuario flexibilidad a la hora de manejarse dentro del programa y menues
            - Clave: es un numero de nuestra opcion
            - Valores:
                - descripcion: valor que va a ser el titulo de nuestra opcion y tambien puede ser elegida como opcion
                - funcion: es la funcion asociada, es decir que va a ser nuestro codigo cuando esta opcion va a ser elegida en caso de que sea otro menu se llamara a la funcion MenuGenerico y se pasara en parametros correspondientes
                - menu: este es obligatorio si esta la funcion MenuGenerico creada, aqui se pone el diccionario de el menu correspondiente
        - Para acceder a un sub menu tenemos la funcion MenuGenerico. Esta funcion lo que hace es empezar ciclos dentro de nuestro ciclo principal para representar cada menu correspondiente. Tambien se puede llamar MenuGenerico dentro de un MenuGenerico para ingresar a un siguiente menu, ejemplo: menuPrincial>Parametrizacion>Alta. Al Finzalizar una opcion (por ejemplo: alta partido) esta volvera a su menu anterior correspondiente. En caso de pulsar "Atras" esto finalizara el ciclo actual y regresa al ciclo anterior. Si se pone la variable "salirAlMenuPrincipal" como verdadera esta volvera al menu principal directamente finlizando todos los demas ciclos.
    Las opciones del munu pueden ser accedidas mediante su descipcion o su clave.
    Ventajas: Facil de ampliar, reutilizacion de funciones.
    Desventajas: Mayor consumo de Memoria (ya que los bucles quedan abiertos), estructura compleja .
-Partido Politicos: Suponemos que las abreviaturas de los partidos son 3 letras y su numero va desde el 1 al 999 y tambien que es su clave.
