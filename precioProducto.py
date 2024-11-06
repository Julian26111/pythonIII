def pedirProducto():
    productos = {}
    while True:
        producto = input("Ingrese el nombre del producto ('fin' para terminar): ")
        if producto.lower() == 'fin':
            break
        try:
            precio = float(input(f"Ingrese el precio unitario de {producto.upper()}: "))
            productos [producto] = precio
        except ValueError:
            print ("Valor errado")    
    return productos