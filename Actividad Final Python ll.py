#******************************************************            
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida"   
def divisionEntera(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: División por cero no permitida"   
def modulo(a, b):
    return a % b
def exponenciacion(a, b):
    return a ** b
#******************************************************
def igual(a, b):
    return a == b
def diferente(a, b):
    return a != b
def mayor(a, b):
    return a > b
def menor(a, b):
    return a < b
def mayorIgual(a, b):
    return a >= b
def menorIgual(a, b):
    return a <= b
#******************************************************
def yLogico(a, b):
    return print (f"{a} y {b} son positivos") if a>0 and b>0 else print("Uno o ambos números son negativos")
def oLogico(a, b):
    return print (f"{a} o {b} son positivos") if a>0 or b>0 else print("Uno o ambos números son negativos")
def negacionLogica(a, b):
    return print (f"{a} y {b} no son negativos") if not (a>0 and b>0) == False else print("Uno o ambos números son negativos") 
#******************************************************
def asignacion(a, b):
    a = b
    return a
def sumaAsigna(a, b):
    a += b
    return a
def restaAsigna(a, b):
    a -= b
    return a
def multiplicaAsigna(a, b):
    a *= b
    return a
def divideAsigna(a, b):
    a /= b
    return a
def divideEnteroAsigna(a, b):
    a //= b
    return a
def exponenteAsigna(a, b):
    a **= b
    return a
def moduloAsinga(a, b):
    a %= b
    return a
#******************************************************
def bitsAnd (a, b):
    return a & b
def bitsOr (a, b):
    return a | b
def bitsXor (a, b):
    return a ^ b
def bitsNot (a):
    return ~ a
def bitsDesplazaIzq(a, b):
    return a << b
def bitsDesplazaDer(a, b):
    return a >> b
#******************************************************

def menuPrincipal ():
    opcion=0
    while opcion < 7:
        print("""OPERACIONES:
        1. Operaciones Matemáticas
        2. Operaciones de Comparación
        3. Operaciones Lógicas
        4. Operaciones de Asignación
        5. Operaciones de bits
        6. Salir""")
        
        try:
            opcion = int(input("Ingresa el número de la operación (1/2/3/4/5/6): "))
            if opcion in [1, 2, 3, 4, 5 ,6]:
                if opcion == 1:
                    opMatematicas()
                elif opcion == 2:
                    opComparacion()
                elif opcion == 3:
                    opLogicas()
                elif opcion == 4:
                    opAsignacion()
                elif opcion == 5:
                    opBits()
                elif opcion == 6:
                    exit ()
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Opción no válida")

def opMatematicas():
    opcion=0
    while opcion < 6:
        print("""Selecciona la operación matemática:
              1. Suma
              2. Resta
              3. Multiplicación
              4. División
              5. Division Entera
              6. Módulo
              7. Exponenciación
              8. Menu Principal""")
        try:
            opcion = int(input("Ingresa el número de la operación (1/2/3/4/5/6/7/8): "))
        
            if opcion in [1, 2, 3, 4, 5, 6, 7, 8]:
                if opcion < 8:
                    num1 = int(input("Ingresa el primer número: "))
                    num2 = int(input("Ingresa el segundo número: "))
                
                if opcion == 1:
                    print("Resultado: " +str(suma(num1, num2)))
                elif opcion == 2:
                    print("Resultado: " +str(resta(num1, num2)))
                elif opcion == 3:
                    print("Resultado: " +str(multiplicacion(num1, num2)))
                elif opcion == 4:
                    print("Resultado: " +str(division(num1, num2)))
                elif opcion == 5:
                    print("Resultado: " +str(divisionEntera(num1, num2)))
                elif opcion == 6:
                    print("Resultado: " +str(modulo(num1, num2)))
                elif opcion == 7:
                    print("Resultado: " +str(exponenciacion(num1, num2)))
                elif opcion == 8:
                    menuPrincipal ()
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Opción no válida")
def opComparacion():
    opcion=0
    while opcion < 6:
        print("""Selecciona la operación de comparación:
              1. Igual a
              2. Diferente de
              3. Mayor que
              4. Menor que
              5. Mayor o igual que
              6. Menor o igual que
              7. Menu Principal""")
        try:
            opcion = int(input("Ingresa el número de la operación (1/2/3/4/5/6/7): "))
            
            if opcion in [1, 2, 3, 4, 5, 6, 7]:
                if opcion < 7:
                    num1 = int(input("Ingresa el primer número: "))
                    num2 = int(input("Ingresa el segundo número: "))
                
                if opcion == 1:
                    print("Resultado: " +str(igual(num1, num2)))
                elif opcion == 2:
                    print("Resultado: " +str(diferente(num1, num2)))
                elif opcion == 3:
                    print("Resultado: " + str(mayor(num1, num2)))
                elif opcion == 4:
                    print("Resultado: " + str(menor(num1, num2)))
                elif opcion == 5:
                    print("Resultado: " + str(mayorIgual(num1, num2)))
                elif opcion == 6:
                    print("Resultado: " + str(menorIgual(num1, num2)))
                elif opcion == 7:
                    menuPrincipal ()
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Opción no válida")
def opLogicas():
    opcion=0
    while opcion < 4:
        print("""Selecciona la operación de comparación:
              1. Y Lógico
              2. O Lógico
              3. Negación Lógica
              4. Menu Principal""")
        try:
            opcion = int(input("Ingresa el número de la operación (1/2/3/4): "))
            
            if opcion in [1, 2, 3, 4]:
                if opcion < 4:
                    num1 = int(input("Ingresa el primer número: "))
                    num2 = int(input("Ingresa el segundo número: "))
                
                if opcion == 1:
                    yLogico (num1,num2)
                elif opcion == 2:
                    oLogico(num1, num2)
                elif opcion == 3:
                    negacionLogica(num1, num2)
                elif opcion == 4:
                    menuPrincipal ()
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Opción no válida")
def opAsignacion():
    opcion=0
    while opcion < 9:
        print("""Selecciona la operación de asignación:
              1. Asignación
              2. Suma y asigna
              3. Resta y asigna
              4. Multiplica y asigna
              5. Divide y asinga
              6. División entera y asinga
              7. Exponente y asigna
              8. Modulo y asigna
              9. Menu Principal""")
        try:
            opcion = int(input("Ingresa el número de la operación (1/2/3/4/5/6/7/8/9): "))
            
            if opcion in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if opcion < 9:
                    num1 = int(input("Ingresa el primer número: "))
                    num2 = int(input("Ingresa el segundo número: "))
                
                if opcion == 1:
                    print("Resultado: " +str(asignacion(num1, num2)))
                elif opcion == 2:
                    print("Resultado: " +str(sumaAsigna(num1, num2)))
                elif opcion == 3:
                    print("Resultado: " + str(restaAsigna(num1, num2)))
                elif opcion == 4:
                    print("Resultado: " + str(multiplicaAsigna(num1, num2)))
                elif opcion == 5:
                    print("Resultado: " +str(divideAsigna(num1, num2)))
                elif opcion == 6:
                    print("Resultado: " + str(divideEnteroAsigna(num1, num2)))
                elif opcion == 7:
                    print("Resultado: " + str(exponenteAsigna(num1, num2)))
                elif opcion == 8:
                    print("Resultado: " + str(moduloAsinga(num1, num2)))
                elif opcion == 9:
                    menuPrincipal ()
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Opción no válida")
def opBits():
    opcion=0
    while opcion < 7:
        print("""Selecciona la operación en el nivel de bits de los datos:
              1. AND a nivel de Bits
              2. OR a nivel de Bits
              3. XOR a nivel de Bits
              4. NOT a nivel de Bits
              5. Desplazamiento a la izquierda
              6. Desplazamiento a la derecha
              7. Menu Principal""")
        try:
            opcion = int(input("Ingresa el número de la operación (1/2/3/4/5/6/7): "))
            
            if opcion in [1, 2, 3, 4, 5, 6, 7]:
                if opcion < 7:
                    num1 = int(input("Ingresa el primer número: "))
                    num2 = int(input("Ingresa el segundo número: "))
                
                if opcion == 1:
                    print("Resultado: " +str(bitsAnd(num1, num2)))
                elif opcion == 2:
                    print("Resultado: " +str(bitsOr(num1, num2)))
                elif opcion == 3:
                    print("Resultado: " + str(bitsXor(num1, num2)))
                elif opcion == 4:
                    print("Resultado: " + str(bitsNot(num1)))
                elif opcion == 5:
                    print("Resultado: " + str(bitsDesplazaIzq(num1, num2)))
                elif opcion == 6:
                    print("Resultado: " +str(bitsDesplazaDer(num1, num2)))
                elif opcion == 7:
                    menuPrincipal ()
            else:
                print("Opción no válida. Intenta de nuevo.")
        except ValueError:
            print("Opción no válida")

menuPrincipal()
