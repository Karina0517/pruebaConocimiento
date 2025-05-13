'''Funcionalidades principales: para alcanzar un resultado óptimo en esta prueba, deberás:
1. Añadir productos al inventario: permitir al usuario agregar productos con atributos como
nombre, precio y cantidad disponibles.
2. Consultar productos en inventario: buscar un producto por su nombre y mostrar sus
detalles (nombre, precio, cantidad).
3. Actualizar precios de productos: modificar el precio de un producto específico en el
inventario.
4. Eliminar productos del inventario: permitir la eliminación de un producto que ya no está
disponible.
5. Calcular el valor total del inventario: multiplicar el precio por la cantidad de cada producto
y mostrar el total acumulado.
Criterios de aceptación:
• El programa debe permitir agregar al menos 5 productos iniciales.
• Al consultar un producto, debe indicar si no existe en el inventario con un mensaje claro.
• La actualización de precios debe validar que el nuevo precio sea un número positivo.
• La eliminación de un producto debe confirmar su existencia antes de borrarlo.
• El cálculo del valor total del inventario debe ser preciso y mostrar el resultado con dos
decimales.
• El código debe estar estructurado en funciones para cada operación y debe incluir
comentarios explicativos.
• El código y los comentarios deben estar 100% sin excepción alguna en inglés'''


inventory = {}

def validateNumber(mensaje):
    while True:
        value = input(mensaje)
        try:
            valueF = float(value)
            if valueF < 0:
                print("No se permiten números menores que cero.")
                continue
            else:
                return valueF
        except ValueError:
            print("Debes ingresar un número.")
            
def validateStr(message):
    while True:
        entrance = input(message).strip()
        if entrance.isalpha():
            return entrance
        else:
            print(" Solo se permiten letras, no se permiten números o caracteres especiales.")

def addProduct():
    
        name = validateStr("Nombre del producto a agregar: ").lower()
        if name in inventory:
            return False
        price = validateNumber("Precio del producto: ")
        cant = validateNumber("Cantidad disponible: ")
        inventory[name] = (price, cant)
        return True

def searchProduct():
    name = validateStr("Nombre del producto a buscar: ").lower()
    if name in inventory:
        return name, inventory[name]
    return None

def updatePrice():
    name = validateStr("Nombre del producto a actualizar: ").lower()
    if name in inventory:
        newPrice = validateNumber("Nuevo precio: ")
        quant = inventory[name][1]
        inventory[name] = (newPrice, quant)
        return True
    else:
        return False

def updateQuant():
    name = validateStr("Nombre del producto a actualizar: ").lower()
    if name in inventory:
        newQuant = validateNumber("Nueva cantidad: ")
        price = inventory[name][0]
        inventory[name] = (price, newQuant)
        return True
    else:
        return False

def deleteProduct():
    name = validateStr("Nombre del producto a eliminar: ").lower()
    
    if name in inventory:
        price = inventory[name][1]
        if price == 0:
            del inventory[name]
            return True
    else:
            return False

def showInventory():
    return inventory

calculateTotal = lambda precio, quant: precio * quant

def valueTotal():
    total = 0
    for price, quant in inventory.values():
        total += calculateTotal(price, quant)
    return total

def fiveProducts():
        q = 0
        if len(inventory) < 5:
            
            while q < 5:
                if addProduct():
                    print("Producto agregado correctamente.")
                    q += 1
                else:
                     print("El producto ya existe.")
        else:
            if addProduct():
                print("Producto agregado correctamente.")
                
            else:
                print("El producto ya existe.")
              

def menu():
    while True:
        print("¡BIENVENIDOS AL SUPERMERCADO KARINA!\n"
              "(1) Agregar producto al inventario. \n"
              "(2) BUscar un producto en el inventario. \n"
              "(3) Actualizar el precio de algún producto. \n"
              "(4) Actualizar la cantidad de algún producto. \n"
              "(5) Eliminar algún producto del inventario. \n"
              "(6) Mostrar el inventario. \n"
              "(7) Ver el total $ del inventario. \n"
              "(8) Salir del programa.\n")

        option = input("Selecciona una opción: ")

        match option:
            case "1":
                fiveProducts()
            case "2":
                result = searchProduct()
                if result:
                    name, (price, quant) = result
                    print(f"{name} - Precio: ${price:,.2f}, Cantidad: {quant}")
                else:
                    print("Producto no encontrado.")
            case "3":
                if updatePrice():
                    print("Precio actualizado.")
                else:
                    print("Producto no encontrado.")
            case "4":
                if updateQuant():
                    print("Cantidad actualizada.")
                else:
                    print("Producto no encontrado.")
            case "5":
                if deleteProduct():
                    print("Producto eliminado.")
                else:
                    print("El producto no existe ó su cantidad es diferente de 0.")
            case "6":
                show = showInventory()
                if not show:
                    print("NO hay productos en el inventario.")
                else:
                    print("Inventario actual:")
                    for name, (price, quant) in show.items():
                        print(f"- {name}: Precio ${price:,.2f}, Cantidad: {quant}")
            case "7":
                total = valueTotal()
                print(f"Valor total calculado del inventario: ${total:,.2f}")
            case "8":
                print("Saliste del programa.")
                break
            case _:
                print("Ésta opción no existe, elige una que si lo sea.")

menu()