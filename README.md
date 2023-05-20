# LPG
UADE Copa Algoritmia 2023

## Desarrollado por:
- Bruno, Gustavo: https://github.com/geb2701 https://www.linkedin.com/in/gustavo-ezequiel-bruno-5197a218b/

## Link del Proyecto
- URL de GITHUB

## Aclaraciones
- Menus: Nuestro Programa esta usando menus de consola para acceder a todas las funcionalidad. 
    Este funciona de la siguente manera:
        - Tenemos un bucle inical que mientras este activo va a hacer que el programa este activo al terminarse finaliza el programa
        - Las opciones de menu se crear con bibliotecas con valor especificos para asi poder ser llamadas correctamente
            - Clave: es un numero de nuestra opcion
            - Valores:
                - descripcion: valor que va a ser el titulo de nuestra opcion y tambien puede ser eleguida como opcion
                - funcion: es la funcion asociada, es decir que va a ser nuestro codigo cuando esta opcion va a ser elegida en caso de que sea otro menu se llamara a la funcion MenuGenerico y se pasara en parametros correspondientes
                - menu: este es obligatorio si esta la funcion MenuGenerico creada, aqui se pone el diccionario de el menu correspondiente
        - Para acceder a un sub menu tenemos la funcion MenuGenerico. Esta funcion lo que hace es empezar ciclos dentro de nuestro ciclo principal para representar cada menu correspondiente. Tambien se puede llamar MenuGenerico dentro de un MenuGenerico para ingresar a un siguiente menu, ejemplo: menuPrincial>Parametrizacion>Alta. Al Finzalizar una opcion (por ejemplo: alta partido) esta volvera a su menu anterior correspondiente. En caso de pulsar "Atras" esto finalizara el ciclo actual y regresa al ciclo anterior. Si se pone la variable "salirAlMenuPrincipal" como verdadera esta volvera al menu principal directamente finlizando todos los demas ciclos
    Las opciones del munu pueden ser accedidas mediante su descipcion o su clave
-Partido Politicos: Suponemos que las abreviaturas de los partidos son 3 letras y su numero va desde el 1 al 999 y tambien que es su clave
-While: Evitamos usar los break