# Imprime el mensaje de bienvenida de la tienda
print("Tienda Riwi, Bienvenid@s")

# Muestra las opciones disponibles para el usuario
print("1. Comprar")
print("2. Salir")

# Manejo de errores al ingresar una opción
try:
    opcion = int(input("Selecciona una opción: "))  # Solicita al usuario que ingrese una opción numérica
except ValueError:  # Captura errores si el usuario ingresa un valor no numérico
    print("Error: Debes ingresar un número entero.")

# Si el usuario elige comprar (opción 1)
if opcion == 1:
    while True:  # Bucle para garantizar entrada válida
        product = input("Ingresa el producto que deseas comprar: ").strip()  # Solicita nombre del producto, eliminando espacios extra
        if product and all(char.isalpha() or char.isspace() for char in product):  # Verifica que el nombre solo contenga letras y espacios
            print(f"Elegiste el producto: {product}")  # Confirma selección del producto
            break  # Sale del bucle cuando el producto es válido
        else:
            print("Por favor, ingresa un producto válido.")  # Mensaje de error si la entrada no es válida

    while True:  # Bucle para garantizar entrada válida
        try:
            precio_producto = int(input("Ingresa el precio de tu producto: "))  # Solicita el precio del producto
            break  # Sale del bucle cuando el precio es válido
        except ValueError:  # Captura errores si el usuario ingresa un valor no numérico
            print("Error: Ingresa una cantidad válida.")  # Mensaje de error

    while True:  # Bucle para garantizar entrada válida
        try:
            cantidad_productos = int(input("Cuántos productos deseas?: "))  # Solicita cantidad de productos
            descuento = int(input("Ingresa el descuento deseado(%): "))  # Solicita el porcentaje de descuento

            if descuento < 0 or descuento <= 100:  # Verifica si el descuento está en el rango adecuado
                porcentaje = precio_producto * descuento / 100  # Calcula la cantidad de descuento
                precio_final = precio_producto - porcentaje  # Calcula el precio final con descuento
                Total = precio_final * cantidad_productos  # Multiplica por la cantidad de productos

                # Muestra los resultados del cálculo
                print(f"El precio de cada producto individual es: {precio_producto}")
                print(f"El precio final de {product} es: {Total}")
                print("Gracias por comprar en la tienda Riwi!!")
            break  # Sale del bucle cuando las entradas son válidas
        except ValueError:  # Captura errores si el usuario ingresa un valor no numérico
            print("El descuento tiene que estar en un rango entre 0% y 100%")  # Mensaje de error

# Si el usuario elige salir (opción 2)
elif opcion == 2:
    print("Gracias por visitarnos!")  # Mensaje de despedida
