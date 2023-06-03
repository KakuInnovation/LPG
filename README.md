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
- Para mejorar la UX (experencia de usuario), hemos mejorado la funcionlidad de corte de ingreso de datos (ingresar "FIN"), por un menu dinamico y amigable para el usuario
- En Archivos Generados ya se encuentrar los archivos de salida solicitados, y en caso de querer generarlos estos se veran en la carpeta del proyecto en la carpeta db
- Al no usar librerias y ni objetos contamos con un problema de relentizacion que empieza a notrarse con los 10000 votos, debido a la cantidad masiva de registros que cargamos sobre una misma variable. Una posible solucion seria hacer diccionario de los votos es decir, un diccionario donde esten todas las provincias y luego dentro de las provincias un segundo donde esten los cargos como un diccionario con sus votos. No hemos pudido llegar a desarrollar esto por falta de tiempo.
- No se aclara en la funcionalidad si el voto en blanco debe ser añadido al archivo, nosotros lo hemos añadido y se ordena automaticamente tambien.
- Hemos acortado los porcentajes de las votaciones a 2 decimales.
- Es muy posible por un error en nuestro diseño las probilidades de voto en blanco sean mas alta a la realidad.
- Una vez realizado el Balotaje (Segunda vuelta) no se podra agregar mas Votos.


## Funcionamiento
- Menus: Nuestro Programa esta usando menus de consola para acceder a todas las funcionalidad. 
    Este funciona de la siguente manera:
        - Tenemos un bucle inicial que mientras este activo va a hacer que el programa este activo al terminarse finaliza el programa
        - Las opciones de menu se crear con bibliotecas con valor especificos para asi poder ser llamadas correctamente
        - Se realizan los calculos correspondientes para obtener el porcentaje de votos de los respectivos partidos politicos y su print y comparacion con los otros partido politicos
        - Se integro la funcionalidad de carga automatica de votos con su respectiva validacion que permite al usuario ingresar N votos con un rango entre 0 y 999.999.999
        - Se agregaron validaciones y modificaciones a los inputs que permiten al usuario flexibilidad a la hora de manejarse dentro del programa y menues
        - El usuario tambien puede subir su propio voto y tambien puede descargar tanto los votos subidos por el usuario como los creados por el programa
            - Clave: es un numero de nuestra opcion
            - Valores:
                - descripcion: valor que va a ser el titulo de nuestra opcion y tambien puede ser elegida como opcion
                - funcion: es la funcion asociada, es decir que va a ser nuestro codigo cuando esta opcion va a ser elegida en caso de que sea otro menu se llamara a la funcion MenuGenerico y se pasara en parametros correspondientes
                - menu: este es obligatorio si esta la funcion MenuGenerico creada, aqui se pone el diccionario de el menu correspondiente
        - Para acceder a un sub menu tenemos la funcion MenuGenerico. Esta funcion lo que hace es empezar ciclos dentro de nuestro ciclo principal para representar cada menu correspondiente. Tambien se puede llamar MenuGenerico dentro de un MenuGenerico para ingresar a un siguiente menu, ejemplo: menuPrincial>Parametrizacion>Alta. Al Finzalizar una opcion (por ejemplo: alta partido) esta volvera a su menu anterior correspondiente. En caso de pulsar "Atras" esto finalizara el ciclo actual y regresa al ciclo anterior. Si se pone la variable "salirAlMenuPrincipal" como verdadera esta volvera al menu principal directamente finalizando todos los demas ciclos.
    Las opciones del menu pueden ser accedidas mediante su descipcion o su clave.
    Ventajas: Facil de ampliar, reutilizacion de funciones.
    Desventajas: Mayor consumo de Memoria (ya que los bucles quedan abiertos), estructura compleja .

-Partido Politicos: Suponemos que las abreviaturas de los partidos son 3 letras y su numero va desde el 1 al 999 y tambien que es su clave.

- Estructura del Programa:
    -Inicia en un menu principal donde tenemos:
        -Parametrizacion: donde podemos dar de Alta, Modificacion, Baja y Ver (ABM) los partidos politicos y regiones
        -Descarga de Archivos de Parametrizacion: donde nos permite descargar los archivos de parametrizacion y ver asi sus datos
        -Alta de votos: aqui podemos simular la creacion de votos, aqui no contamos con Modificacion, Baja ni Ver para simular un funcionamiento mas realista. Aunque si mostramos el voto al momento de la carga para tener de registro.
            -Manual: Permite simular de forma manual toda la carga de un voto y confirmarlo para subirlo
            -Automatica: Establecemos una cantidad de votos y se generan automaticamente. 
            Adevertencia: 
        -Escrutinio: Aqui podemos ver y descargar los resultados de las votaciones. Tambien hemos sumado para que se pueda ver las elecciones presidenciales de todas las provincias y la ciudad de Buenos Aires