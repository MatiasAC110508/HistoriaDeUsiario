#  INVENTARIO

nombre = input("Ingrese el nombre del producto aquí: ").strip() # Pide el nombre del producto.

while True: # Para que no se cierre el programa.

    try: # Para evitar que se ciaga el programa por errores de caracter.

        precio = float(input("Ingrese el precio del producto aquí: ")) # Pide el precio del programa
        
        if precio < 0: # Para evitar que el precio sea negativo.
            print("Cantidad invalida.\n") # Mensaje informativo para el usuario.
            continue    # Para preguntar de nuevo al usuario.
        break   # Para cerrar el bucle while y continuar con el otro
    
    except ValueError:  # Para que detecte errores de caracter.
        print("Porfavor ingrese un caracter valido para el precio.\n")  # Mensaje informativo para el usuario.

while True:

    try:

        cantidad = int(input("Ingrese la cantidad del producto aquí: "))

        if cantidad < 0:
            print("Cantidad invalida. \n")
            continue
        break

    except ValueError:
        print("Porfavor ingrese un caracter valido para la cantidad.\n")

print("\n Producto registrado correctamente:")  # Informa el exito en el registro.
print(f"Nombre: {nombre}")  # Informa el registro del  nombre.
print(f"Precio unitario: ${precio:,.2f}")   # Informa el registro del precio.
print(f"Cantidad: {cantidad}")  # Informa el registro de la cantidad.
print(f"Costo total en inventario: ${precio * cantidad:,.2f}")  # Infomra el registro del inventario.

"""ESTE PROGRAMA ES PARA REGISTRAR PRODUCTOS EN UN INVENTARIO.

Evita errores de caracteres, no se cierra al ingrear datos erroneos 
y calcula el costo total del inventario del producto.

Name: Matias Aguirre Correa
Clan: Tesla"""


