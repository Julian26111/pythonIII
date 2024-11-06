import precioProducto
import cantidadProducto
import calculos
def menu():
    opc = None
    while opc != 4:
        print ("""
MENU PRINCIPAL
1.Pedir Valor Productos
2.Pedir Cantidad Productos
3.Mostrar Totales
4.Salir """)
        try:
            opc = int(input("Elija una opción: "))
            if   opc==1: productos=precioProducto.pedirProducto()
            elif opc==2: cantidades=cantidadProducto.mostrarProducto(productos)
            elif opc==3: calculos.calcularTotal(productos,cantidades)
            elif opc==4: print("Saliendo...")
            else:        print("Opción no valida ")
        except ValueError:
            print("Entrada no válida. Por favor, intenta nuevamente")
menu()