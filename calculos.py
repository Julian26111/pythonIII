def calcularTotal (productos,cantidades):
    total = 0
    for producto, precio in productos.items():
        cantidad = cantidades.get(producto, 0)
        subtotal = cantidad*precio
        total += subtotal
        print (f"{cantidad} {producto.upper()} precio unitario ${precio:.2f}, subtotal ${subtotal:.2f}")
    print (f"Total a pagar: ${total:.2f}")