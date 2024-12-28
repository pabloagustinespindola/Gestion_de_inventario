# Gestion_de_inventario

Programa de Gestión de Inventario


TABLA DE CONTENIDO:

1. Información general

2. Estado del proyecto

3. Funciones

4. Bugs/errores

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Información general:

    El siguiente programa resulta de utilidad a cualquier tienda pequeña que necesite realizar un seguimiento de inventario. Proporciona herramientas para registrar, mostrar, eliminar o actualizar productos. También ofrece la posibilidad de buscar un producto y de realizar un registro delos productos que se encuentren por debajo de ciertos stock especificado por el usuario

2. Estado del proyecto:

    El proyecto se encuentra finalizado pero puede ser fácilmente ampliado agregando funcionalidades extra. Escrito en Visual Studio Code con lenguaje Python, utiliza el modulo SQLITE3 para crear, acceder y modificar una base de datos con el nombre inventario.db. En esta se crea una tabla con el nombre productos y allí se alojan los datos id, nombre, descripción, cantidad, precio y categoria. 

3. Funciones

Descripción de todas las funciones utilizadas en el programa y su funcionamiento

menú(): Esta función tiene como finalidad única imprimir en pantalla un menú sencillo

crear_tabla(): Esta función es la encargada de acceder a la base de datos (o crearla en caso de que no exista) y crear una tabla llamada productos

es_menor_a_cero(numero): Esta función, como indica su nombre, sirve para comprobar si un numero es positivo. Si lo es, retorna el valor True, en caso contrario, retorna False, lo que la hace especialmente útil en estructuras de control WHILE o IF

buscar_id(id): Esta función accede a la base de datos y busca un elemento por su id. En caso de encontrarlo, retorna True. De otra forma, retorna False

mostrar_elemento(lista): Esta función recorre los elementos de una lista (productos en este caso) e imprime cada uno con el formato:

ID:

Nombre:

Descripción:

Cantidad:

Precio: $

Categoría:

registrar_productos(): Esta función accede a la base de datos, pide al usuario que ingrese cada dato necesario (comprobando que los números sean positivos) y luego agrega esos datos, cada uno en su campo. Finalmente guarda la información y cierra la conexión

mostrar_productos(): Esta función accede a la base de datos, selecciona todos los elementos (productos) y si hay productos guardados, los muestra usando la función mostrar_elemento()

actualizar_producto(): Esta función accede a la base de datos, pide al usuario que ingrese el ID del producto a actualizar y si el producto existe (utilizando la función buscar_id() ) pide al usuario el nuevo valor (comprobando que sea positivo). Finalmente se actualiza el valor del producto y se guarda la información

eliminar_producto(): Esta función accede a la base de datos, pide al usuario que ingrese el ID del producto a eliminar, y si existe (utilizando la función buscar_id() ) lo elimina y guarda la información

buscar_producto(dato): Esta función accede a la base de datos y dependiendo del parámetro dato se ejecuta cierta parte del código, aunque todas con el mismo funcionamiento: pedir la id, el nombre o la categoria del producto, selecciona el o los productos que coincidan con el criterio de búsqueda, y en caso de que se encuentre uno o varios, se lo/s muestra por pantalla

registro_bajo_stock(): Esta función accede a la base de datos, le pide al usuario que ingrese el limite de stock precisado, selecciona y guarda en una lista todos los nombres y cantidades de productos. Luego recorre dicha lista y si la cantidad (indexada en 1) es menor o igual al limite, lo imprime por pantalla

4. Bugs/errores:
    Este programa no contiene errores encontrados, aunque siempre puede haber algún error al ingresar un dato. Si los tipos de datos son incorrectos, por ejemplo ingresar un texto cuando se pide un numero, esto generará un error y el programa se cerrara. Es recomendable prestar atención al ingreso de datos, especialmente al ingresar el precio y la cantidad
