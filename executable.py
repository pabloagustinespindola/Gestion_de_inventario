# Programa de Gestión de Inventario. 

import sqlite3


def menu():
    print("""
----------------------------------------
    SISTEMA DE GESTIÓN DE INVENTARIO          
----------------------------------------
  1. Registrar producto                           
  2. Mostrar productos                            
  3. Actualizar stock de un producto                          
  4. Eliminar producto                            
  5. Buscar producto                              
  6. Registro de bajo stock                       
  7. Salir                                        
----------------------------------------
""")

def crear_tabla():
    #Funcion que crea una tabla para almacenar los datos de cada producto
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, descripcion TEXT, cantidad INTEGER NOT NULL, precio REAL NOT NULL, categoria TEXT)")
    conn.commit()
    conn.close()

# FUNCIONES EXTRA -----------------------------
def es_menor_a_cero(numero):
    if numero <= 0:
        return True
    else:
        return False

def buscar_id(id):
    # Función que busca un elemento y retorna True si lo encuentra
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    # Buscar el elemento
    cursor.execute("SELECT * FROM productos WHERE id = ?", (str(id)))
    respuesta = cursor.fetchall()

    # Retornar si existe o no en el inventario
    if len(respuesta) > 0:
        return True
    else:
        return False

def mostrar_elemento(lista):
    for producto in lista:
        print(f'''
ID: {producto[0]}
Nombre: {producto[1]}
Descripción: {producto[2]}
Cantidad: {producto[3]}
Precio: ${producto[4]}
Categoria: {producto[5]}
''')

# FUNCIONALIDADES ------------------------------------------
def registrar_producto():
    # Función que permite al ususario registrar productos usando los 
    # datos nombre, descripcion, cantidad, precio y categoria   
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    # Ingreso de datos
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese una descipcion del producto: ")
    cantidad = int(input("Ingrese la cantidad en stock: "))
    while es_menor_a_cero(cantidad):
        cantidad = int(input("Ingrese una cantidad mayor a 0: "))
    precio = float(input("Ingrese el precio del producto: $"))
    while es_menor_a_cero(precio):
        precio = float(input("Ingrese un precio mayor a 0: $"))
    categoria = input("Ingrese la categoria del producto: ")
    # Insertar productos en la tabla
    cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)", (nombre, descripcion, cantidad, precio, categoria))
    conn.commit()
    conn.close()

def mostrar_productos():
    # Función que muestra en pantalla todos los productos del inventario de forma ordenada
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM productos")
    respuesta = cursor.fetchall()
    if len(respuesta) > 0:
        mostrar_elemento(respuesta)
        
    else:
        print("No hay productos ingresados")
    conn.close()
    input("\nPresione enter para volver al menu")

def actualizar_producto():
    # Funcion que permite al usuario actualizar los datos de un producto en particular
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    # Preguntar que producto se actualizará
    id = input("Ingrese el id del producto que desea actualizar: ")

    if buscar_id(id): #Comprobar si el id existe

        # Pedir al usuario que ingrese el nuevo valor
        nuevo_valor = int(input("Ingrese la nueva cantidad en stock: "))
        while es_menor_a_cero(nuevo_valor):
            nuevo_valor = input("Ingrese una cantidad mayor a cero: ")

        # Actualizar el producto
        cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nuevo_valor, id))
        conn.commit()
        conn.close()

    else:
        print("El producto no existe")

def eliminar_producto():
    # Función que permite al usuario eliminar un producto pidiendole el id
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    #Pedir al usuario el id del prodcuto a eliminar
    id = int(input("\nIngrese el id del producto que desea eliminar: "))

    if buscar_id(id): #Comprobar si el id existe

        #Borrar producto
        cursor.execute("DELETE FROM productos WHERE id = ?", (str(id)))
        conn.commit()
        conn.close()
    else:
        print("El producto no existe")
    input("\nPresione enter para volver al menu")

def buscar_producto(dato):
    # Función que busca y muestra por pantalla uno o varios productos que coincidan con el criterio de búsqueda
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    
    if dato == "id":
        id = input("Ingrese el ID del producto: ")
        # Buscar el producto en el inventario por su id
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
        producto = cursor.fetchall()
        
        if len(producto) > 0:
            mostrar_elemento(producto)
            
        else:
            print("El producto no existe en el inventario")
        conn.close()
        input("\nPresione enter para volver al menu")

    elif dato == "nombre":
        nombre = input("Ingrese el nombre del producto: ")
        # Buscar el producto en el inventario por su nombre
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
        producto = cursor.fetchall()

        if len(producto) > 0:
            mostrar_elemento(producto)
            
        else:
            print("El producto no existe en el inventario")
        conn.close()
        input("Presione enter para volver al menu")

    elif dato == "categoria":
        categoria = input("Ingrese la categoría del producto: ")
        # Buscar productos por su categoria
        cursor.execute("SELECT * FROM productos WHERE categoria = ?", (categoria,))
        producto = cursor.fetchall()

        if len(producto) > 0:
            mostrar_elemento(producto)
        else:
            print("El producto no existe en el inventario")
        conn.close()
        input("Presione enter para volver al menu")
    else:
        print("Revise los datos ingresados")
        input("Presione enter para volver al menu")
  
def registro_bajo_stock():
    # Función que compara todos los productos del inventario con
    # el límite (fijado por el ususario) e imprime por pantalla los
    # que se encuentren por debajo de dicho limite
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    # Pedir limite
    limite_stock = int(input("Ingrese el limite de stock: "))
    while es_menor_a_cero(limite_stock):
        limite_stock = int(input("Ingrese un número mayor a 0: "))
    cursor.execute("SELECT nombre, cantidad FROM productos")
    respuesta = cursor.fetchall()
    print("Productos con bajo stock: ")
    for elemento in respuesta:
        if elemento[1] <= limite_stock:
            print(f"Nombre: {elemento[0]}")
            print(f"Stock: {elemento[1]}")

    conn.close()
    input("\nPresione enter para volver al menu")

# MAIN -------------------------------
def main():
    crear_tabla()
    while True:
        menu()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1: # Registro de producto
            registrar_producto()
        elif opcion == 2: # Mostrar productos
            mostrar_productos()
        elif opcion == 3: # Actualizar producto
            actualizar_producto()
        elif opcion == 4: # Eliminar producto
            eliminar_producto()
        elif opcion == 5: # Buscar producto
            dato = input("\n¿Desea buscar el producto por 'id', 'nombre' o 'categoria'?: ")
            buscar_producto(dato)
        elif opcion == 6: # Registro de bajo stock
            registro_bajo_stock()
        elif opcion == 7: # Salir
            print("Saliendo...")
            break
        else:
            print("Ingrese un numero valido (1 al 7): ")

main()
