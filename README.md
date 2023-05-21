# LPG
UADE Copa Algoritmia 2023

## Desarrollado por:
- Bruno, Gustavo: https://github.com/geb2701S gubruno@uade.edu.ar
- Guerrero, Alejandro: https://github.com/KakuInnovation alguerrero@uade.edu.ar
- Pedemonte, Matias https://github.com/catafrulo
- Roubineau, Augusto: https://github.com/AugstR CRoubineau@uade.edu.ar
- Voutsina, Luciano: https://github.com/1UCHQ LVoutsina@uade.edu.ar

## Link del Proyecto
- https://github.com/KakuInnovation/LPG

## Aclaraciones
- El programa debe ejecutarse desde el archivo "CONTROLLER.PY"
- Para un correcto orden en el código, buscando escalabilidad y simplicidad para el mantenimiento, utilizamos el patron de diseño MVC - Model - View - Controller.
- Las estructuras de programación utilizadas son POO - Programación Orientada a Objetos y Funciones.
- Segun entendemos con el mensaje dicho por la VARANDO MARIA EUGENIA entendemos que el tema de cargos, no contemplamos para esta etapa la funcionalidad de cargo ya que esa funcionalidad estaria pensada para la siguente etapa:
    - Funcionlidad Pedida: Los cargos a elegir serán presidente y vicepresidente (código 1), diputado (2), senador (3), gobernador y vicegobernador (4). Estos datos no deberán ser ingresados ya que se encuentran preestablecidos. Para simplificar el proceso se omiten cargos de menor nivel como intendentes y concejales.
    - Mensaje: Hola Ivan buenas tardes, la idea de la primera etapa es que generen los datos con los que van a trabajar el resto de las etapas. En este caso tienen que generar los procesos repetitivos correspondientes con sus respectivas validaciones para lograr ingresar el conjunto de los datos con los que vamos a trabajar. En esta etapa se les pide que estos datos queden guardados en archivos CSV (texto plano donde cada uno de los campos dentro del registro queda separado por - ; - (punto y coma). En esta primera estapa NO HAY VOTACION. 
- Para mejorar la UX (experencia de usuario), hemos mejorado la funcionlidad de corte de ingreso de datos (ingresar "FIN"), por un menu dinamico y amigable para el usuario

## Funcionamiento
- Menus: Nuestro Programa esta usando menus de consola para acceder a todas las funcionalidad. 
    Este funciona de la siguente manera:
        - Tenemos un bucle inicial que mientras este activo va a hacer que el programa este activo al terminarse finaliza el programa
        - Las opciones de menu se crear con bibliotecas con valor especificos para asi poder ser llamadas correctamente
            - Clave: es un numero de nuestra opcion
            - Valores:
                - descripcion: valor que va a ser el titulo de nuestra opcion y tambien puede ser elegida como opcion
                - funcion: es la funcion asociada, es decir que va a ser nuestro codigo cuando esta opcion va a ser elegida en caso de que sea otro menu se llamara a la funcion MenuGenerico y se pasara en parametros correspondientes
                - menu: este es obligatorio si esta la funcion MenuGenerico creada, aqui se pone el diccionario de el menu correspondiente
        - Para acceder a un sub menu tenemos la funcion MenuGenerico. Esta funcion lo que hace es empezar ciclos dentro de nuestro ciclo principal para representar cada menu correspondiente. Tambien se puede llamar MenuGenerico dentro de un MenuGenerico para ingresar a un siguiente menu, ejemplo: menuPrincial>Parametrizacion>Alta. Al Finzalizar una opcion (por ejemplo: alta partido) esta volvera a su menu anterior correspondiente. En caso de pulsar "Atras" esto finalizara el ciclo actual y regresa al ciclo anterior. Si se pone la variable "salirAlMenuPrincipal" como verdadera esta volvera al menu principal directamente finlizando todos los demas ciclos
    Las opciones del munu pueden ser accedidas mediante su descipcion o su clave
    Ventajas: Facil de ampliar, reutilizacion de funciones
    Desventajas: Mayor consumo de Memoria (ya que los bucles quedan abiertos), estructura compleja 
-Partido Politicos: Suponemos que las abreviaturas de los partidos son 3 letras no permitiendo numeros
