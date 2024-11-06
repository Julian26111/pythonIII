def mostrarProducto(productos):
    cantidades = {}
    for producto in productos:
        try:
            cantidad = int(input(f"Ingrese la cantidad de {producto.upper()}: "))
            cantidades [producto] = cantidad
        except ValueError:
            print ("Cantidad errada")    
    return cantidades